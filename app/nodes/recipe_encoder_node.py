from __future__ import annotations

from app.states.recommend_state import RecommendWineState
from app.states.score_state import ScorePairingState
from nodes.intent_node import parse_recipe_intent
from services.skill_service import select_pairing_skill


def encode_recipe(state: RecommendWineState | ScorePairingState) -> RecommendWineState | ScorePairingState:
    parsed = parse_recipe_intent(state)
    profile = parsed["profile"]
    return {
        "profile": profile,
        "skill_selection": select_pairing_skill(profile, state["recipe"]),
    }
