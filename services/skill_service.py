from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from graph.state import PairingSkillSelection, RecipeProfile


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = PROJECT_ROOT / "skills"


@dataclass(frozen=True)
class SkillRoute:
    name: str
    directory: str
    keywords: tuple[str, ...]
    reason: str


SKILL_ROUTES: tuple[SkillRoute, ...] = (
    SkillRoute(
        name="wine-pairing-desserts",
        directory="wine-pairing-desserts",
        keywords=("dessert", "cake", "chocolate", "custard", "ice cream", "honey", "caramel", "sweet pastry"),
        reason="The recipe reads as sweet or dessert-led, so dessert sweetness matching rules are primary.",
    ),
    SkillRoute(
        name="wine-pairing-cheese",
        directory="wine-pairing-cheese",
        keywords=("cheese", "brie", "camembert", "cheddar", "blue cheese", "goat cheese", "parmesan"),
        reason="Cheese texture, salt, fat, and rind style need cheese-specific pairing rules.",
    ),
    SkillRoute(
        name="wine-pairing-cuisine-international",
        directory="wine-pairing-cuisine-international",
        keywords=(
            "sichuan",
            "szechuan",
            "chinese",
            "cantonese",
            "thai",
            "vietnamese",
            "korean",
            "japanese",
            "indian",
            "mexican",
            "cajun",
            "bbq",
            "middle eastern",
            "moroccan",
            "peruvian",
            "soy",
            "miso",
            "gochujang",
            "curry",
            "chili bean paste",
        ),
        reason="The dish has a non-European cuisine signature, so cuisine-specific spice, sauce, and aroma rules matter.",
    ),
    SkillRoute(
        name="wine-pairing-cuisine-european",
        directory="wine-pairing-cuisine-european",
        keywords=(
            "french",
            "italian",
            "spanish",
            "german",
            "austrian",
            "portuguese",
            "greek",
            "scandinavian",
            "risotto",
            "paella",
            "ratatouille",
        ),
        reason="The recipe has a European cuisine pattern, so regional sauce and tradition rules are useful.",
    ),
    SkillRoute(
        name="wine-pairing-meat-red",
        directory="wine-pairing-meat-red",
        keywords=("beef", "steak", "lamb", "venison", "boar", "duck", "game", "ribeye", "short rib"),
        reason="The dominant protein is red meat, game, or duck, so tannin/body rules are central.",
    ),
    SkillRoute(
        name="wine-pairing-meat-white",
        directory="wine-pairing-meat-white",
        keywords=("chicken", "turkey", "pork", "veal", "poultry", "ham", "bacon", "sausage"),
        reason="The dominant protein is white meat or pork, so medium-body and sauce-sensitive rules are central.",
    ),
    SkillRoute(
        name="wine-pairing-fish-seafood",
        directory="wine-pairing-fish-seafood",
        keywords=("fish", "salmon", "tuna", "cod", "seafood", "shrimp", "prawn", "crab", "lobster", "oyster", "clam"),
        reason="Fish or seafood is central, so delicacy, salinity, oil, and acidity rules should lead.",
    ),
    SkillRoute(
        name="wine-pairing-pasta-pizza",
        directory="wine-pairing-pasta-pizza",
        keywords=("pasta", "pizza", "spaghetti", "lasagna", "ravioli", "gnocchi", "tomato sauce", "bolognese"),
        reason="Pasta or pizza structure makes sauce base and acidity the main pairing drivers.",
    ),
    SkillRoute(
        name="wine-pairing-vegetables",
        directory="wine-pairing-vegetables",
        keywords=("vegetable", "salad", "asparagus", "artichoke", "eggplant", "mushroom", "greens", "tofu", "bean"),
        reason="Vegetables, legumes, or tofu are structurally important, so green, earthy, bitter, and umami rules matter.",
    ),
)


SUPPORTING_SKILL_PATHS = (
    SKILLS_ROOT / "wine-sommelier-assistant" / "SKILL.md",
    SKILLS_ROOT / "wine-sommelier-assistant" / "modules" / "recipe-to-wine-profile.md",
    SKILLS_ROOT / "wine-pairing-fundamentals" / "SKILL.md",
)

RECIPE_ANALYSIS_SKILL_PATHS = (
    SKILLS_ROOT / "wine-sommelier-assistant" / "SKILL.md",
    SKILLS_ROOT / "wine-sommelier-assistant" / "modules" / "recipe-to-wine-profile.md",
)


def select_pairing_skill(profile: RecipeProfile, recipe: str) -> PairingSkillSelection:
    haystack = _profile_text(profile, recipe)
    route = _find_best_route(haystack, profile)
    selected_path = SKILLS_ROOT / route.directory / "SKILL.md"
    supporting_paths = list(SUPPORTING_SKILL_PATHS)
    context_paths = supporting_paths + [selected_path]

    return PairingSkillSelection(
        name=route.name,
        path=str(selected_path),
        reason=route.reason,
        supporting_skills=[str(path) for path in supporting_paths],
        context=_build_skill_context(context_paths),
    )


def recipe_analysis_skill_context() -> str:
    return _build_skill_context(list(RECIPE_ANALYSIS_SKILL_PATHS), max_chars_per_file=8000)


def _find_best_route(haystack: str, profile: RecipeProfile) -> SkillRoute:
    if profile.sweetness == "high":
        return _route_by_name("wine-pairing-desserts")

    for route in SKILL_ROUTES:
        if any(keyword in haystack for keyword in route.keywords):
            return route

    return _route_by_name("wine-pairing-fundamentals")


def _route_by_name(name: str) -> SkillRoute:
    for route in SKILL_ROUTES:
        if route.name == name:
            return route
    return SkillRoute(
        name="wine-pairing-fundamentals",
        directory="wine-pairing-fundamentals",
        keywords=(),
        reason="No narrow dish category dominated, so use the general pairing framework.",
    )


def _profile_text(profile: RecipeProfile, recipe: str) -> str:
    parts = [
        recipe,
        profile.title,
        " ".join(profile.main_ingredients),
        " ".join(profile.cooking_methods),
        " ".join(profile.flavor_notes),
        profile.intensity,
        profile.acidity,
        profile.sweetness,
        profile.fat,
        profile.spice,
        profile.viscosity,
        profile.oiliness,
        profile.hardness,
    ]
    return " ".join(parts).lower()


def _build_skill_context(paths: list[Path], max_chars_per_file: int = 12000) -> str:
    chunks: list[str] = []
    for path in paths:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if len(text) > max_chars_per_file:
            text = text[:max_chars_per_file] + "\n\n[Skill context truncated for prompt size.]"
        chunks.append(f"## Skill: {path.relative_to(PROJECT_ROOT)}\n\n{text}")
    return "\n\n---\n\n".join(chunks)
