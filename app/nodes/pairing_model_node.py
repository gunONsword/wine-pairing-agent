from __future__ import annotations

from app.states.recommend_state import RecommendWineState
from nodes.pairing_node import recommend_pairing


def run_pairing_model(state: RecommendWineState) -> RecommendWineState:
    return recommend_pairing(state)
