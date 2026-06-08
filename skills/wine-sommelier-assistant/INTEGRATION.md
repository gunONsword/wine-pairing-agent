# Wine Sommelier Skill Integration

这个目录是当前项目内的 sommelier skill bundle。

核心 skill：

```text
skills/wine-sommelier-assistant/SKILL.md
```

辅助 skills：

```text
skills/wine-sommelier-assistant/integrated-skills/recipe_search
skills/wine-sommelier-assistant/integrated-skills/recipe-generator
skills/wine-sommelier-assistant/integrated-skills/nutrition-analyzer
skills/wine-sommelier-assistant/integrated-skills/meal_planner
```

## 整合方式

`wine-sommelier-assistant` 是这个项目的核心领域 skill，负责葡萄酒搭配、品鉴、产区和收藏知识。

`integrated-skills` 目录里的 skill 作为辅助能力：

- `recipe_search`：当用户只给菜名或食材时，可用于检索 recipe。
- `recipe-generator`：当 recipe 不完整时，可用于补全或生成标准菜谱。
- `nutrition-analyzer`：当 pairing 需要考虑营养、热量、健康目标时，可作为后续扩展。
- `meal_planner`：当需求从单道菜扩展到一周菜单或多餐搭配时，可作为后续扩展。

当前代码运行时并不会自动执行这些 skill 文件。它们被放进项目内，是为了让 agent 的领域知识、后续扩展依据和可审查材料都跟随仓库版本管理。

## 当前代码里的对应关系

```text
LangGraph agent
  -> src/wine_pairing_agent/graph.py

MiniMax 调用
  -> src/wine_pairing_agent/llm.py

菜品结构化模型
  -> src/wine_pairing_agent/models.py

本地候选酒规则
  -> src/wine_pairing_agent/wine_rules.py

领域 skill bundle
  -> skills/wine-sommelier-assistant/
```

后续如果要真正把这些 skills 接入 LangGraph，可以新增节点，例如：

```text
recipe_search_node
  -> 当用户输入太短时搜索 recipe

recipe_generation_node
  -> 当 recipe 缺少做法或食材时补全

nutrition_context_node
  -> 当用户给出健康目标时加入营养约束

meal_plan_pairing_node
  -> 当用户请求多餐或一周菜单时批量生成 pairing
```

