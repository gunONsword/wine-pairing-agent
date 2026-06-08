from __future__ import annotations

from app.states.score_state import PairingScoreResult, WineProfile
from graph.state import PairingSkillSelection, RecipeProfile
from prompts.score_prompt import PAIRING_SCORE_PROMPT
from services.llm_service import build_llm, invoke_json_model


def score_pairing_with_model(
    recipe_profile: RecipeProfile,
    wine_profile: WineProfile,
    skill_selection: PairingSkillSelection,
) -> PairingScoreResult:
    llm = build_llm()
    prompt = PAIRING_SCORE_PROMPT.format(
        recipe_profile_json=recipe_profile.model_dump_json(indent=2),
        wine_profile_json=wine_profile.model_dump_json(indent=2),
        selected_skill=skill_selection.name,
        skill_reason=skill_selection.reason,
        skill_context=skill_selection.context,
    )
    return invoke_json_model(llm, prompt, PairingScoreResult)
