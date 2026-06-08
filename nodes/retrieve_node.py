from __future__ import annotations

from agents.sommelier_agent import candidate_wines
from graph.state import AgentState


def retrieve_candidates(state: AgentState) -> AgentState:
    return {"candidates": candidate_wines(state["profile"], state["skill_selection"].name)}

