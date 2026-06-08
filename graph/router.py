from __future__ import annotations

from graph.state import AgentState


def route_after_intent(state: AgentState) -> str:
    """Reserved router for future multi-intent workflows."""
    return "retrieve_candidates"

