from __future__ import annotations

from app.states.recommend_state import RecommendWineState
from app.states.score_state import ScorePairingState
from nodes.evaluate_node import evaluate_recommendation
from nodes.output_node import format_output


def explain_recommendation(state: RecommendWineState) -> RecommendWineState:
    evaluated = evaluate_recommendation(state)
    merged = {**state, **evaluated}
    return format_output(merged)


def explain_score(state: ScorePairingState) -> ScorePairingState:
    result = state["score_result"]
    wine = state["wine_profile"]
    skill_selection = state["skill_selection"]
    matches = "\n".join(f"- {item}" for item in result.matches) or "- None"
    conflicts = "\n".join(f"- {item}" for item in result.conflicts) or "- None"
    adjustments = "\n".join(f"- {item}" for item in result.adjustments) or "- None"

    answer = f"""# Pairing Score

Wine: {wine.name}
Grapes: {", ".join(wine.grapes) or "unknown"}
Region: {", ".join(part for part in [wine.country, wine.region] if part) or "unknown"}
Score: {result.pairing_score}/100
Verdict: {result.verdict}

Skill workflow: recipe + wine analysis -> {skill_selection.name}
Skill path: {skill_selection.path}
Skill reason: {skill_selection.reason}

1 风味分析
{result.flavor_analysis}

2 单宁
{result.tannin}

3 酸度
{result.acidity}

4 酒体
{result.body}

5 Pairing理由
{result.pairing_reason}

Matches:
{matches}

Conflicts:
{conflicts}

Adjustments:
{adjustments}
"""
    return {"answer": answer}
