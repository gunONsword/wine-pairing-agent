from __future__ import annotations

from graph.state import AgentState, RecipeProfile
from prompts.intent_prompt import PROFILE_PROMPT
from services.llm_service import build_llm, invoke_json_model
from services.skill_service import recipe_analysis_skill_context


def parse_recipe_intent(state: AgentState) -> AgentState:
    llm = build_llm()
    prompt = PROFILE_PROMPT.format(
        recipe=state["recipe"],
        recipe_analysis_context=recipe_analysis_skill_context(),
    )
    return {"profile": invoke_json_model(llm, prompt, RecipeProfile)}

