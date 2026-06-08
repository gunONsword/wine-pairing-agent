from __future__ import annotations

from app.states.score_state import ScorePairingState, WineProfile
from prompts.score_prompt import WINE_PROFILE_PROMPT
from services.llm_service import build_llm, invoke_json_model


def encode_wine(state: ScorePairingState) -> ScorePairingState:
    llm = build_llm()
    prompt = WINE_PROFILE_PROMPT.format(wine=state["wine"])
    return {"wine_profile": invoke_json_model(llm, prompt, WineProfile)}
