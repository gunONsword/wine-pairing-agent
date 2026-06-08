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

Pairing principle skills：

```text
skills/wine-pairing-multilang/SKILL.md
skills/wine-pairing-en/SKILL.md
skills/packages/wine-pairing-multilang.skill
skills/packages/wine-pairing-en.skill
```

## 整合方式

`wine-sommelier-assistant` 是这个项目的核心领域 skill，负责两件事：

1. 根据 recipe 推荐可用于未来 wine list 搜索的葡萄品种、国家、产区、地区和风格标签。
2. 根据 recipe 标签和 wine 标签判断 pairing 是否合适，并解释匹配点和冲突点。

`integrated-skills` 目录里的 skill 作为辅助能力：

- `recipe_search`：当用户只给菜名或食材时，可用于检索 recipe。
- `recipe-generator`：当 recipe 不完整时，可用于补全或生成标准菜谱。
- `nutrition-analyzer`：当 pairing 需要考虑营养、热量、健康目标时，可作为后续扩展。
- `meal_planner`：当需求从单道菜扩展到一周菜单或多餐搭配时，可作为后续扩展。

新增核心模块：

- `modules/recipe-to-wine-profile.md`：把 recipe 转成葡萄品种、产地、产区和 wine style tags。
- `modules/pairing-tag-evaluator.md`：通过 recipe tags 和 wine tags 计算 pairing quality。
- `modules/wine-list-matching-schema.md`：定义未来 wine list 应该提供的字段和匹配优先级。

新增 pairing 原则库：

- `skills/wine-pairing-multilang/SKILL.md`：多语言原文版 food-wine pairing 抽象原则，适合保留原语言术语和地域搭配语感。
- `skills/wine-pairing-en/SKILL.md`：英文翻译版 food-wine pairing 抽象原则，适合 agent 统一理解和生成英文解释。
- `skills/packages/*.skill`：对应的可分享、可重装压缩包。

当前代码运行时并不会自动执行这些 skill 文件。它们被放进项目内，是为了让 agent 的领域知识、后续扩展依据和可审查材料都跟随仓库版本管理。

## 当前代码里的对应关系

```text
LangGraph agent
  -> graph/workflow.py

MiniMax 调用
  -> services/llm_service.py

菜品结构化模型
  -> graph/state.py

本地候选酒规则
  -> agents/sommelier_agent.py

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
