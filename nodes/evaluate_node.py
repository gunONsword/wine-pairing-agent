from __future__ import annotations

from graph.state import AgentState


def evaluate_recommendation(state: AgentState) -> AgentState:
    recommendation = state["recommendation"]
    return {
        "evaluation": {
            "has_top_pick": bool(recommendation.top_pick.name),
            "alternative_count": len(recommendation.alternatives),
            "avoid_count": len(recommendation.avoid),
        }
    }

