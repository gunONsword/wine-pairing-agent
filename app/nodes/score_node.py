from __future__ import annotations

from app.states.score_state import PairingScoreResult, ScorePairingState
from prompts.score_prompt import PAIRING_SCORE_PROMPT
from services.llm_service import build_llm, invoke_json_model


def score_pairing_match(state: ScorePairingState) -> ScorePairingState:
    llm = build_llm()
    prompt = PAIRING_SCORE_PROMPT.format(
        recipe_profile_json=state["profile"].model_dump_json(indent=2),
        wine_profile_json=state["wine_profile"].model_dump_json(indent=2),
        selected_skill=state["skill_selection"].name,
        skill_reason=state["skill_selection"].reason,
        skill_context=state["skill_selection"].context,
    )
    return {"score_result": invoke_json_model(llm, prompt, PairingScoreResult)}
