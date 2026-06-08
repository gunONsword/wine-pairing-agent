from __future__ import annotations

from typing import Literal, TypedDict

from pydantic import BaseModel, Field, field_validator

from graph.state import PairingSkillSelection, RecipeProfile


class WineProfile(BaseModel):
    name: str = Field(default="Untitled wine")
    grapes: list[str] = Field(default_factory=list)
    country: str = ""
    region: str = ""
    style: str = ""
    flavor_notes: list[str] = Field(default_factory=list)
    acidity: Literal["low", "medium", "high"] = "medium"
    tannin: Literal["low", "medium", "high"] = "medium"
    body: Literal["light", "medium", "full"] = "medium"
    sweetness: Literal["dry", "off-dry", "medium", "sweet"] = "dry"
    alcohol: Literal["low", "medium", "high"] = "medium"
    oak: Literal["none", "light", "medium", "heavy"] = "none"


class PairingScoreResult(BaseModel):
    pairing_score: int = Field(ge=0, le=100)
    verdict: Literal["excellent", "good", "acceptable", "risky", "poor"]
    flavor_analysis: str
    tannin: str
    acidity: str
    body: str
    pairing_reason: str
    matches: list[str] = Field(default_factory=list)
    conflicts: list[str] = Field(default_factory=list)
    adjustments: list[str] = Field(default_factory=list)

    @field_validator("matches", "conflicts", "adjustments", mode="before")
    @classmethod
    def normalize_list(cls, value: object) -> list[str]:
        if value is None:
            return []
        if not isinstance(value, list):
            return [str(value)]
        return [str(item) for item in value]


class ScorePairingState(TypedDict, total=False):
    recipe: str
    wine: str
    profile: RecipeProfile
    wine_profile: WineProfile
    skill_selection: PairingSkillSelection
    score_result: PairingScoreResult
    answer: str
