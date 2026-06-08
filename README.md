# Wine Pairing Agent

这是一个基于 LangGraph 的葡萄酒搭配 AI Agent。用户输入一段 recipe 或菜品描述后，Agent 会分析菜品的食材、烹饪方式、酸度、脂肪感、辣度和风味强度，然后推荐适合的葡萄酒，并说明 pairing 的理由。

当前版本是命令行交互形态，后续可以继续扩展成 FastAPI 接口、网页聊天界面或 LangGraph Studio 工作流。

## Agent 构造

这个 Agent 由两部分组成：

1. LangGraph 工作流
2. MiniMax 大模型调用

LangGraph 负责把推荐过程拆成多个节点，每个节点只做一件事。整体 workflow 如下：

```text
recipe 输入
  -> parse_recipe_intent
  -> retrieve_candidates
  -> recommend_pairing
  -> evaluate_recommendation
  -> format_output
  -> 最终推荐结果
```

## Workflow 详细流程

一次完整推荐会经历 6 个主要阶段：

```text
1. 用户输入菜谱
   输入可以是一句话菜品描述，也可以是一整段 recipe 文本。

2. 菜品结构化分析
   parse_recipe_intent 节点调用 MiniMax，把自然语言菜谱转成 RecipeProfile。
   这个结构里包含：
   - title
   - main_ingredients
   - cooking_methods
   - flavor_notes
   - intensity
   - acidity
   - sweetness
   - fat
   - spice

3. 候选酒生成
   retrieve_candidates 节点不直接问模型，而是先用本地规则生成候选酒。
   这样可以让 Agent 的推荐更稳定，也方便后续扩展自己的 wine knowledge base。

4. 最终推荐与解释
   recommend_pairing 节点把菜品画像和候选酒交给 MiniMax。
   MiniMax 负责选择 top pick，并生成 pairing reason、alternatives 和 avoid 列表。

5. 推荐评估
   evaluate_recommendation 节点先做轻量结构检查。

6. 输出格式化
   format_output 节点把结构化结果整理成 Markdown，方便命令行阅读。
```

简单来说，这个 Agent 不是一次性把所有问题丢给大模型，而是先用 LangGraph 拆步骤：

```text
理解菜品 -> 生成候选 -> 模型决策 -> 解释理由 -> 格式化输出
```

这样做的好处是：

- 比单 prompt 更容易调试。
- 每个节点可以单独替换。
- wine rules 可以本地维护，不完全依赖模型。
- 后续可以加搜索、数据库、用户偏好、预算过滤等节点。

各节点作用如下：

- `parse_recipe_intent`：调用 MiniMax，把用户输入的菜谱解析成结构化菜品画像，例如主食材、烹饪方法、酸度、脂肪、辣度、甜度、风味强度。
- `retrieve_candidates`：根据菜品画像，用本地 wine pairing 规则生成候选酒款，例如 Riesling、Chardonnay、Pinot Noir、Syrah、Sauvignon Blanc。
- `recommend_pairing`：再次调用 MiniMax，让模型从候选酒中选择最合适的一款，并生成搭配理由、替代选项和应避免的酒款。
- `evaluate_recommendation`：对推荐结果做轻量结构检查。
- `format_output`：把结构化推荐结果整理成用户可读的 Markdown 文本。

MiniMax 使用 OpenAI-compatible Chat Completions API：

- Base URL: `https://api.minimax.io/v1`
- 默认模型: `MiniMax-M3`
- API key: 从 `.env` 或系统环境变量读取

## 文件结构

```text
wine-pairing-agent/
  .env.example
  .gitignore
  README.md
  pyproject.toml
  requirements.txt
  app/
    main.py
    config.py
  graph/
    workflow.py
    state.py
    router.py
    checkpoint.py
  nodes/
    intent_node.py
    retrieve_node.py
    pairing_node.py
    explanation_node.py
    evaluate_node.py
    output_node.py
  agents/
    sommelier_agent.py
    food_agent.py
    wine_agent.py
  tools/
    vector_search.py
    sql_tool.py
    wine_db_tool.py
    recipe_db_tool.py
  models/
    cocrossattention.py
    triplet_model.py
    vae_encoder.py
  prompts/
    intent_prompt.py
    explanation_prompt.py
    recommendation_prompt.py
  services/
    embedding_service.py
    rerank_service.py
    llm_service.py
  memory/
    redis_memory.py
    postgres_memory.py
  skills/
    wine-sommelier-assistant/
  tests/
    test_wine_rules.py
```

主要文件说明：

- `app/main.py`：命令行入口，负责接收用户输入。
- `app/config.py`：读取 `.env` 和 MiniMax 配置。
- `graph/workflow.py`：LangGraph 工作流核心，定义 Agent 节点和执行顺序。
- `graph/state.py`：定义菜品画像、候选酒、推荐结果和 AgentState。
- `nodes/intent_node.py`：解析用户输入的 recipe。
- `nodes/retrieve_node.py`：获取候选 wine。
- `nodes/pairing_node.py`：调用 MiniMax 选择最终 pairing。
- `nodes/evaluate_node.py`：对推荐结果做轻量结构检查。
- `nodes/output_node.py`：格式化最终输出。
- `agents/sommelier_agent.py`：本地葡萄酒候选规则，用于根据菜品特征生成候选酒。
- `prompts/intent_prompt.py`：菜品结构化分析 prompt。
- `prompts/recommendation_prompt.py`：葡萄酒推荐 prompt。
- `services/llm_service.py`：封装 MiniMax LLM 调用和 JSON 解析。
- `skills/wine-sommelier-assistant/`：项目内整合的 sommelier skill bundle。
- `tests/test_wine_rules.py`：基础规则测试。

## 预留文件说明

下面这些文件目前是占位文件，暂时没有接入主 workflow。它们不是无意义文件，而是为了后续扩展保留的分层位置：

另外，各目录里的 `__init__.py` 是 Python 包标记文件，用来保证 `app`、`graph`、`nodes` 等目录可以被正常 import，不承载业务逻辑。

| 文件 | 当前状态 | 预期用途 |
| --- | --- | --- |
| `graph/router.py` | 预留 | 未来支持多 intent 路由，例如单菜 pairing、一周菜单 pairing、只解释酒款等 |
| `graph/checkpoint.py` | 预留 | 未来接入 LangGraph checkpoint / persistent memory |
| `nodes/explanation_node.py` | 预留 | 未来把 pairing explanation 拆成独立 refinement 节点 |
| `agents/food_agent.py` | 空壳 | 未来负责 recipe 补全、菜品分析、食材规范化 |
| `agents/wine_agent.py` | 空壳 | 未来负责 wine catalog、产区、品种、价格、库存逻辑 |
| `tools/vector_search.py` | 空壳 | 未来接向量库，搜索 wine/recipe 知识 |
| `tools/sql_tool.py` | 空壳 | 未来接 SQL 数据库 |
| `tools/wine_db_tool.py` | 空壳 | 未来封装 wine database 查询 |
| `tools/recipe_db_tool.py` | 空壳 | 未来封装 recipe database 查询 |
| `models/cocrossattention.py` | 空壳 | 未来放深度匹配模型，不影响当前 Agent 运行 |
| `models/triplet_model.py` | 空壳 | 未来放 triplet ranking / embedding 模型 |
| `models/vae_encoder.py` | 空壳 | 未来放 VAE 风味表示模型 |
| `services/embedding_service.py` | 空壳 | 未来封装 embedding 生成 |
| `services/rerank_service.py` | 空壳 | 未来封装 rerank 逻辑 |
| `memory/redis_memory.py` | 空壳 | 未来接 Redis 会话记忆 |
| `memory/postgres_memory.py` | 空壳 | 未来接 Postgres 长期记忆 |

## 交互方式

当前交互方式是命令行：

```text
用户输入 recipe 或菜品描述
Agent 分析菜品
Agent 推荐葡萄酒
Agent 输出搭配理由
```

示例：

```powershell
cd C:\Users\gos\project\wine-pairing-agent
& 'C:\Users\gos\project\nursing-record-assistant\.venv\Scripts\python.exe' -m app.main --recipe "Spicy Sichuan mapo tofu with pork, chili bean paste, tofu, scallions, and steamed rice"
```

也可以一行执行：

```powershell
cd C:\Users\gos\project\wine-pairing-agent; & 'C:\Users\gos\project\nursing-record-assistant\.venv\Scripts\python.exe' -m app.main --recipe "Grilled salmon with lemon butter, asparagus, and dill"
```

也支持从文本文件读取 recipe：

```powershell
& 'C:\Users\gos\project\nursing-record-assistant\.venv\Scripts\python.exe' -m app.main --file .\recipe.txt
```

输出示例：

```text
# Wine Pairing Recommendation

Recipe: Spicy Sichuan mapo tofu with ground pork, chili bean paste, tofu, and scallions.

Top pick: Off-dry Riesling
Style: aromatic white with high acidity and gentle sweetness
Grapes: Riesling
Regions to look for: Mosel, Rheingau, Clare Valley
Serving: Serve chilled, around 6-8 C.

Why it pairs:
A little sweetness softens chili heat, while high acidity cuts through pork fat and fermented bean paste. Riesling's floral and stone-fruit notes also work well with Sichuan peppercorn and scallions.

Alternatives:
- Syrah: peppery and savory, works if you want a red wine.

Avoid:
- High-tannin Cabernet Sauvignon: tannin makes chili heat feel harsher.
```

## 环境变量

`.env` 文件不会提交到 GitHub，因为它已经被 `.gitignore` 忽略。

你可以参考 `.env.example`：

```powershell
MINIMAX_API_KEY=your-minimax-api-key
MINIMAX_BASE_URL=https://api.minimax.io/v1
MINIMAX_MODEL=MiniMax-M3
```

也可以直接在 PowerShell 里设置：

```powershell
$env:MINIMAX_API_KEY="your-minimax-api-key"
$env:MINIMAX_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL="MiniMax-M3"
```

## 测试

使用现有虚拟环境运行测试：

```powershell
cd C:\Users\gos\project\wine-pairing-agent
& 'C:\Users\gos\project\nursing-record-assistant\.venv\Scripts\python.exe' -m pytest -q
```

当前测试覆盖了基础 wine pairing 规则，例如：

- 辣味菜品会推荐 Off-dry Riesling
- 浓郁牛肉类菜品会推荐 Syrah

## 用到的 Skills 总结

这次根据粘贴文本中能安装的项目，已经安装到：

```text
C:\Users\gos\project\.agents\skills
```

同时，和本项目相关的 skills 已经复制进当前仓库，核心整合目录是：

```text
skills/wine-sommelier-assistant
```

其中 `wine-sommelier-assistant` 是核心 sommelier skill，其他辅助 skills 放在：

```text
skills/wine-sommelier-assistant/integrated-skills
```

项目内整合说明见：

```text
skills/wine-sommelier-assistant/INTEGRATION.md
```

和本项目最相关的 skills：

| Skill | 来源 | 作用 | 当前项目中的定位 |
| --- | --- | --- | --- |
| `wine-sommelier-assistant` | `sandraschi/advanced-memory-mcp` | 葡萄酒搭配、品鉴、产区、酒窖收藏相关知识 | 作为 wine pairing 领域参考 |
| `recipe_search` | `arunrlverma/openclaw-skills` | 根据食材、偏好、时间搜索食谱 | 后续可用于“用户只输入菜名时先找 recipe” |
| `recipe-generator` | `cclank/recipe-generator` 与 `ayia/NutriProfile` | 生成或管理菜谱内容 | 后续可用于补全 recipe 或生成标准菜谱 |
| `nutrition-analyzer` | `ayia/NutriProfile` | 食物识别、营养分析、热量和宏量营养估算 | 后续可扩展为“健康饮食 + wine pairing” |
| `meal_planner` | `arunrlverma/openclaw-skills` | 膳食计划相关 | 后续可扩展到一周菜单和配酒 |

已经尝试但未成功安装：

| Skill / Repo | 结果 | 原因 |
| --- | --- | --- |
| `techwavedev/agi-agent-kit-templates` | 未安装成功 | GitHub clone 认证失败，可能是私有仓库或需要账号权限 |

目前代码里的核心 Agent 没有直接依赖这些 skills 才能运行。它们更像是项目知识和后续扩展能力：

- 当前运行依赖：`langgraph`、`langchain-openai`、`pydantic`、MiniMax API。
- 当前推荐逻辑：`wine_rules.py` 本地规则 + MiniMax 决策。
- 后续可以把 recipe search、recipe generator、nutrition analyzer 等能力接入 LangGraph，变成更多节点。

## 后续扩展方向

可以继续扩展成：

- FastAPI 接口：前端或其他服务通过 HTTP 调用。
- Web Chat UI：用户在网页里输入菜谱并查看推荐。
- 更丰富的 wine knowledge base：加入产区、价格、购买链接、库存。
- 多轮对话：让用户补充预算、偏好、是否只喝红酒或白酒。
- 食谱检索结合：用户只说菜名时，先搜索或生成 recipe，再做 wine pairing。

## 分支工作流

当前仓库使用两个主要分支：

- `main`：稳定分支，用于保存确认过的版本。
- `develop`：开发分支，日常功能开发、文档更新和实验性修改默认推送到这里。

推荐流程：

```text
日常开发 -> push 到 develop
确认稳定 -> 询问是否合并到 main
得到确认 -> merge develop 到 main
```

以后如果需要把 `develop` 合并到 `main`，需要先确认，不会默认直接合并。
