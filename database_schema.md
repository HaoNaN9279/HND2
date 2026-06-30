# Destiny2 数据库 Schema 文档

> **数据库**：`destiny2_zh-chs.sqlite3` · **83** 张表 · Bungie API Manifest 定义数据  

> 每表含 SQL 列 `id`（INTEGER 主键，对应 Bungie API hash）+ `json`（BLOB，存储完整 JSON 定义）。  
> 以下列出 JSON 内的所有字段及中文描述。字段含 `Hash` 后缀的引用其他定义表。  

## DestinyAchievementDefinition
**成就定义：游戏内成就/奖杯信息** · 113 行 · 主键 `id` · 7 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `acccumulatorThreshold` | Number | 累积阈值 |
| `platformIndex` | Number | 平台索引 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyActivityDefinition
**活动定义：副本、打击、突袭等所有活动的基础信息** · 4069 行 · 主键 `id` · 37 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `originalDisplayProperties` | Object{description, hasIcon, icon, iconHash, name} | 原始显示属性 |
| `releaseIcon` | String | 发布图标 |
| `releaseTime` | Number | 发布时间 |
| `completionUnlockHash` | Number | 完成解锁条件hash |
| `activityLightLevel` | Number | 活动光等级 |
| `destinationHash` | Number | 目的地hash引用 |
| `placeHash` | Number | 地点hash引用 |
| `activityTypeHash` | Number | 活动类型hash引用 |
| `tier` | Number | 难度等级 |
| `rewards` | Array[2]{rewardItems, rewardText} | 奖励配置数组（含奖励物品/文字） |
| `modifiers` | Array[1]{activityModifierHash} | Modifier数组（含activityModifierHash） |
| `isPlaylist` | Boolean | 是否为播放列表 |
| `challenges` | Array[?] | 挑战列表 |
| `optionalUnlockStrings` | Array[1]{displayString} | 可选解锁字符串 |
| `inheritFromFreeRoam` | Boolean | 继承自由探索属性 |
| `suppressOtherRewards` | Boolean | 抑制其他奖励 |
| `playlistItems` | Array[31]{activityHash, activityModeHashes, activityModeTypes, dire... | 播放列表条目 |
| `matchmaking` | Object{isMatchmade, maxParty, maxPlayers, minParty, requiresGuardia... | 匹配参数 |
| `directActivityModeHash` | Number | 直接活动模式hash |
| `directActivityModeType` | Number | 直接活动模式类型 |
| `activityModeHashes` | Array[Number] | 活动模式hash数组 |
| `activityModeTypes` | Array[Number] | 活动模式类型数组 |
| `isPvP` | Boolean | 是否为PvP |
| `insertionPoints` | Array[?] | 重生点列表 |
| `activityLocationMappings` | Array[1]{activationSource, activityHash, locationHash} | 活动位置映射 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `pgcrImage` | String | 战后报告背景图 |
| `traitHashes` | Array[?] | 特性hash数组 |
| `selectableSkullCollectionHashes` | Array[?] | 可选Modifier集合hash数组 |
| `selectableSkullCollections` | Array[?] | 可选Modifier集合数据 |
| `curatorBlockDefinition` | Object{quickplaySortPriority, quickplaySortToFront} | 策划排序配置 |
| `requirements` | Object{fireteamRequirementLabels, leaderRequirementLabels} | 参与要求 |
| `activityFamilyHashes` | Array[Number] | 活动系列hash数组 |

## DestinyActivityDifficultyTierCollectionDefinition
**活动难度等级集合** · 23 行 · 主键 `id` · 5 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `difficultyTiers` | Array[12]{activityLevel, displayProperties, fixedActivitySkulls, ma... | 难度等级数组（光等/显示属性/头骨修饰等） |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyActivityFamilyDefinition
**活动系列定义** · 266 行 · 主键 `id` · 8 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `traits` | Array[Number] | 特性数组 |
| `disabledSkullCategoryHashes` | Array[?] | 禁用头骨分类hash数组 |
| `disabledSkullSubcategoryHashes` | Array[?] | 禁用头骨子类hash数组 |
| `fixedSkullSubcategoryHashes` | Array[?] | 固定头骨子类hash数组 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyActivityGraphDefinition
**活动图谱定义：活动节点及连线关系** · 49 行 · 主键 `id` · 12 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `nodes` | Array[1]{activities, featuringStates, nodeId, overrideDisplay, posi... | 图谱节点数组（活动/状态/位置/UI样式） |
| `artElements` | Array[?] | 美术元素数组 |
| `connections` | Array[?] | 节点连线数组 |
| `displayObjectives` | Array[?] | 显示目标数组 |
| `displayProgressions` | Array[?] | 显示进度数组 |
| `linkedGraphs` | Array[8]{description, linkedGraphId, linkedGraphs, name, overview} | 关联子图谱数组（描述/名称/概览） |
| `uiScreen` | Number | UI界面类型枚举 |
| `ignoreForMilestones` | Boolean | 是否忽略里程碑统计 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyActivityInteractableDefinition
**活动可交互对象定义** · 141 行 · 主键 `id` · 5 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `entries` | Array[1]{activityHash} | 条目数组 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyActivityLoadoutRestrictionDefinition
**活动配装限制** · 14 行 · 主键 `id` · 6 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `restrictedItemFilterHash` | Number | restricted/item/filterhash引用 |
| `restrictedEquipmentSlotHashes` | Array[Number] | restricted/equipment/slothash数组（引用列表） |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyActivityModeDefinition
**活动模式定义（PVE/PVP/Gambit等）** · 75 行 · 主键 `id` · 16 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `pgcrImage` | String | 战后报告背景图 |
| `modeType` | Number | 类型枚举 |
| `activityModeCategory` | Number | activity/mode/category数值 |
| `isTeamBased` | Boolean | 是否teambased |
| `tier` | Number | 难度等级 |
| `isAggregateMode` | Boolean | 是否aggregatemode |
| `friendlyName` | String | 名称文本 |
| `supportsFeedFiltering` | Boolean | 布尔标记 |
| `display` | Boolean | 布尔标记 |
| `order` | Number | 排序号 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `parentHashes` | Array[Number] | parenthash数组（引用列表） |

## DestinyActivityModifierDefinition
**活动Modifier定义：词缀/修正效果** · 351 行 · 主键 `id` · 7 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, iconSequences, name} | 显示属性（名称/描述/图标） |
| `displayInNavMode` | Boolean | 布尔标记 |
| `displayInActivitySelection` | Boolean | 布尔标记 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyActivitySelectableSkullCollectionDefinition
**可选Modifier集合** · 279 行 · 主键 `id` · 8 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `skullSubcategoryHashes` | Array[Number] | skull/subcategoryhash数组（引用列表） |
| `selectableActivitySkulls` | Array[15]{activitySkull, debugSelectableSkull, isEmptySkull, requir... | selectable/activity/skull数组（15{activitySkull, debugSelectableSkull, isEmptySkull, requiredTraitExistence}） |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `selectionType` | Object{refreshTimeMinutes, refreshTimeOffsetMinutes, selectionCount} | selection/type对象（refreshTimeMinutes, refreshTimeOffsetMinutes, selectionCount） |

## DestinyActivitySelectableSkullExclusionGroupDefinition
**Modifier互斥组** · 12 行 · 主键 `id` · 4 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyActivitySkullCategoryDefinition
**Modifier分类定义** · 13 行 · 主键 `id` · 5 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, iconSequences, name} | 显示属性（名称/描述/图标） |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyActivitySkullCollectionDefinition
**Modifier集合定义** · 621 行 · 主键 `id` · 5 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `skulls` | Array[1]{activityModifierConnotation, activityModifierDisplayCatego... | Modifier数据数组 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyActivitySkullSubcategoryDefinition
**Modifier子分类定义** · 95 行 · 主键 `id` · 7 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, iconSequences, name} | 显示属性（名称/描述/图标） |
| `parentSkullCategoryHash` | Number | 父级Modifier分类hash |
| `availabilityTierRank` | Number | 可用等级排序 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyActivityTypeDefinition
**活动类型定义** · 83 行 · 主键 `id` · 5 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyArtifactDefinition
**神器定义：赛季神器** · 1 行 · 主键 `id` · 6 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `tiers` | Array[5]{displayTitle, items, minimumUnlockPointsUsedRequirement, t... | 层级数组（含标题/解锁/要求） |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyBondDefinition
**职业债券定义（已废弃）** · 4 行 · 主键 `id` · 7 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `providedUnlockHash` | Number | 提供的解锁条件hash |
| `providedUnlockValueHash` | Number | 提供的解锁值hash |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyBreakerTypeDefinition
**破盾类型定义：元素护盾类型及克制** · 3 行 · 主键 `id` · 7 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `enumValue` | Number | 枚举值 |
| `unlockHash` | Number | 解锁条件hash |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyChecklistDefinition
**检查清单定义：可追踪的收集/成就清单** · 22 行 · 主键 `id` · 8 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `viewActionString` | String | 查看动作 |
| `scope` | Number | 作用范围枚举 |
| `entries` | Array[10]{displayProperties, hash, scope} | 条目数组 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyClassDefinition
**职业定义：猎人/泰坦/术士** · 3 行 · 主键 `id` · 8 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `classType` | Number | 职业类型 |
| `displayProperties` | Object{hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `genderedClassNames` | Object{Female, Male} | 按性别职业名（男/女） |
| `genderedClassNamesByGenderHash` | Object{2204441813, 3111576190} | 按性别hash映射职业名 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyCollectibleDefinition
**收藏品定义：可收集物品/外观** · 12255 行 · 主键 `id` · 15 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, highResIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `scope` | Number | 作用范围枚举 |
| `sourceString` | String | 来源描述文本 |
| `sourceHash` | Number | 来源hash引用 |
| `itemHash` | Number | 关联物品hash引用（→DestinyInventoryItemDefinition） |
| `acquisitionInfo` | Object{acquireMaterialRequirementHash, runOnlyAcquisitionRewardSite} | 获取信息对象（含材料需求/奖励站点等） |
| `stateInfo` | Object{requirements} | 状态信息对象（含需求） |
| `presentationNodeType` | Number | 展示节点类型 |
| `traitIds` | Array[?] | 特性ID数组 |
| `traitHashes` | Array[?] | 特性hash数组 |
| `parentNodeHashes` | Array[Number] | 父节点hash数组 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyDamageTypeDefinition
**伤害类型定义：动能/电弧/炽热/虚空/冰影等** · 7 行 · 主键 `id` · 9 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `showIcon` | Boolean | 是否显示图标 |
| `enumValue` | Number | 枚举值 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `transparentIconPath` | String | 透明图标路径 |
| `color` | Object{alpha, blue, green, red} | 颜色(RGBA) |

## DestinyDestinationDefinition
**目的地定义：游戏中各目的地/星球** · 142 行 · 主键 `id` · 10 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `placeHash` | Number | 地点hash引用 |
| `defaultFreeroamActivityHash` | Number | 默认自由探索活动hash |
| `activityGraphEntries` | Array[1]{activityGraphHash} | 活动图谱入口列表 |
| `bubbleSettings` | Array[14]{displayProperties} | 气泡设置列表 |
| `bubbles` | Array[14]{displayProperties, hash} | 气泡列表 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyEnergyTypeDefinition
**能量类型定义：武器元素能量类型** · 7 行 · 主键 `id` · 10 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `showIcon` | Boolean | 是否显示图标 |
| `enumValue` | Number | 枚举值 |
| `costStatHash` | Number | 消耗属性hash |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `capacityStatHash` | Number | 容量属性hash |
| `transparentIconPath` | String | 透明图标路径 |

## DestinyEquipableItemSetDefinition
**可装备套装定义** · 56 行 · 主键 `id` · 7 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `setItems` | Array[Number] | 套装物品hash列表 |
| `setPerks` | Array[2]{requiredSetCount, sandboxPerkHash} | 套装Perk列表（含所需数量/sandboxPerkHash） |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyEquipmentSlotDefinition
**装备插槽定义** · 18 行 · 主键 `id` · 9 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `equipmentCategoryHash` | Number | 装备分类hash |
| `bucketTypeHash` | Number | 背包分类hash |
| `applyCustomArtDyes` | Boolean | 是否应用自定义涂装 |
| `artDyeChannels` | Array[3]{artDyeChannelHash} | 涂装通道列表 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyEventCardDefinition
**活动通行证定义** · 3 行 · 主键 `id` · 20 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `ownershipUnlockFlagHash` | Number | 拥有权解锁标记hash |
| `triumphsPresentationNodeHash` | Number | 成就展示节点hash |
| `sealPresentationNodeHash` | Number | 印章展示节点hash |
| `eventCardCurrencyList` | Array[Number] | 活动通行证货币hash列表 |
| `ticketCurrencyItemHash` | Number | 门票货币物品hash |
| `ticketVendorHash` | Number | 门票商人hash |
| `ticketVendorCategoryHash` | Number | 门票商人分类hash |
| `endTime` | String | 结束时间 |
| `endTimeOverrideUnlockValueHash` | Number | 结束时间覆盖解锁值hash |
| `uiThemeHash` | Number | UI主题hash |
| `rewardProgressionHash` | Number | 奖励进度hash |
| `rewardProgressionHashList` | Array[Number] | 奖励进度hash列表 |
| `weeklyChallengesPresentationNodeHash` | Number | 每周挑战展示节点hash |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `color` | Object{alpha, blue, green, red} | 颜色(RGBA) |
| `images` | Object{themeBackgroundImagePath} | 图片资源（背景图/图标路径） |

## DestinyFactionDefinition
**阵营定义** · 82 行 · 主键 `id` · 9 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `progressionHash` | Number | 进度系统hash |
| `rewardItemHash` | Number | 奖励物品hash |
| `rewardVendorHash` | Number | 奖励商人hash |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `vendors` | Array[1]{backgroundImagePath, destinationHash, vendorHash} | 关联商人列表 |

## DestinyFireteamFinderActivityGraphDefinition
**火力队查找器活动图谱** · 563 行 · 主键 `id` · 18 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `isPlayerElectedDifficultyNode` | Boolean | 是否玩家选择难度节点 |
| `parentHash` | Number | 父节点hash |
| `children` | Array[?] | 子节点hash列表 |
| `selfAndAllDescendantHashes` | Array[Number] | 自身及全部后裔hash列表 |
| `relatedActivitySetHashes` | Array[?] | 关联活动集hash列表 |
| `relatedDirectorNodes` | Array[1]{activityGraphHash} | 关联指引节点列表 |
| `relatedInteractableActivities` | Array[1]{activityInteractableElementIndex, activityInteractableHash} | 关联可交互活动列表 |
| `relatedLocationHashes` | Array[?] | 关联地点hash列表 |
| `sortMatchmadeActivitiesToFront` | Boolean | 匹配活动排序靠前 |
| `enabledOnTreeTypesListEnum` | Array[Number] | 启用树类型枚举列表 |
| `activityTreeChildSortMode` | Number | 活动树子节点排序模式 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `specificActivitySetHash` | Number | 特定活动集hash |
| `relatedActivityHashes` | Array[?] | 关联活动hash列表 |

## DestinyFireteamFinderActivitySetDefinition
**火力队活动集合** · 563 行 · 主键 `id` · 9 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `maximumPartySize` | Number | 最大队伍人数 |
| `optionHashes` | Array[Number] | 选项hash列表 |
| `labelHashes` | Array[Number] | 标签hash列表 |
| `activityGraphHashes` | Array[?] | 活动图谱hash列表 |
| `activityHashes` | Array[Number] | 活动hash列表 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyFireteamFinderConstantsDefinition
**火力队查找器常量** · 1 行 · 主键 `id` · 10 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `fireteamFinderActivityGraphRootCategoryHashes` | Array[Number] | 活动图谱根分类hash列表 |
| `allFireteamFinderActivityHashes` | Array[Number] | 全部火力队活动hash列表 |
| `guardianOathDisplayProperties` | Object{description, hasIcon, iconHash, name} | 守护者誓言显示属性 |
| `guardianOathTenets` | Array[4]{description, hasIcon, iconHash, name} | 守护者誓言信条列表 |
| `guardianOathConfirmedUnlockFlagHash` | Number | 守护者誓言确认解锁标记hash |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyFireteamFinderLabelDefinition
**火力队查找器标签** · 228 行 · 主键 `id` · 8 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `descendingSortPriority` | Number | 降序排序优先级 |
| `groupHash` | Number | 所属组hash引用 |
| `allowInFields` | Number | 允许出现字段位掩码 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyFireteamFinderLabelGroupDefinition
**火力队查找器标签组** · 8 行 · 主键 `id` · 6 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `descendingSortPriority` | Number | 降序排序优先级 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyFireteamFinderOptionDefinition
**火力队查找器选项** · 10 行 · 主键 `id` · 13 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `descendingSortPriority` | Number | 降序排序优先级 |
| `groupHash` | Number | 所属组hash引用 |
| `codeOptionType` | Number | 类型枚举 |
| `availability` | Number | availability数值 |
| `visibility` | Number | 可见性枚举 |
| `uiDisplayStyle` | String | ui/display/style文本 |
| `searcherSettings` | Object{control, searchFilterType} | searcher/setting对象（control, searchFilterType） |
| `values` | Object{displayFormatType, optionalFormatString, optionalNull, type,... | value对象（displayFormatType, optionalFormatString, optionalNull, type, valueDefinitions） |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyFireteamFinderOptionGroupDefinition
**火力队查找器选项组** · 8 行 · 主键 `id` · 6 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `descendingSortPriority` | Number | 降序排序优先级 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyGenderDefinition
**性别定义** · 2 行 · 主键 `id` · 6 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `genderType` | Number | 类型枚举 |
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyGlobalConstantsDefinition
**全局常量定义** · 1 行 · 主键 `id` · 27 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `pathfinderConstants` | Object{allPathfinderRootNodeHashes, blacklisted, hash, index, pathf... | pathfinder/constant对象（allPathfinderRootNodeHashes, blacklisted, hash, index, pathfinderTopology, pathfinderTreeTiers, redacted, thePaleHeartPathfinderRootNodeHash） |
| `collectionsRootNodeHash` | Number | collections/root/nodehash引用 |
| `collectionBadgesRootNodeHash` | Number | collection/badges/root/nodehash引用 |
| `activeTriumphsRootNodeHash` | Number | active/triumphs/root/nodehash引用 |
| `activeSealsRootNodeHash` | Number | active/seals/root/nodehash引用 |
| `legacyTriumphsRootNodeHash` | Number | legacy/triumphs/root/nodehash引用 |
| `legacySealsRootNodeHash` | Number | legacy/seals/root/nodehash引用 |
| `medalsRootNodeHash` | Number | medals/root/nodehash引用 |
| `exoticCatalystsRootNodeHash` | Number | exotic/catalysts/root/nodehash引用 |
| `loreRootNodeHash` | Number | lore/root/nodehash引用 |
| `metricsRootNodeHash` | Number | metrics/root/nodehash引用 |
| `craftingRootNodeHash` | Number | crafting/root/nodehash引用 |
| `guardianRanksRootNodeHash` | Number | guardian/ranks/root/nodehash引用 |
| `seasonalHubEventCardHash` | Number | seasonal/hub/event/cardhash引用 |
| `destinyRewardPassRankSealImages` | Object{rewardPassRankSealImagePath, rewardPassRankSealPremiumImageP... | destiny/reward/pass/rank/seal/image对象（rewardPassRankSealImagePath, rewardPassRankSealPremiumImagePath, rewardPassRankSealPremiumPrestigeImagePath, rewardPassRankSealPrestigeImagePath） |
| `destinySeasonalHubRankIconImages` | Object{seasonalHubRankIconActive, seasonalHubRankIconEarning, seaso... | destiny/seasonal/hub/rank/icon/image对象（seasonalHubRankIconActive, seasonalHubRankIconEarning, seasonalHubRankIconUnearned） |
| `armorArchetypePlugSetHash` | Number | armor/archetype/plug/sethash引用 |
| `featuredItemsListHash` | Number | featured/items/listhash引用 |
| `portalActivityGraphRootNodesWithIcons` | Object{1204273545, 1246572235, 2042336100, 2699534027, 4038998327} | portal/activity/graph/root/nodes/with/icon对象（1204273545, 1246572235, 2042336100, 2699534027, 4038998327） |
| `orderRewardsUnlockValueHashesToRewardItemHashes` | Object{207387605, 2299106475, 3745011343, 3953935840, 994595365} | order/rewards/unlock/value/hashes/to/reward/itemhash数组（引用列表） |
| `questItemTraitToFeaturedQuestImagePath` | Object{1056186694, 370766376, 520867389, 904453863} | quest/item/trait/to/featured/quest/image/path对象（1056186694, 370766376, 520867389, 904453863） |
| `currentReleaseTraitHash` | Number | current/release/traithash引用 |
| `vanguardAlertsFireteamFinderActivityGraphRootNodeHash` | Number | vanguard/alerts/fireteam/finder/activity/graph/root/nodehash引用 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyGuardianRankConstantsDefinition
**守护者等级常量** · 1 行 · 主键 `id` · 9 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, iconSequences, name} | 显示属性（名称/描述/图标） |
| `rankCount` | Number | 限制/计数 |
| `guardianRankHashes` | Array[Number] | guardian/rankhash数组（引用列表） |
| `rootNodeHash` | Number | root/nodehash引用 |
| `iconBackgrounds` | Object{backgroundEmptyBlueGradientBorderedImagePath, backgroundEmpt... | icon/background对象（backgroundEmptyBlueGradientBorderedImagePath, backgroundEmptyBorderedImagePath, backgroundFilledBlueBorderedImagePath, backgroundFilledBlueGradientBorderedImagePath, backgroundFilledBlueLowAlphaImagePath, backgroundFilledBlueMediumAlphaImagePath, backgroundFilledGrayHeavyAlphaBorderedImagePath, backgroundFilledGrayMediumAlphaBorderedImagePath, backgroundFilledWhiteImagePath, backgroundFilledWhiteMediumAlphaImagePath, backgroundPlateBlackAlphaImagePath, backgroundPlateBlackImagePath） |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyGuardianRankDefinition
**守护者等级定义** · 11 行 · 主键 `id` · 10 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `rankNumber` | Number | 等级/优先级 |
| `presentationNodeHash` | Number | presentation/nodehash引用 |
| `foregroundImagePath` | String | 资源路径 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `overlayImagePath` | String | 资源路径 |
| `overlayMaskImagePath` | String | 资源路径 |

## DestinyHistoricalStatsDefinition
**历史统计数据定义** · 405 行 · 主键 `key` · 13 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `statId` | String | 唯一标识符 |
| `hash` | Number | 全局唯一标识hash |
| `hashSigned` | Number | hash值 |
| `group` | Number | group数值 |
| `periodTypes` | Array[Number] | period/type数组（Number） |
| `modes` | Array[Number] | mode数组（Number） |
| `category` | Number | category数值 |
| `statName` | String | 名称文本 |
| `unitType` | Number | 类型枚举 |
| `unitLabel` | String | 标签文本 |
| `weight` | Number | 权重值 |
| `statDescription` | String | 描述文本 |
| `bestActivityIdPropertyName` | String | 名称文本 |

## DestinyIconDefinition
**图标定义** · 26645 行 · 主键 `id` · 9 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `foreground` | String | foreground文本 |
| `background` | String | background文本 |
| `secondaryBackground` | String | secondary/background文本 |
| `specialBackground` | String | special/background文本 |
| `highResForeground` | String | high/res/foreground文本 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyInventoryBucketDefinition
**物品栏分类桶定义** · 60 行 · 主键 `id` · 13 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `scope` | Number | 作用范围枚举 |
| `category` | Number | category数值 |
| `bucketOrder` | Number | 排序值 |
| `itemCount` | Number | 限制/计数 |
| `location` | Number | location数值 |
| `hasTransferDestination` | Boolean | 是否有transferdestination |
| `enabled` | Boolean | 是否启用 |
| `fifo` | Boolean | 布尔标记 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyInventoryItemConstantsDefinition
**物品常量定义** · 1 行 · 主键 `id` · 20 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `gearTierOverlayImagePaths` | Array[String] | gear/tier/overlay/image/path数组（String） |
| `watermarkDropShadowPath` | String | 资源路径 |
| `craftedBackgroundPath` | String | 资源路径 |
| `featuredItemFlagPath` | String | 资源路径 |
| `masterworkOverlayPath` | String | 资源路径 |
| `masterworkExoticOverlayPath` | String | 资源路径 |
| `masterworkBorderedOverlayPath` | String | 资源路径 |
| `masterworkExoticBorderedOverlayPath` | String | 资源路径 |
| `craftedOverlayPath` | String | 资源路径 |
| `enhancedItemOverlayPath` | String | 资源路径 |
| `holofoilBackgroundOverlayPath` | String | 资源路径 |
| `holofoil900BackgroundOverlayPath` | String | 资源路径 |
| `holofoil900AnimatedBackgroundOverlayPath` | String | 资源路径 |
| `universalOrnamentBackgroundOverlayPath` | String | 资源路径 |
| `universalOrnamentLegendaryBackgroundOverlayPath` | String | 资源路径 |
| `universalOrnamentExoticBackgroundOverlayPath` | String | 资源路径 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyInventoryItemDefinition
**物品定义：所有可装备/收集/使用物品（最大表，含武器护甲模组等）** · 38894 行 · 主键 `id` · 54 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `tooltipNotifications` | Array[?] | 提示通知数组 |
| `isFeaturedItem` | Boolean | 是否为推荐物品 |
| `isHolofoil` | Boolean | 是否全息 |
| `isAdept` | Boolean | 是否专家/宗师版 |
| `itemTypeDisplayName` | String | 物品类型显示名 |
| `flavorText` | String | 背景文字 |
| `uiItemDisplayStyle` | String | UI显示样式 |
| `itemTypeAndTierDisplayName` | String | 物品类型+品质显示名 |
| `displaySource` | String | 来源显示文本 |
| `inventory` | Object{bucketTypeHash, expirationTooltip, expiredInActivityMessage,... | 库存属性 |
| `acquireRewardSiteHash` | Number | 获取奖励站点hash |
| `acquireUnlockHash` | Number | 获取解锁hash |
| `investmentStats` | Array[16]{isConditionallyActive, statTypeHash, value} | 投资属性数组 |
| `perks` | Array[?] | Perk数组 |
| `allowActions` | Boolean | 是否允许动作 |
| `doesPostmasterPullHaveSideEffects` | Boolean | 邮政官取回是否有副作用 |
| `nonTransferrable` | Boolean | 是否不可转移 |
| `itemCategoryHashes` | Array[?] | 物品分类hash数组 |
| `specialItemType` | Number | 特殊物品类型 |
| `itemType` | Number | 物品类型 |
| `itemSubType` | Number | 物品子类型 |
| `classType` | Number | 职业类型 |
| `breakerType` | Number | 破盾类型 |
| `equippable` | Boolean | 是否可装备 |
| `defaultDamageType` | Number | 默认伤害类型 |
| `isWrapper` | Boolean | 是否包装物品 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `backgroundColor` | Object{alpha, blue, colorHash, green, red} | 背景颜色(RGBA) |
| `action` | Object{actionTypeLabel, consumeEntireStack, deleteOnAction, isPosit... | 使用动作 |
| `stats` | Object{disablePrimaryStatDisplay, hasDisplayableStats, primaryBaseS... | 属性数值 |
| `quality` | Object{currentVersion, displayVersionWatermarkIcons, infusionCatego... | quality对象（currentVersion, displayVersionWatermarkIcons, infusionCategoryHash, infusionCategoryHashes, infusionCategoryName, itemLevels, progressionLevelRequirementHash, qualityLevel, versions） |
| `traitIds` | Array[String] | 特性ID数组 |
| `traitHashes` | Array[Number] | 特性hash数组 |
| `iconWatermark` | String | 水印图标路径 |
| `iconWatermarkShelved` | String | 搁置水印图标 |
| `iconWatermarkFeatured` | String | 资源路径 |
| `screenshot` | String | 截图路径 |
| `equippingBlock` | Object{ammoType, attributes, displayStrings, equipableItemSetHash, ... | 装备槽位信息（含槽位hash/美术通道等） |
| `translationBlock` | Object{arrangements, customDyes, defaultDyes, hasGeometry, lockedDy... | translation/block对象（arrangements, customDyes, defaultDyes, hasGeometry, lockedDyes, weaponPatternHash） |
| `preview` | Object{previewActionString, previewVendorHash, screenStyle} | 预览（描述/图片/链接） |
| `plug` | Object{actionRewardItemOverrideHash, actionRewardSiteHash, alternat... | plug对象（actionRewardItemOverrideHash, actionRewardSiteHash, alternatePlugStyle, alternateUiPlugLabel, applyStatsToSocketOwnerItem, enabledMaterialRequirementHash, enabledRules, insertionMaterialRequirementHash, insertionRules, isDummyPlug, onActionRecreateSelf, parentItemOverride） |
| `sockets` | Object{detail, intrinsicSockets, socketCategories, socketEntries} | 插槽信息（含全部socket配置） |
| `collectibleHash` | Number | collectiblehash引用 |
| `tooltipStyle` | String | tooltip/style文本 |
| `sack` | Object{detailAction, openAction, openOnAcquire, resolvedBitVectorUn... | sack对象（detailAction, openAction, openOnAcquire, resolvedBitVectorUnlockValueHash, resolvedItemCountUnlockValueHash, rewardItemListHash, rollStateUnlockValueHash, seedUnlockValueHash, selectItemCount, vendorSackType） |
| `damageTypeHashes` | Array[Number] | 伤害类型hash数组 |
| `damageTypes` | Array[Number] | 伤害类型数组 |
| `defaultDamageTypeHash` | Number | default/damage/typehash引用 |
| `loreHash` | Number | lorehash引用 |
| `secondaryIcon` | String | 二级图标路径 |

## DestinyItemCategoryDefinition
**物品分类定义** · 130 行 · 主键 `id` · 18 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `visible` | Boolean | 是否可见 |
| `deprecated` | Boolean | 是否已弃用 |
| `shortTitle` | String | 短标题 |
| `itemTypeRegex` | String | 物品类型匹配正则 |
| `grantDestinyBreakerType` | Number | 授予的破防类型 |
| `grantDestinyItemType` | Number | 授予的物品类型 |
| `grantDestinySubType` | Number | 授予的子类型 |
| `grantDestinyClass` | Number | 授予的职业类型 |
| `groupedCategoryHashes` | Array[?] | 分组分类hash数组 |
| `isPlug` | Boolean | 是否为插件 |
| `parentCategoryHashes` | Array[?] | 父分类hash数组 |
| `groupCategoryOnly` | Boolean | 是否仅分组用途 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `plugCategoryIdentifier` | String | 插件分类标识符 |

## DestinyItemFilterDefinition
**物品筛选定义** · 14 行 · 主键 `id` · 5 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `allowedItems` | Array[?] | 允许物品hash数组 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyItemTierTypeDefinition
**物品品质定义：传说/异域/稀有等** · 7 行 · 主键 `id` · 6 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `infusionProcess` | Object{baseQualityTransferRatio, minimumQualityIncrement} | 灌注参数（基础品质转移比/最小品质增量） |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyLoadoutColorDefinition
**配装颜色定义** · 22 行 · 主键 `id` · 5 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `colorImagePath` | String | 颜色图片路径 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyLoadoutConstantsDefinition
**配装常量定义** · 1 行 · 主键 `id` · 13 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `whiteIconImagePath` | String | 白色图标路径 |
| `blackIconImagePath` | String | 黑色图标路径 |
| `loadoutCountPerCharacter` | Number | 每角色配装数量 |
| `loadoutPreviewFilterOutSocketCategoryHashes` | Array[Number] | 预览排除插槽分类hash数组 |
| `loadoutPreviewFilterOutSocketTypeHashes` | Array[Number] | 预览排除插槽类型hash数组 |
| `loadoutNameHashes` | Array[Number] | 配装名称hash数组 |
| `loadoutIconHashes` | Array[Number] | 配装图标hash数组 |
| `loadoutColorHashes` | Array[Number] | 配装颜色hash数组 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyLoadoutIconDefinition
**配装图标定义** · 21 行 · 主键 `id` · 5 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `iconImagePath` | String | 图标图片路径 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyLoadoutNameDefinition
**配装名称定义** · 22 行 · 主键 `id` · 5 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `name` | String | 名称文本 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyLocationDefinition
**地点/区域定义** · 1228 行 · 主键 `id` · 6 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `vendorHash` | Number | 关联商人hash |
| `locationReleases` | Array[1]{activityBubbleName, activityGraphHash, activityGraphNodeHa... | 地点发布信息（气泡/图/节点/目的hash） |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyLoreDefinition
**背景故事定义** · 3514 行 · 主键 `id` · 6 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `subtitle` | String | 副标题 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyMaterialRequirementSetDefinition
**材料需求集定义** · 332 行 · 主键 `id` · 5 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `materials` | Array[1]{count, countIsConstant, deleteOnAction, hasVirtualStackSiz... | 材料需求数组（数量/hash/消耗标记等） |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyMedalTierDefinition
**奖牌等级定义** · 7 行 · 主键 `id` · 6 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `tierName` | String | 等级名称 |
| `order` | Number | 排序号 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyMetricDefinition
**指标定义：追踪指标** · 402 行 · 主键 `id` · 11 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, iconSequences, name} | 显示属性（名称/描述/图标） |
| `trackingObjectiveHash` | Number | tracking/objectivehash引用 |
| `lowerValueIsBetter` | Boolean | 布尔标记 |
| `presentationNodeType` | Number | 展示节点类型 |
| `traitIds` | Array[?] | 特性ID数组 |
| `traitHashes` | Array[Number] | 特性hash数组 |
| `parentNodeHashes` | Array[Number] | 父节点hash数组 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyMilestoneDefinition
**里程碑定义：周常/日常任务** · 31 行 · 主键 `id` · 16 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `milestoneType` | Number | 里程碑类型枚举 |
| `recruitable` | Boolean | 是否可招募 |
| `showInExplorer` | Boolean | 是否在探索中显示 |
| `showInMilestones` | Boolean | 是否在里程碑中显示 |
| `explorePrioritizesActivityImage` | Boolean | 探索优先显示活动图 |
| `hasPredictableDates` | Boolean | 是否有可预测日期 |
| `quests` | Object{1276528297} | 任务列表 |
| `isInGameMilestone` | Boolean | 是否为游戏内里程碑 |
| `defaultOrder` | Number | 默认排序 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `activities` | Array[1]{activityGraphNodes, activityHash, challenges, phases} | 活动列表 |
| `image` | String | 资源路径 |

## DestinyObjectiveDefinition
**目标定义：任务/赏金的具体目标** · 11003 行 · 主键 `id` · 24 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, iconSequences, name} | 显示属性（名称/描述/图标） |
| `unlockValueHash` | Number | 解锁值hash |
| `completionValue` | Number | completion/value数值 |
| `scope` | Number | 作用范围枚举 |
| `locationHash` | Number | locationhash引用 |
| `allowNegativeValue` | Boolean | 是否允许负值 |
| `allowValueChangeWhenCompleted` | Boolean | 布尔标记 |
| `isCountingDownward` | Boolean | 是否倒数 |
| `valueStyle` | Number | 数值样式枚举 |
| `progressDescription` | String | 进度描述文本 |
| `perks` | Object{perkHash, style} | Perk数组 |
| `stats` | Object{style} | 属性数值 |
| `minimumVisibilityThreshold` | Number | 最低可见阈值 |
| `allowOvercompletion` | Boolean | 是否允许超额完成 |
| `showValueOnComplete` | Boolean | 完成时显示值 |
| `isDisplayOnlyObjective` | Boolean | 是否displayonlyobjective |
| `completedValueStyle` | Number | completed/value/style数值 |
| `inProgressValueStyle` | Number | 进行中数值样式枚举 |
| `uiLabel` | String | UI标签 |
| `uiStyle` | Number | ui/style数值 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyPlaceDefinition
**地点定义：宇宙层面地点** · 63 行 · 主键 `id` · 5 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyPlugSetDefinition
**插件集合定义：Perk池/模组池** · 5422 行 · 主键 `id` · 7 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `reusablePlugItems` | Array[12]{alternateWeight, craftingRequirements, currentlyCanRoll, ... | 可复用插件列表（含plugItemHash） |
| `isFakePlugSet` | Boolean | 是否fakeplugset |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyPowerCapDefinition
**能量上限定义** · 17 行 · 主键 `id` · 5 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `powerCap` | Number | power/cap数值 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyPresentationNodeDefinition
**展示节点定义：收藏/目录树形节点** · 2375 行 · 主键 `id` · 23 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, iconSequences, name} | 显示属性（名称/描述/图标） |
| `nodeType` | Number | 类型枚举 |
| `isSeasonal` | Boolean | 是否seasonal |
| `scope` | Number | 作用范围枚举 |
| `children` | Object{collectibles, craftables, metrics, presentationNodes, records} | 子节点hash列表 |
| `displayStyle` | Number | 显示样式枚举 |
| `screenStyle` | Number | screen/style数值 |
| `requirements` | Object{entitlementUnavailableMessage} | 参与要求 |
| `disableChildSubscreenNavigation` | Boolean | 布尔标记 |
| `categoryScoreUnlockValueHash` | Number | category/score/unlock/valuehash引用 |
| `maxCategoryRecordScore` | Number | 限制/计数 |
| `presentationNodeType` | Number | 展示节点类型 |
| `traitIds` | Array[?] | 特性ID数组 |
| `traitHashes` | Array[?] | 特性hash数组 |
| `parentNodeHashes` | Array[Number] | 父节点hash数组 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `objectiveHash` | Number | 目标hash引用 |
| `originalIcon` | String | 资源路径 |
| `rootViewIcon` | String | 资源路径 |
| `completionRecordHash` | Number | completion/recordhash引用 |

## DestinyProgressionDefinition
**进度定义：声望/等级进度条** · 172 行 · 主键 `id` · 15 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, displayUnitsName, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `scope` | Number | 作用范围枚举 |
| `repeatLastStep` | Boolean | 布尔标记 |
| `steps` | Array[12]{displayEffectType, progressTotal, stepName} | step数组（12{displayEffectType, progressTotal, stepName}） |
| `visible` | Boolean | 是否可见 |
| `progressToNextStepScaling` | Number | progress/to/next/step/scaling数值 |
| `storageMappingIndex` | Number | 排序值 |
| `currentResetCountUnlockValueHash` | Number | current/reset/count/unlock/valuehash引用 |
| `rewardItems` | Array[?] | reward/item数组（?） |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `factionHash` | Number | factionhash引用 |
| `color` | Object{alpha, blue, green, red} | 颜色(RGBA) |

## DestinyProgressionLevelRequirementDefinition
**进度等级需求定义** · 11 行 · 主键 `id` · 6 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `requirementCurve` | Array[12]{value, weight} | requirement/curve数组（12{value, weight}） |
| `progressionHash` | Number | 进度系统hash |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyRaceDefinition
**种族定义：人类/觉醒者/Exo** · 3 行 · 主键 `id` · 8 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `raceType` | Number | 类型枚举 |
| `genderedRaceNames` | Object{Female, Male} | gendered/race/name对象（Female, Male） |
| `genderedRaceNamesByGenderHash` | Object{2204441813, 3111576190} | gendered/race/names/by/genderhash引用 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyRecordDefinition
**记录定义：Triumphs/成就记录** · 6169 行 · 主键 `id` · 24 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, iconSequences, name} | 显示属性（名称/描述/图标） |
| `scope` | Number | 作用范围枚举 |
| `objectiveHashes` | Array[?] | objectivehash数组（引用列表） |
| `recordValueStyle` | Number | record/value/style数值 |
| `forTitleGilding` | Boolean | 布尔标记 |
| `shouldShowLargeIcons` | Boolean | 布尔标记 |
| `titleInfo` | Object{hasTitle} | title/info对象（hasTitle） |
| `completionInfo` | Object{ScoreValue, partialCompletionObjectiveCountThreshold, should... | completion/info对象（ScoreValue, partialCompletioniveCountThreshold, shouldFireToast, toastStyle） |
| `stateInfo` | Object{claimedUnlockHash, completeUnlockHash, completedCounterUnloc... | 状态信息对象（含需求） |
| `requirements` | Object{entitlementUnavailableMessage} | 参与要求 |
| `expirationInfo` | Object{description, hasExpiration} | expiration/info对象（description, hasExpiration） |
| `intervalInfo` | Object{intervalObjectives, intervalRewards, isIntervalVersionedFrom... | interval/info对象（intervalives, intervalRewards, isIntervalVersionedFromNormalRecord, originaliveArrayInsertionIndex） |
| `rewardItems` | Array[6]{hasConditionalVisibility, itemHash, quantity} | reward/item数组（6{hasConditionalVisibility, itemHash, quantity}） |
| `anyRewardHasConditionalVisibility` | Boolean | 布尔标记 |
| `recordTypeName` | String | 名称文本 |
| `presentationNodeType` | Number | 展示节点类型 |
| `traitIds` | Array[?] | 特性ID数组 |
| `traitHashes` | Array[?] | 特性hash数组 |
| `parentNodeHashes` | Array[Number] | 父节点hash数组 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `loreHash` | Number | lorehash引用 |

## DestinyReportReasonCategoryDefinition
**举报原因分类定义** · 0 行 · 主键 `id` · 0 个 JSON 字段  

（JSON 为空结构或无字段）

## DestinyRewardSourceDefinition
**奖励来源定义** · 0 行 · 主键 `id` · 0 个 JSON 字段  

（JSON 为空结构或无字段）

## DestinySackRewardItemListDefinition
**战利品池定义：掉落池/奖励池** · 6639 行 · 主键 `id` · 4 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinySandboxPatternDefinition
**沙盒模式定义** · 1402 行 · 主键 `id` · 11 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `patternHash` | Number | 模式标识hash |
| `patternGlobalTagIdHash` | Number | 全局标签ID hash |
| `weaponContentGroupHash` | Number | 武器内容组hash |
| `weaponTranslationGroupHash` | Number | 武器翻译组hash |
| `weaponTypeHash` | Number | 武器类型hash |
| `weaponType` | Number | 武器类型枚举 |
| `filters` | Array[7]{arrangementIndexByStatValue, artArrangementRegionHash, art... | 过滤器数组 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinySandboxPerkDefinition
**沙盒Perk定义：武器/护甲Perk效果** · 5203 行 · 主键 `id` · 7 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, iconSequences, name} | 显示属性（名称/描述/图标） |
| `isDisplayable` | Boolean | 是否可显示 |
| `damageType` | Number | 伤害类型枚举 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinySeasonDefinition
**赛季定义：赛季编号/主题** · 28 行 · 主键 `id` · 18 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `seasonNumber` | Number | 赛季编号 |
| `seasonPassList` | Array[1]{ownershipUnlockFlagHash, seasonPassEndDate, seasonPassHash... | 通行证列表（解锁/哈希/起止时间） |
| `seasonPassProgressionHash` | Number | 通行证进度hash |
| `startTimeInSeconds` | String | 开始时间（秒时间戳） |
| `seasonalChallengesPresentationNodeHash` | Number | 赛季挑战展示节点hash |
| `seasonPassUnlockHash` | Number | 通行证解锁hash |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `backgroundImagePath` | String | 背景图路径 |
| `startDate` | String | 开始日期 |
| `endDate` | String | 结束日期 |
| `artifactItemHash` | Number | 神器物品hash |
| `preview` | Object{description, images, linkPath} | 预览（描述/图片/链接） |
| `sealPresentationNodeHash` | Number | 印章展示节点hash |
| `acts` | Array[3]{displayName, rankCount, startTime} | 赛季幕列表（幕名/等级/时间） |

## DestinySeasonPassDefinition
**赛季通行证定义** · 23 行 · 主键 `id` · 10 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `rewardProgressionHash` | Number | 奖励进度hash |
| `prestigeProgressionHash` | Number | 声望进度hash |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `linkRedirectPath` | String | 链接重定向路径 |
| `color` | Object{alpha, blue, green, red} | 颜色(RGBA) |
| `images` | Object{iconImagePath, themeBackgroundImagePath} | 图片资源（背景图/图标路径） |

## DestinySocialCommendationDefinition
**社交推荐定义：玩家互评** · 16 行 · 主键 `id` · 11 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `cardImagePath` | String | 卡片图片路径 |
| `color` | Object{alpha, blue, green, red} | 颜色(RGBA) |
| `displayPriority` | Number | 显示优先级 |
| `activityGivingLimit` | Number | 单次活动给予上限 |
| `parentCommendationNodeHash` | Number | 上级推荐节点hash |
| `displayActivities` | Array[1]{description, hasIcon, icon, iconHash, name} | 展示活动列表 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinySocialCommendationNodeDefinition
**社交推荐节点定义** · 5 行 · 主键 `id` · 10 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `parentCommendationNodeHash` | Number | 上级推荐节点hash |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `displayProperties` | Object{description, hasIcon, icon, iconHash, name} | 显示属性（名称/描述/图标） |
| `color` | Object{alpha, blue, green, red} | 颜色(RGBA) |
| `tintedIcon` | String | 着色图标路径 |
| `childCommendationHashes` | Array[Number] | 子推荐hash数组 |
| `childCommendationNodeHashes` | Array[Number] | 子推荐节点hash数组 |

## DestinySocketCategoryDefinition
**插槽分类定义** · 65 行 · 主键 `id` · 7 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `uiCategoryStyle` | Number | UI分类样式 |
| `categoryStyle` | Number | 分类样式枚举 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinySocketTypeDefinition
**插槽类型定义** · 1874 行 · 主键 `id` · 15 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `insertAction` | Object{actionExecuteSeconds, actionSoundHash, actionType, isPositiv... | 插入动作（执行秒/音效/类型） |
| `plugWhitelist` | Array[1]{categoryHash, categoryIdentifier} | 插件白名单（分类/标识符） |
| `socketCategoryHash` | Number | 插槽分类hash |
| `visibility` | Number | 可见性枚举 |
| `alwaysRandomizeSockets` | Boolean | 始终随机插槽 |
| `isPreviewEnabled` | Boolean | 是否启用预览 |
| `hideDuplicateReusablePlugs` | Boolean | 隐藏重复可复用插件 |
| `overridesUiAppearance` | Boolean | 覆盖UI外观 |
| `avoidDuplicatesOnInitialization` | Boolean | 初始化避免重复 |
| `currencyScalars` | Array[?] | 货币标量数组 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyStatDefinition
**属性定义** · 79 行 · 主键 `id` · 9 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, icon, iconHash, iconSequences, name} | 显示属性（名称/描述/图标） |
| `aggregationType` | Number | 聚合类型 |
| `hasComputedBlock` | Boolean | 是否有计算块 |
| `statCategory` | Number | 属性分类 |
| `interpolate` | Boolean | 是否插值 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyStatGroupDefinition
**属性组定义** · 112 行 · 主键 `id` · 8 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `maximumValue` | Number | 最大值 |
| `uiPosition` | Number | UI位置 |
| `scaledStats` | Array[12]{displayAsNumeric, displayInterpolation, maximumValue, sta... | 缩放属性列表（statHash/displayAsNumeric等） |
| `overrides` | Object{} | 覆盖数据 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyTraitDefinition
**特质定义** · 554 行 · 主键 `id` · 6 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `displayHint` | String | 显示提示 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyUnlockDefinition
**解锁条件定义** · 58194 行 · 主键 `id` · 7 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, iconHash, name} | 显示属性（名称/描述/图标） |
| `unlockType` | Number | 解锁类型 |
| `scope` | Number | 作用范围枚举 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

## DestinyVendorDefinition
**商人定义：NPC商人出售信息** · 2170 行 · 主键 `id` · 32 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `displayProperties` | Object{description, hasIcon, highResIcon, icon, iconHash, iconSeque... | 显示属性（名称/描述/图标） |
| `vendorProgressionType` | Number | 商人进度类型枚举 |
| `displayItemHash` | Number | 显示物品hash |
| `inhibitBuying` | Boolean | 是否禁止购买 |
| `inhibitSelling` | Boolean | 是否禁止出售 |
| `factionHash` | Number | factionhash引用 |
| `resetIntervalMinutes` | Number | 重置间隔分钟 |
| `resetOffsetMinutes` | Number | 重置偏移分钟 |
| `failureStrings` | Array[?] | 失败提示字符串列表 |
| `unlockRanges` | Array[?] | 解锁范围列表 |
| `enabled` | Boolean | 是否启用 |
| `visible` | Boolean | 是否可见 |
| `consolidateCategories` | Boolean | 是否合并分类 |
| `unlockValueHash` | Number | 解锁值hash |
| `actions` | Array[?] | 动作列表 |
| `categories` | Array[1]{buyStringOverride, categoryHash, categoryIndex, disabledDe... | 商品分类列表 |
| `originalCategories` | Array[1]{buyStringOverride, categoryHash, categoryIndex, disabledDe... | 原始分类列表 |
| `displayCategories` | Array[1]{displayCategoryHash, displayInBanner, displayProperties, i... | 显示分类列表 |
| `interactions` | Array[?] | 交互行为列表 |
| `inventoryFlyouts` | Array[?] | 库存弹出菜单列表 |
| `itemList` | Array[14]{action, categoryIndex, creationLevels, currencies, displa... | 售卖物品列表 |
| `services` | Array[?] | 服务列表 |
| `acceptedItems` | Array[?] | 可接收物品列表 |
| `returnWithVendorRequest` | Boolean | 随商人请求返回 |
| `ignoreSaleItemHashes` | Array[?] | 忽略出售物品hash列表 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |
| `vendorIdentifier` | String | 商人唯一标识符 |
| `locations` | Array[1]{destinationHash} | 位置列表（含目的地hash） |
| `groups` | Array[?] | 分组列表 |

## DestinyVendorGroupDefinition
**商人分组定义** · 11 行 · 主键 `id` · 6 个 JSON 字段  

| 字段 | 类型 | 描述 |
|------|------|------|
| `order` | Number | 排序号 |
| `categoryName` | String | 分类名称 |
| `hash` | Number | 全局唯一标识hash |
| `index` | Number | Manifest排序索引 |
| `redacted` | Boolean | Bungie隐藏标记 |
| `blacklisted` | Boolean | 黑名单标记 |

---
> 共 83 张表 · 878 个 JSON 字段描述