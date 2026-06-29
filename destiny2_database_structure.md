# Destiny 2 离线数据库结构

| # | 表名 | 字段 | 内容说明 |
|---|---|---|---|
| 1 | `DestinyAchievementDefinition` | id, json | 成就/奖杯定义 |
| 2 | `DestinyActivityDefinition` | id, json | 活动/副本定义（打击、突袭、熔炉等） |
| 3 | `DestinyActivityDifficultyTierCollectionDefinition` | id, json | 活动难度等级集合 |
| 4 | `DestinyActivityFamilyDefinition` | id, json | 活动系列分组 |
| 5 | `DestinyActivityGraphDefinition` | id, json | 活动导航图定义（目的地地图节点） |
| 6 | `DestinyActivityInteractableDefinition` | id, json | 活动中可互动对象定义 |
| 7 | `DestinyActivityLoadoutRestrictionDefinition` | id, json | 活动配装限制定义 |
| 8 | `DestinyActivityModeDefinition` | id, json | 活动模式定义（如铁旗、试炼等） |
| 9 | `DestinyActivityModifierDefinition` | id, json | 活动 modifiers/词缀定义 |
| 10 | `DestinyActivitySelectableSkullCollectionDefinition` | id, json | 可选活动词缀集合 |
| 11 | `DestinyActivitySelectableSkullExclusionGroupDefinition` | id, json | 可选词缀互斥组 |
| 12 | `DestinyActivitySkullCategoryDefinition` | id, json | 活动词缀分类 |
| 13 | `DestinyActivitySkullCollectionDefinition` | id, json | 活动词缀集合定义 |
| 14 | `DestinyActivitySkullSubcategoryDefinition` | id, json | 活动词缀子分类 |
| 15 | `DestinyActivityTypeDefinition` | id, json | 活动类型定义 |
| 16 | `DestinyArtifactDefinition` | id, json | 赛季神器/圣物定义 |
| 17 | `DestinyBondDefinition` | id, json | 职业印记/标识定义 |
| 18 | `DestinyBreakerTypeDefinition` | id, json | 破盾类型定义（干扰、穿刺等） |
| 19 | `DestinyChecklistDefinition` | id, json | 检查清单定义（收集品进度） |
| 20 | `DestinyClassDefinition` | id, json | 职业定义（泰坦/猎人/术士） |
| 21 | `DestinyCollectibleDefinition` | id, json | 收藏品定义 |
| 22 | `DestinyDamageTypeDefinition` | id, json | 伤害类型定义（电弧/灼烧/虚空等） |
| 23 | `DestinyDestinationDefinition` | id, json | 目的地/星球定义 |
| 24 | `DestinyEnergyTypeDefinition` | id, json | 能量类型定义 |
| 25 | `DestinyEquipableItemSetDefinition` | id, json | 可装备物品套装定义 |
| 26 | `DestinyEquipmentSlotDefinition` | id, json | 装备槽位定义（动能/能量/护甲等） |
| 27 | `DestinyEventCardDefinition` | id, json | 活动通行证/卡片定义 |
| 28 | `DestinyFactionDefinition` | id, json | 阵营定义 |
| 29 | `DestinyFireteamFinderActivityGraphDefinition` | id, json | 火力战队搜索器活动图定义 |
| 30 | `DestinyFireteamFinderActivitySetDefinition` | id, json | 火力战队搜索器活动集合 |
| 31 | `DestinyFireteamFinderConstantsDefinition` | id, json | 火力战队搜索器常量 |
| 32 | `DestinyFireteamFinderLabelDefinition` | id, json | 火力战队搜索器标签定义 |
| 33 | `DestinyFireteamFinderLabelGroupDefinition` | id, json | 火力战队搜索器标签分组 |
| 34 | `DestinyFireteamFinderOptionDefinition` | id, json | 火力战队搜索器选项定义 |
| 35 | `DestinyFireteamFinderOptionGroupDefinition` | id, json | 火力战队搜索器选项分组 |
| 36 | `DestinyGenderDefinition` | id, json | 性别定义 |
| 37 | `DestinyGlobalConstantsDefinition` | id, json | 游戏全局常量定义 |
| 38 | `DestinyGuardianRankConstantsDefinition` | id, json | 守护者等级常量定义 |
| 39 | `DestinyGuardianRankDefinition` | id, json | 守护者等级定义 |
| 40 | `DestinyHistoricalStatsDefinition` | key, json | 历史统计指标定义 |
| 41 | `DestinyIconDefinition` | id, json | 图标定义（前景/背景图） |
| 42 | `DestinyInventoryBucketDefinition` | id, json | 物品栏分类桶定义 |
| 43 | `DestinyInventoryItemConstantsDefinition` | id, json | 物品常量定义 |
| 44 | `DestinyInventoryItemDefinition` | id, json | 物品/装备定义（武器、护甲、消耗品等所有物品） |
| 45 | `DestinyItemCategoryDefinition` | id, json | 物品分类定义 |
| 46 | `DestinyItemFilterDefinition` | id, json | 物品过滤器定义 |
| 47 | `DestinyItemTierTypeDefinition` | id, json | 物品品质等级定义（普通/稀有/传说/异域等） |
| 48 | `DestinyLoadoutColorDefinition` | id, json | 配置方案颜色定义 |
| 49 | `DestinyLoadoutConstantsDefinition` | id, json | 配置方案常量定义 |
| 50 | `DestinyLoadoutIconDefinition` | id, json | 配置方案图标定义 |
| 51 | `DestinyLoadoutNameDefinition` | id, json | 配置方案名称定义 |
| 52 | `DestinyLocationDefinition` | id, json | 地点位置定义 |
| 53 | `DestinyLoreDefinition` | id, json | 背景故事/Lore 定义 |
| 54 | `DestinyMaterialRequirementSetDefinition` | id, json | 材料需求集合定义 |
| 55 | `DestinyMedalTierDefinition` | id, json | 勋章等级定义 |
| 56 | `DestinyMetricDefinition` | id, json | 度量指标定义（追踪统计项） |
| 57 | `DestinyMilestoneDefinition` | id, json | 里程碑/周常任务定义 |
| 58 | `DestinyObjectiveDefinition` | id, json | 任务目标定义 |
| 59 | `DestinyPlaceDefinition` | id, json | 场景/地点定义 |
| 60 | `DestinyPlugSetDefinition` | id, json | 插槽插入物集合定义（模组池） |
| 61 | `DestinyPowerCapDefinition` | id, json | 能量上限定义（每赛季软/硬上限） |
| 62 | `DestinyPresentationNodeDefinition` | id, json | 展示节点定义（收藏品/ triumphs 树） |
| 63 | `DestinyProgressionDefinition` | id, json | 进度系统定义（声望/等级等） |
| 64 | `DestinyProgressionLevelRequirementDefinition` | id, json | 进度等级需求定义 |
| 65 | `DestinyRaceDefinition` | id, json | 种族定义（人类/觉醒者/Exo） |
| 66 | `DestinyRecordDefinition` | id, json | 记录/ triumphs 定义 |
| 67 | `DestinyReportReasonCategoryDefinition` | id, json | 举报原因分类定义 |
| 68 | `DestinyRewardSourceDefinition` | id, json | 奖励来源定义 |
| 69 | `DestinySackRewardItemListDefinition` | id, json | 战利品袋奖励列表定义 |
| 70 | `DestinySandboxPatternDefinition` | id, json | 沙盒模式/武器模型定义 |
| 71 | `DestinySandboxPerkDefinition` | id, json | 沙盒 Perk/技能定义 |
| 72 | `DestinySeasonDefinition` | id, json | 赛季定义 |
| 73 | `DestinySeasonPassDefinition` | id, json | 季票定义 |
| 74 | `DestinySocialCommendationDefinition` | id, json | 社交赞誉定义（赛后点赞） |
| 75 | `DestinySocialCommendationNodeDefinition` | id, json | 社交赞誉节点定义 |
| 76 | `DestinySocketCategoryDefinition` | id, json | 插槽分类定义 |
| 77 | `DestinySocketTypeDefinition` | id, json | 插槽类型定义 |
| 78 | `DestinyStatDefinition` | id, json | 属性定义（敏捷/力量/智力等） |
| 79 | `DestinyStatGroupDefinition` | id, json | 属性组定义 |
| 80 | `DestinyTraitDefinition` | id, json | 特性标签定义 |
| 81 | `DestinyUnlockDefinition` | id, json | 解锁条件定义（游戏状态标记） |
| 82 | `DestinyVendorDefinition` | id, json | 商人/NPC 定义 |
| 83 | `DestinyVendorGroupDefinition` | id, json | 商人群组定义 |