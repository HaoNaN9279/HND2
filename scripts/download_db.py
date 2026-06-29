#!/usr/bin/env python3
"""
命运2 简体中文离线 SQLite 数据库下载脚本

用法：
  1. 设置环境变量 BUNGIE_API_KEY（在 https://www.bungie.net/en/Application 注册获取）
  2. python scripts/download_db.py          # 下载/更新数据库
     python scripts/download_db.py --check  # 仅检查版本，不下载
     python scripts/download_db.py --force  # 强制重新下载

配置：
  - 数据库保存路径：destiny2_zh-chs.sqlite3（项目根目录）
  - 版本缓存文件：.db_version（记录当前数据库版本）
"""

import argparse
import json
import os
import sys
import urllib.request
import zipfile
import tempfile
import shutil
from pathlib import Path

# ---------- 配置 ----------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "destiny2_zh-chs.sqlite3"
VERSION_FILE = PROJECT_ROOT / ".db_version"

MANIFEST_URL = "https://www.bungie.net/Platform/Destiny2/Manifest/"
BUNGIE_BASE = "https://www.bungie.net"
LANGUAGE = "zh-chs"
TIMEOUT = 120  # 下载超时（秒）
# ------------------------


def get_api_key() -> str:
    """从环境变量读取 Bungie API Key。"""
    key = os.environ.get("BUNGIE_API_KEY")
    if not key:
        print("错误：未设置 BUNGIE_API_KEY 环境变量。")
        print("请通过 https://www.bungie.net/en/Application 注册应用获取 API Key。")
        print("设置方法：")
        if sys.platform == "win32":
            print('  set BUNGIE_API_KEY=你的密钥')
        else:
            print('  export BUNGIE_API_KEY=你的密钥')
        sys.exit(1)
    return key


def fetch_manifest(api_key: str) -> dict:
    """请求 Bungie Manifest API，返回 JSON 数据。"""
    req = urllib.request.Request(MANIFEST_URL)
    req.add_header("X-API-Key", api_key)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"请求 Manifest 失败：{e}")
        sys.exit(1)

    if data.get("ErrorCode") != 1:
        print(f"Bungie API 返回错误：{data.get('ErrorStatus', 'unknown')}")
        sys.exit(1)

    return data["Response"]


def get_local_version() -> str | None:
    """读取本地版本缓存。"""
    if VERSION_FILE.exists():
        return VERSION_FILE.read_text(encoding="utf-8").strip()
    return None


def save_local_version(version: str):
    """保存版本号到缓存文件。"""
    VERSION_FILE.write_text(version.strip(), encoding="utf-8")
    print(f"版本已记录：{version.strip()}")


def download_database(download_path: str, api_key: str) -> bool:
    """下载数据库 zip 并解压为 .sqlite3 文件。"""
    url = f"{BUNGIE_BASE}{download_path}"
    print(f"正在下载数据库（{url}）...")

    # 流式下载到临时文件
    req = urllib.request.Request(url)
    req.add_header("X-API-Key", api_key)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            total = int(resp.headers.get("Content-Length", 0))
            downloaded = 0
            chunk_size = 1024 * 1024  # 1MB

            with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as tmp:
                tmp_path = tmp.name
                while True:
                    chunk = resp.read(chunk_size)
                    if not chunk:
                        break
                    tmp.write(chunk)
                    downloaded += len(chunk)
                    if total > 0:
                        pct = downloaded * 100 // total
                        print(f"\r  进度：{downloaded // (1024*1024)}MB / {total // (1024*1024)}MB ({pct}%)", end="")
                print()
    except Exception as e:
        print(f"下载失败：{e}")
        return False

    # 解压
    print("正在解压...")
    try:
        with zipfile.ZipFile(tmp_path, "r") as zf:
            # 找到 .content 文件
            content_files = [n for n in zf.namelist() if n.endswith(".content")]
            if not content_files:
                print("错误：ZIP 内未找到 .content 文件")
                os.unlink(tmp_path)
                return False

            # 解压到临时位置
            extract_dir = tempfile.mkdtemp()
            zf.extractall(extract_dir)
            content_path = os.path.join(extract_dir, content_files[0])

            # 改名复制到目标路径
            shutil.copy2(content_path, DB_PATH)
            shutil.rmtree(extract_dir)
    except Exception as e:
        print(f"解压失败：{e}")
        os.unlink(tmp_path)
        return False
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

    db_size = DB_PATH.stat().st_size // (1024 * 1024)
    print(f"数据库已保存：{DB_PATH}（{db_size}MB）")
    return True


def main():
    parser = argparse.ArgumentParser(description="命运2 简体中文离线数据库下载器")
    parser.add_argument("--check", action="store_true", help="仅检查版本，不下载")
    parser.add_argument("--force", action="store_true", help="强制重新下载（即使版本相同）")
    args = parser.parse_args()

    api_key = get_api_key()

    # 获取 Manifest
    print("正在获取 Manifest 版本信息...")
    manifest = fetch_manifest(api_key)

    # 提取简体中文数据库路径
    mobile_paths = manifest.get("mobileWorldContentPaths", {})
    download_path = mobile_paths.get(LANGUAGE)
    if not download_path:
        print(f"错误：Manifest 中未找到 {LANGUAGE} 语言条目")
        sys.exit(1)

    # 提取版本标识（来自 manifest 的 version 字段）
    remote_version = manifest.get("version", download_path)
    local_version = get_local_version()

    print(f"  远程版本：{remote_version}")
    print(f"  本地版本：{local_version or '（无）'}")

    if args.check:
        if not DB_PATH.exists():
            print("状态：数据库不存在")
            sys.exit(2)
        if local_version != remote_version:
            print("状态：数据库需要更新")
            sys.exit(2)
        print("状态：数据库已是最新")
        return

    # 判断是否需要下载
    db_exists = DB_PATH.exists()
    version_match = local_version == remote_version

    if db_exists and version_match and not args.force:
        db_size = DB_PATH.stat().st_size // (1024 * 1024)
        print(f"数据库已是最新（{db_size}MB，版本 {remote_version}），跳过下载。")
        print("如需强制重新下载请使用 --force。")
        return

    if args.force:
        print("强制下载模式...")

    # 开始下载
    if not db_exists:
        print("未找到本地数据库，开始下载...")
    else:
        print("版本不一致，开始更新...")

    success = download_database(download_path, api_key)
    if not success:
        sys.exit(1)

    save_local_version(remote_version)
    print("完成！")


if __name__ == "__main__":
    main()
