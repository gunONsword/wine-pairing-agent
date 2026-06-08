from __future__ import annotations

import json

from graph.state import AgentState, PairingRecommendation
from prompts.recommendation_prompt import PAIRING_PROMPT
from services.llm_service import build_llm, invoke_json_model


def recommend_pairing(state: AgentState) -> AgentState:
    llm = build_llm()
    prompt = PAIRING_PROMPT.format(
        profile_json=state["profile"].model_dump_json(indent=2),
        selected_skill=state["skill_selection"].name,
        skill_reason=state["skill_selection"].reason,
        skill_context=state["skill_selection"].context,
        candidates_json=json.dumps([candidate.model_dump() for candidate in state["candidates"]], indent=2),
    )
    return {"recommendation": invoke_json_model(llm, prompt, PairingRecommendation)}

