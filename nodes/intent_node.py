from __future__ import annotations

from graph.state import AgentState, RecipeProfile
from prompts.intent_prompt import PROFILE_PROMPT
from services.llm_service import build_llm, invoke_json_model


def parse_recipe_intent(state: AgentState) -> AgentState:
    llm = build_llm()
    prompt = PROFILE_PROMPT.format(recipe=state["recipe"])
    return {"profile": invoke_json_model(llm, prompt, RecipeProfile)}

