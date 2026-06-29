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

## 2. 查询工作流规范

- 任何内容都从数据表中获取，**绝对禁止**凭空捏造信息。
- 查询数据时确保查找所有需要查找的数据，不允许跳过，漏查。

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
- 通用查询脚本放在scripts/目录下。
- 临时查询脚本统一放在scripts/temp/目录下，查询完成后**必须**清理删除。
- 每次执行完查询任务，将查询任务中使用的查询方法提取出来，增加/覆盖/改进现有的通用查询脚本。
- 写临时查询脚本时，优先使用通用查询脚本。
- 查询脚本使用 `uv run python` 执行
- 优先使用 Python 标准库 `sqlite3` + `json`，不引入额外依赖

### 3.4 通用查询工具
现有通用工具位于 `scripts/db.py`，提供：

| 函数 | 功能 |
|---|---|
| `get_conn()` | 获取数据库连接 |
| `load_json(val)` | 解析 BLOB/TEXT 为 JSON |
| `search_perk(cur, keyword)` | 按关键词搜索 Perk（名称+描述） |
| `search_items(cur, keyword)` | 按关键词搜索物品 |
| `resolve_perk_name(cur, plug_hash)` | 从 plug hash 解析 Perk 名称 |
| `resolve_perk_with_description(cur, plug_hash)` | 解析 Perk 名称+效果描述 |
| `find_weapons_with_perks(cur, plug_hashes)` | 查找含指定 Perk 组合的武器 |
| `get_weapon_socket_analysis(cur, weapon_id)` | 分析武器所有插槽和 Perk 池 |
| `SLOT_TYPES` 字典 | 武器槽类型 hash → 名称映射 |
| `to_signed(hash)` / `to_unsigned(id)` | 有符号/无符号 ID 互转 |

## 4. 数据库编码注意事项

- `id` 列存储的是有符号 32 位整数。JSON 中的 hash 为无符号表示，查询时需转换
- ID 转换方法：Python 中 `hash_value if hash_value < 2**31 else hash_value - 2**32`
- 或直接使用带符号整数字面量（如 `-1902153673`）
