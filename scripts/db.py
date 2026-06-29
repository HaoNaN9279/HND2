# -*- coding: utf-8 -*-
"""
命运2 数据库通用工具模块

用法：
    from scripts.db import get_conn, load_json, SLOT_TYPES, resolve_perk_name, search_perk, search_items

依赖：Python 标准库 sqlite3 + json
"""

import sqlite3
import json
from pathlib import Path

# ---------- 常量 ----------

# 武器槽类型 hash
SLOT_KINETIC = 1498876634      # 动能（一号位）
SLOT_ENERGY = 2465295065       # 能量（二号位）
SLOT_POWER = 953998645         # 重武器（三号位）

SLOT_TYPES = {
    SLOT_KINETIC: "动能",
    SLOT_ENERGY: "能量",
    SLOT_POWER: "重武器",
}

# 项目根目录
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "destiny2_zh-chs.sqlite3"


# ---------- 数据库连接 ----------

def get_conn():
    """获取数据库连接。"""
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"数据库未找到：{DB_PATH}\n"
            "请先运行：python scripts/download_db.py"
        )
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA journal_mode=WAL")  # 提升并发读取性能
    return conn


def load_json(val) -> dict | None:
    """将 SQLite BLOB/TEXT 字段解析为 JSON 对象。"""
    if val is None:
        return None
    if isinstance(val, bytes):
        return json.loads(val.decode("utf-8"))
    if isinstance(val, str):
        return json.loads(val)
    return val


# ---------- ID 转换 ----------

def to_signed(hash_val: int) -> int:
    """将无符号 32 位 hash 转为有符号（数据库 id 格式）。"""
    return hash_val if hash_val < 2**31 else hash_val - 2**32


def to_unsigned(id_val: int) -> int:
    """将有符号数据库 id 转为无符号（JSON hash 格式）。"""
    return id_val if id_val >= 0 else id_val + 2**32


# ---------- 查询工具 ----------

def resolve_perk_name(cur, plug_hash: int) -> str:
    """
    从 plug item hash 解析为可读的 Perk 名称。
    
    查询链路：
        DestinyInventoryItemDefinition (plug)
        -> perks[].perkHash
        -> DestinySandboxPerkDefinition.displayProperties.name
    """
    sid = to_signed(plug_hash)
    cur.execute("SELECT json FROM DestinyInventoryItemDefinition WHERE id=?", (sid,))
    row = cur.fetchone()
    if not row:
        return f"(hash:{plug_hash})"
    plug = load_json(row[0])
    if not plug:
        return f"(hash:{plug_hash})"

    # 优先从 sandbox perk 取名称
    for perk in plug.get("perks", []):
        pkh = perk.get("perkHash", 0)
        if pkh:
            cur.execute("SELECT json FROM DestinySandboxPerkDefinition WHERE id=?", (to_signed(pkh),))
            spr = cur.fetchone()
            if spr:
                sp_data = load_json(spr[0])
                if sp_data:
                    name = sp_data.get("displayProperties", {}).get("name", "")
                    if name:
                        return name

    # 回退到插件自身的 displayProperties.name
    return plug.get("displayProperties", {}).get("name", f"(hash:{plug_hash})")


def resolve_perk_with_description(cur, plug_hash: int) -> tuple[str, str]:
    """
    解析 perk 名称和描述。
    返回 (name, description)
    """
    sid = to_signed(plug_hash)
    cur.execute("SELECT json FROM DestinyInventoryItemDefinition WHERE id=?", (sid,))
    row = cur.fetchone()
    if not row:
        return f"(hash:{plug_hash})", ""

    plug = load_json(row[0])
    if not plug:
        return f"(hash:{plug_hash})", ""

    for perk in plug.get("perks", []):
        pkh = perk.get("perkHash", 0)
        if pkh:
            cur.execute("SELECT json FROM DestinySandboxPerkDefinition WHERE id=?", (to_signed(pkh),))
            spr = cur.fetchone()
            if spr:
                sp_data = load_json(spr[0])
                if sp_data:
                    dp = sp_data.get("displayProperties", {})
                    name = dp.get("name", "")
                    desc = dp.get("description", "")
                    return name, desc

    return (
        plug.get("displayProperties", {}).get("name", f"(hash:{plug_hash})"),
        plug.get("displayProperties", {}).get("description", ""),
    )


def search_perk(cur, keyword: str) -> list[dict]:
    """
    在 DestinySandboxPerkDefinition 中按关键词搜索 Perk。
    
    返回列表，每项包含 hash、名称、描述。
    """
    cur.execute(
        "SELECT json FROM DestinySandboxPerkDefinition WHERE json LIKE ?",
        (f"%{keyword}%",),
    )
    results = []
    for (row,) in cur.fetchall():
        data = load_json(row)
        if data:
            dp = data.get("displayProperties", {})
            name = dp.get("name", "")
            desc = dp.get("description", "")
            results.append({
                "hash": data.get("hash", 0),
                "name": name,
                "description": desc,
            })
    return results


def search_items(cur, keyword: str, item_type: str | None = None) -> list[dict]:
    """
    在 DestinyInventoryItemDefinition 中按关键词搜索物品。
    
    item_type: 可选过滤，如 "手炮"、"脉冲步枪" 等
    返回列表，每项包含 id、名称、类型、品质等级。
    """
    cur.execute(
        "SELECT id, json FROM DestinyInventoryItemDefinition WHERE json LIKE ?",
        (f"%{keyword}%",),
    )
    results = []
    for (id_val, rj) in cur.fetchall():
        data = load_json(rj)
        if not data:
            continue
        dp = data.get("displayProperties", {})
        name = dp.get("name", "")
        itype = data.get("itemTypeDisplayName", "")
        tier = data.get("inventory", {}).get("tierTypeName", "")
        slot = data.get("equippingBlock", {}).get("equipmentSlotTypeHash", 0)

        if item_type and item_type != itype:
            continue

        results.append({
            "id": id_val,
            "name": name,
            "type": itype,
            "tier": tier,
            "slot_type": slot,
            "slot_name": SLOT_TYPES.get(slot, ""),
        })

    return results


def find_weapons_with_perks(cur, plug_hashes: list[int]) -> list[dict]:
    """
    查找同时包含指定 Perk 组合的武器。
    
    plug_hashes: Perk 插件的 hash 列表（无符号），每项在 JSON 中至少出现一种表示（有符号/无符号）即为匹配
    返回武器列表。
    """
    # 每项 hash 生成一组候选字符串（有符号 + 无符号）
    candidates = []
    for h in plug_hashes:
        candidates.append({str(h), str(to_signed(h))})

    # 用所有候选构建 LIKE 筛选（减少扫描量）
    all_forms = set()
    for c in candidates:
        all_forms |= c
    like_clauses = " OR ".join([f"json LIKE '%{f}%'" for f in all_forms])

    cur.execute(f"""
        SELECT id, json FROM DestinyInventoryItemDefinition
        WHERE json LIKE '%equippingBlock%'
          AND ({like_clauses})
    """)

    results = []
    for (id_val, rj) in cur.fetchall():
        data = load_json(rj)
        if not data:
            continue
        txt = rj if isinstance(rj, str) else rj.decode("utf-8", errors="replace")

        # 检查每项 hash：至少有一种形式存在于 JSON 中
        matched_all = True
        for c in candidates:
            if not any(f in txt for f in c):
                matched_all = False
                break
        if not matched_all:
            continue

        dp = data.get("displayProperties", {})
        slot = data.get("equippingBlock", {}).get("equipmentSlotTypeHash", 0)

        results.append({
            "id": id_val,
            "name": dp.get("name", ""),
            "type": data.get("itemTypeDisplayName", ""),
            "tier": data.get("inventory", {}).get("tierTypeName", ""),
            "slot_type": slot,
            "slot_name": SLOT_TYPES.get(slot, str(slot)),
        })

    return results


def get_weapon_socket_analysis(cur, weapon_id: int) -> dict | None:
    """
    分析指定武器的插槽和 Perk 结构。
    
    返回包含 categories 和 sockets 的字典。
    """
    cur.execute("SELECT json FROM DestinyInventoryItemDefinition WHERE id=?", (weapon_id,))
    row = cur.fetchone()
    if not row:
        return None

    data = load_json(row[0])
    if not data:
        return None

    display = data.get("displayProperties", {})
    sockets = data.get("sockets", {})

    # Socket categories
    categories = []
    for cat in sockets.get("socketCategories", []):
        ch = cat.get("socketCategoryHash", 0)
        cur.execute("SELECT json FROM DestinySocketCategoryDefinition WHERE id=?", (to_signed(ch),))
        cat_row = cur.fetchone()
        cat_name = ""
        if cat_row:
            cd = load_json(cat_row[0])
            if cd:
                cat_name = cd.get("displayProperties", {}).get("name", "")
        categories.append({
            "hash": ch,
            "name": cat_name,
            "indexes": cat.get("socketIndexes", []),
        })

    # Socket entries
    entries = []
    for entry in sockets.get("socketEntries", []):
        idx = len(entries)
        rp = entry.get("reusablePlugItems", [])
        rpsh = entry.get("reusablePlugSetHash", 0)
        rand_psh = entry.get("randomizedPlugSetHash", 0)

        plug_names = []
        # inline reusable items
        for pl in rp:
            ph = pl.get("plugItemHash", 0)
            if ph:
                plug_names.append(resolve_perk_name(cur, ph))

        # randomized plug set
        if rand_psh:
            cur.execute("SELECT json FROM DestinyPlugSetDefinition WHERE id=?", (to_signed(rand_psh),))
            ps_row = cur.fetchone()
            if ps_row:
                ps_data = load_json(ps_row[0])
                if ps_data:
                    for pl in ps_data.get("reusablePlugItems", []):
                        ph = pl.get("plugItemHash", 0)
                        if ph:
                            plug_names.append(resolve_perk_name(cur, ph))

        entries.append({
            "index": idx,
            "reusable_count": len(rp),
            "has_reusable_set": bool(rpsh),
            "has_randomized_set": bool(rand_psh),
            "randomized_set_hash": rand_psh,
            "plug_names": plug_names,
        })

    return {
        "name": display.get("name", ""),
        "type": data.get("itemTypeDisplayName", ""),
        "id": weapon_id,
        "hash": to_unsigned(weapon_id),
        "categories": categories,
        "sockets": entries,
    }
