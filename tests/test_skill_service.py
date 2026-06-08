from graph.state import RecipeProfile
from services.skill_service import select_pairing_skill


def test_sichuan_recipe_routes_to_international_skill() -> None:
    profile = RecipeProfile(
        title="Mapo tofu",
        main_ingredients=["tofu", "pork", "chili bean paste"],
        flavor_notes=["Sichuan", "hot", "umami"],
        spice="hot",
    )

    selection = select_pairing_skill(profile, "Spicy Sichuan mapo tofu")

    assert selection.name == "wine-pairing-cuisine-international"
    assert "wine-pairing-cuisine-international" in selection.path
    assert "recipe-to-wine-profile" in selection.context


def test_steak_routes_to_red_meat_skill() -> None:
    profile = RecipeProfile(
        title="Grilled steak",
        main_ingredients=["beef", "black pepper"],
        cooking_methods=["grilled"],
        intensity="rich",
    )

    selection = select_pairing_skill(profile, "Grilled ribeye steak")

    assert selection.name == "wine-pairing-meat-red"
