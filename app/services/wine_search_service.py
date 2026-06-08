from __future__ import annotations

from agents.sommelier_agent import candidate_wines
from graph.state import RecipeProfile, WineCandidate


def search_candidate_wines(profile: RecipeProfile, skill_name: str | None = None) -> list[WineCandidate]:
    return candidate_wines(profile, skill_name)
