from __future__ import annotations

from typing import Literal, TypedDict

from pydantic import BaseModel, Field, field_validator


class RecipeProfile(BaseModel):
    title: str = Field(default="Untitled recipe")
    main_ingredients: list[str] = Field(default_factory=list)
    cooking_methods: list[str] = Field(default_factory=list)
    flavor_notes: list[str] = Field(default_factory=list)
    intensity: Literal["light", "medium", "rich"] = "medium"
    acidity: Literal["low", "medium", "high"] = "medium"
    sweetness: Literal["low", "medium", "high"] = "low"
    fat: Literal["low", "medium", "high"] = "medium"
    spice: Literal["none", "mild", "hot"] = "none"


class WineCandidate(BaseModel):
    name: str
    style: str
    grapes: list[str] = Field(default_factory=list)
    region_examples: list[str] = Field(default_factory=list)
    why_it_might_work: str
    serving_note: str


class PairingRecommendation(BaseModel):
    recipe_summary: str
    top_pick: WineCandidate
    alternatives: list[WineCandidate] = Field(default_factory=list)
    pairing_reason: str
    avoid: list[str] = Field(default_factory=list)

    @field_validator("avoid", mode="before")
    @classmethod
    def normalize_avoid(cls, value: object) -> list[str]:
        if value is None:
            return []
        if not isinstance(value, list):
            return [str(value)]

        normalized: list[str] = []
        for item in value:
            if isinstance(item, dict):
                style = item.get("style") or item.get("name") or "Wine style"
                reason = item.get("reason") or item.get("why") or item.get("description") or ""
                normalized.append(f"{style}: {reason}".strip(": "))
            else:
                normalized.append(str(item))
        return normalized


class AgentState(TypedDict, total=False):
    recipe: str
    profile: RecipeProfile
    candidates: list[WineCandidate]
    recommendation: PairingRecommendation
    answer: str
