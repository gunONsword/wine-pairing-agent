from __future__ import annotations

from graph.state import AgentState
from services.skill_service import select_pairing_skill


def select_recipe_pairing_skill(state: AgentState) -> AgentState:
    return {"skill_selection": select_pairing_skill(state["profile"], state["recipe"])}
