from __future__ import annotations

from graph.state import AgentState


def format_output(state: AgentState) -> AgentState:
    recommendation = state["recommendation"]
    skill_selection = state["skill_selection"]
    top = recommendation.top_pick
    alternatives = "\n".join(f"- {wine.name}: {wine.why_it_might_work}" for wine in recommendation.alternatives)
    avoid = "\n".join(f"- {item}" for item in recommendation.avoid) or "- None"

    answer = f"""# Wine Pairing Recommendation

Recipe: {recommendation.recipe_summary}

Top pick: {top.name}
Style: {top.style}
Grapes: {", ".join(top.grapes) or "varies"}
Regions to look for: {", ".join(top.region_examples) or "many regions"}
Serving: {top.serving_note}

Skill workflow: recipe analysis -> {skill_selection.name}
Skill path: {skill_selection.path}
Skill reason: {skill_selection.reason}

1 风味分析
{recommendation.flavor_analysis or recommendation.recipe_summary}

2 单宁
{recommendation.tannin or "Prefer tannin that does not clash with the dish structure."}

3 酸度
{recommendation.acidity or "Choose acidity that balances the dish's fat, sauce, and freshness."}

4 酒体
{recommendation.body or "Match wine body to the dish intensity."}

5 Pairing理由
{recommendation.pairing_reason}

Alternatives:
{alternatives or "- No alternatives suggested"}

Avoid:
{avoid}
"""
    return {"answer": _normalize_punctuation(answer)}


def _normalize_punctuation(text: str) -> str:
    replacements = {
        "\u2013": "-",
        "\u2014": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    return text
