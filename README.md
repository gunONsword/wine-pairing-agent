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
  -> parse_recipe
  -> retrieve_candidates
  -> recommend_pairing
  -> format_answer
  -> 最终推荐结果
```

## Workflow 详细流程

一次完整推荐会经历 5 个主要阶段：

```text
1. 用户输入菜谱
   输入可以是一句话菜品描述，也可以是一整段 recipe 文本。

2. 菜品结构化分析
   parse_recipe 节点调用 MiniMax，把自然语言菜谱转成 RecipeProfile。
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

5. 输出格式化
   format_answer 节点把结构化结果整理成 Markdown，方便命令行阅读。
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

- `parse_recipe`：调用 MiniMax，把用户输入的菜谱解析成结构化菜品画像，例如主食材、烹饪方法、酸度、脂肪、辣度、甜度、风味强度。
- `retrieve_candidates`：根据菜品画像，用本地 wine pairing 规则生成候选酒款，例如 Riesling、Chardonnay、Pinot Noir、Syrah、Sauvignon Blanc。
- `recommend_pairing`：再次调用 MiniMax，让模型从候选酒中选择最合适的一款，并生成搭配理由、替代选项和应避免的酒款。
- `format_answer`：把结构化推荐结果整理成用户可读的 Markdown 文本。

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
  src/
    wine_pairing_agent/
      __init__.py
      cli.py
      config.py
      graph.py
      llm.py
      models.py
      prompts.py
      wine_rules.py
  tests/
    test_wine_rules.py
```

主要文件说明：

- `src/wine_pairing_agent/cli.py`：命令行入口，负责接收用户输入。
- `src/wine_pairing_agent/config.py`：读取 `.env` 和 MiniMax 配置。
- `src/wine_pairing_agent/graph.py`：LangGraph 工作流核心，定义 Agent 节点和执行顺序。
- `src/wine_pairing_agent/llm.py`：封装 MiniMax LLM 调用和 JSON 解析。
- `src/wine_pairing_agent/models.py`：定义菜品画像、候选酒、推荐结果等 Pydantic 数据结构。
- `src/wine_pairing_agent/prompts.py`：存放给 MiniMax 的 prompt 模板。
- `src/wine_pairing_agent/wine_rules.py`：本地葡萄酒候选规则，用于根据菜品特征生成候选酒。
- `tests/test_wine_rules.py`：基础规则测试。

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
& 'C:\Users\gos\project\nursing-record-assistant\.venv\Scripts\python.exe' -m wine_pairing_agent.cli --recipe "Spicy Sichuan mapo tofu with pork, chili bean paste, tofu, scallions, and steamed rice"
```

也可以一行执行：

```powershell
cd C:\Users\gos\project\wine-pairing-agent; & 'C:\Users\gos\project\nursing-record-assistant\.venv\Scripts\python.exe' -m wine_pairing_agent.cli --recipe "Grilled salmon with lemon butter, asparagus, and dill"
```

也支持从文本文件读取 recipe：

```powershell
& 'C:\Users\gos\project\nursing-record-assistant\.venv\Scripts\python.exe' -m wine_pairing_agent.cli --file .\recipe.txt
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
