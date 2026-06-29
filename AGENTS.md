# 命运2 离线数据库查询规范

## 1. 数据库生命周期管理

### 1.1 前置检查
在执行任何数据库查询任务前，**必须**先验证数据库状态：

```bash
python scripts/download_db.py --check
```

- 如果返回码为 0（数据库已是最新）→ 继续查询
- 如果返回码非 0（数据库不存在或需要更新）→ 先运行 `python scripts/download_db.py` 下载/更新，再执行查询

### 1.2 首次设置
1. 前往 https://www.bungie.net/en/Application 注册应用获取 API Key
2. 设置环境变量：`set BUNGIE_API_KEY=你的密钥`（Windows）
3. 运行 `python scripts/download_db.py` 下载数据库（约 340MB）

### 1.3 强制更新
需要最新数据时：`python scripts/download_db.py --force`

## 2. 数据库文件

| 文件 | 说明 |
|---|---|
| `destiny2_zh-chs.sqlite3` | 简体中文离线 SQLite 数据库（不纳入版本管理） |
| `.db_version` | 版本缓存文件，记录当前数据库版本 |
| `scripts/download_db.py` | 数据库下载/更新脚本 |

### 2.1 关键表结构

- `DestinyInventoryItemDefinition`：装备、道具、Perk 插件定义（主表）
  - `id`（有符号 INT32，对应 JSON 中的无符号 hash 转换而来）
  - `json`（TEXT，完整 JSON 定义）
- `DestinySandboxPerkDefinition`：沙盒 Perk 详细描述
  - `id`（有符号 INT32）
  - `json`（TEXT）
- `DestinySocketCategoryDefinition`：插槽分类定义
- `DestinyPlugSetDefinition`：Perk 池定义（包含 reusablePlugItems）

### 2.2 Perk 查询链路

```
DestinyInventoryItemDefinition（武器 JSON）
  → sockets.socketEntries[]
    → reusablePlugItems[].plugItemHash / randomizedPlugSetHash / reusablePlugSetHash
      → DestinyInventoryItemDefinition（插件条目，name = Perk 名）
        → perks[].perkHash
          → DestinySandboxPerkDefinition（Perk 详细描述）
```

## 3. 查询结果输出规范

### 3.1 格式要求
所有数据库查询结果**必须**输出为自包含的 HTML 文件。HTML 文件应当：
- 单一文件，无外部依赖（CSS/JS 全部内联或通过 CDN 引用）
- 中文编码正确（UTF-8）
- 包含完整的查询说明和结果表格
- 文件命名：按查询内容命名，存于项目根目录或 `results/` 目录

### 3.2 HTML 模板要求
- 使用 Pico CSS（通过 CDN）作为基础样式
- 查询结果放在 `<table>` 中
- 页面包含标题、查询时间、查询说明
- 大文本使用 `word-break: break-all` 避免溢出

### 3.3 查询代码规范
- 查询脚本使用 `uv run python` 执行
- 临时查询脚本存于项目根目录，以 `query_` 为前缀，查询完成后**必须**清理删除
- 复用查询脚本存于 `scripts/` 目录
- 优先使用 Python 标准库 `sqlite3` + `json`，不引入额外依赖

## 4. 数据库编码注意事项

- `id` 列存储的是有符号 32 位整数。JSON 中的 hash 为无符号表示，查询时需转换
- ID 转换方法：Python 中 `hash_value if hash_value < 2**31 else hash_value - 2**32`
- 或直接使用带符号整数字面量（如 `-1902153673`）
