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


def test_international_skill_adds_aromatic_whites() -> None:
    profile = RecipeProfile(
        title="Mapo tofu",
        main_ingredients=["tofu", "pork", "chili bean paste"],
        flavor_notes=["Sichuan", "hot"],
        spice="hot",
    )

    wines = candidate_wines(profile, "wine-pairing-cuisine-international")

    assert any(wine.name == "Gewurztraminer" for wine in wines)


def test_oily_recipe_gets_sparkling_wine() -> None:
    profile = RecipeProfile(
        title="Tempura",
        main_ingredients=["shrimp", "vegetables"],
        cooking_methods=["fried"],
        oiliness="high",
    )

    wines = candidate_wines(profile)

    assert any(wine.name == "Brut Sparkling Wine" for wine in wines)


def test_viscous_recipe_gets_chardonnay() -> None:
    profile = RecipeProfile(
        title="Cream stew",
        main_ingredients=["chicken", "cream"],
        cooking_methods=["stewed"],
        viscosity="high",
    )

    wines = candidate_wines(profile)

    assert any(wine.name == "Chardonnay" for wine in wines)


def test_hard_texture_recipe_gets_syrah() -> None:
    profile = RecipeProfile(
        title="Chewy grilled lamb",
        main_ingredients=["lamb"],
        cooking_methods=["grilled"],
        hardness="high",
    )

    wines = candidate_wines(profile)

    assert any(wine.name == "Syrah" for wine in wines)
