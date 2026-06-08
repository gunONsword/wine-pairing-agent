from __future__ import annotations

from app.states.recommend_state import RecommendWineState
from nodes.retrieve_node import retrieve_candidates


def retrieve_wines(state: RecommendWineState) -> RecommendWineState:
    return retrieve_candidates(state)
