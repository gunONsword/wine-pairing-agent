from agents.sommelier_agent import candidate_wines
from graph.state import RecipeProfile


def test_spicy_recipe_gets_off_dry_riesling() -> None:
    profile = RecipeProfile(
        title="Spicy curry",
        main_ingredients=["chicken", "coconut milk", "chili"],
        cooking_methods=["simmered"],
        flavor_notes=["hot", "aromatic"],
        spice="hot",
    )

    wines = candidate_wines(profile)

    assert any(wine.name == "Off-dry Riesling" for wine in wines)


def test_rich_beef_gets_syrah() -> None:
    profile = RecipeProfile(
        title="Braised beef",
        main_ingredients=["beef", "mushroom"],
        cooking_methods=["braised"],
        flavor_notes=["savory"],
        intensity="rich",
    )

    wines = candidate_wines(profile)

    assert any(wine.name == "Syrah" for wine in wines)
