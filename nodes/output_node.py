from __future__ import annotations

import unicodedata

from graph.state import AgentState


def format_output(state: AgentState) -> AgentState:
    recommendation = state["recommendation"]
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

Why it pairs:
{recommendation.pairing_reason}

Alternatives:
{alternatives or "- No alternatives suggested"}

Avoid:
{avoid}
"""
    return {"answer": _plain_ascii(answer)}


def _plain_ascii(text: str) -> str:
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
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")

