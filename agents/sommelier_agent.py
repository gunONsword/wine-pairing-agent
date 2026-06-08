from __future__ import annotations

from graph.state import RecipeProfile, WineCandidate


def candidate_wines(profile: RecipeProfile, skill_name: str | None = None) -> list[WineCandidate]:
    candidates: list[WineCandidate] = []
    ingredients = " ".join(profile.main_ingredients + profile.flavor_notes).lower()

    if any(term in ingredients for term in ["salmon", "tuna", "duck", "mushroom"]):
        candidates.append(
            WineCandidate(
                name="Pinot Noir",
                style="light-bodied red with red fruit and earthy notes",
                grapes=["Pinot Noir"],
                region_examples=["Burgundy", "Oregon Willamette Valley", "Central Otago"],
                why_it_might_work="Low tannin protects delicate protein while earthy red fruit handles savory depth.",
                serving_note="Serve slightly cool, around 13-15 C.",
            )
        )

    if profile.acidity == "high" or any(term in ingredients for term in ["lemon", "tomato", "vinegar", "capers"]):
        candidates.append(
            WineCandidate(
                name="Sauvignon Blanc",
                style="crisp aromatic white with citrus and herb notes",
                grapes=["Sauvignon Blanc"],
                region_examples=["Sancerre", "Marlborough", "Napa Valley"],
                why_it_might_work="Bright acidity mirrors citrus or tomato while herbal aromas connect with green herbs.",
                serving_note="Serve well chilled, around 7-9 C.",
            )
        )

    if profile.fat == "high" or any(term in ingredients for term in ["cream", "butter", "cheese", "pork belly"]):
        candidates.append(
            WineCandidate(
                name="Chardonnay",
                style="medium to full-bodied white with orchard fruit and texture",
                grapes=["Chardonnay"],
                region_examples=["Burgundy", "Sonoma Coast", "Margaret River"],
                why_it_might_work="Body and texture match richness, while enough acidity cuts butter, cream, or cheese.",
                serving_note="Choose lightly oaked for balance; serve around 9-11 C.",
            )
        )

    if profile.spice in {"mild", "hot"} or any(term in ingredients for term in ["chili", "curry", "sichuan", "gochujang"]):
        candidates.append(
            WineCandidate(
                name="Off-dry Riesling",
                style="aromatic white with high acidity and gentle sweetness",
                grapes=["Riesling"],
                region_examples=["Mosel", "Rheingau", "Clare Valley"],
                why_it_might_work="A little sweetness calms heat, and high acidity keeps spicy food lively.",
                serving_note="Serve chilled, around 6-8 C.",
            )
        )

    if profile.intensity == "rich" or any(term in ingredients for term in ["beef", "lamb", "braised", "stew", "roast"]):
        candidates.append(
            WineCandidate(
                name="Syrah",
                style="fuller red with dark fruit, pepper, and savory structure",
                grapes=["Syrah", "Shiraz"],
                region_examples=["Northern Rhone", "Barossa", "Washington State"],
                why_it_might_work="Dark fruit and pepper match roasted or braised intensity, and tannin handles red meat.",
                serving_note="Serve around 15-17 C.; decant young bottles.",
            )
        )

    if not candidates:
        candidates.append(
            WineCandidate(
                name="Dry Rose",
                style="versatile dry rose with red fruit, freshness, and moderate body",
                grapes=["Grenache", "Cinsault", "Syrah"],
                region_examples=["Provence", "Tavel", "Navarra"],
                why_it_might_work="Freshness, light tannin, and moderate fruit cover many recipes without overwhelming them.",
                serving_note="Serve chilled, around 8-10 C.",
            )
        )

    candidates.extend(_skill_candidates(skill_name))
    return _dedupe(candidates)


def _skill_candidates(skill_name: str | None) -> list[WineCandidate]:
    if skill_name == "wine-pairing-cuisine-international":
        return [
            WineCandidate(
                name="Gewurztraminer",
                style="aromatic white with lychee, rose, spice, and a soft texture",
                grapes=["Gewurztraminer"],
                region_examples=["Alsace", "Trentino-Alto Adige", "Marlborough"],
                why_it_might_work="Perfumed fruit and spice bridge aromatic sauces while low tannin avoids chili clashes.",
                serving_note="Choose dry to off-dry depending on heat; serve around 7-9 C.",
            ),
            WineCandidate(
                name="Vouvray Chenin Blanc",
                style="high-acid Chenin Blanc with apple, honey, and optional off-dry balance",
                grapes=["Chenin Blanc"],
                region_examples=["Vouvray", "Savennieres", "South Africa Swartland"],
                why_it_might_work="Acidity refreshes the palate, and a little residual sugar can handle heat or sweet-sour sauces.",
                serving_note="Serve chilled, around 7-9 C.",
            ),
        ]

    if skill_name == "wine-pairing-cuisine-european":
        return [
            WineCandidate(
                name="Sangiovese",
                style="medium-bodied high-acid red with cherry, herbs, and savory grip",
                grapes=["Sangiovese"],
                region_examples=["Chianti Classico", "Brunello di Montalcino", "Tuscany"],
                why_it_might_work="High acidity works with tomato, herbs, roasted vegetables, and many European sauces.",
                serving_note="Serve around 14-16 C.",
            )
        ]

    if skill_name == "wine-pairing-meat-red":
        return [
            WineCandidate(
                name="Cabernet Sauvignon",
                style="full-bodied tannic red with cassis, cedar, and dark fruit",
                grapes=["Cabernet Sauvignon"],
                region_examples=["Bordeaux Medoc", "Napa Valley", "Coonawarra"],
                why_it_might_work="Tannin binds with red-meat protein and fat while full body matches grilled or roasted intensity.",
                serving_note="Serve around 16-18 C.; decant young structured bottles.",
            ),
            WineCandidate(
                name="Malbec",
                style="full-bodied red with plush black fruit and moderate tannin",
                grapes=["Malbec"],
                region_examples=["Mendoza", "Cahors"],
                why_it_might_work="Dark fruit and body match charred beef while softer tannin keeps the pairing generous.",
                serving_note="Serve around 15-17 C.",
            ),
        ]

    if skill_name == "wine-pairing-meat-white":
        return [
            WineCandidate(
                name="Pinot Gris",
                style="medium-bodied white with pear fruit, spice, and rounded texture",
                grapes=["Pinot Gris", "Pinot Grigio"],
                region_examples=["Alsace", "Oregon", "Friuli"],
                why_it_might_work="Moderate body and texture fit pork or poultry without overpowering lighter meat.",
                serving_note="Serve around 8-10 C.",
            )
        ]

    if skill_name == "wine-pairing-fish-seafood":
        return [
            WineCandidate(
                name="Albarino",
                style="crisp coastal white with citrus, stone fruit, and saline freshness",
                grapes=["Albarino"],
                region_examples=["Rias Baixas", "Vinho Verde"],
                why_it_might_work="Salinity and high acidity echo seafood while keeping delicate flavors clear.",
                serving_note="Serve well chilled, around 6-8 C.",
            )
        ]

    if skill_name == "wine-pairing-pasta-pizza":
        return [
            WineCandidate(
                name="Barbera",
                style="juicy high-acid Italian red with low tannin and red fruit",
                grapes=["Barbera"],
                region_examples=["Barbera d'Asti", "Barbera d'Alba", "Piedmont"],
                why_it_might_work="High acidity handles tomato sauce while low tannin avoids bitterness with cheese and herbs.",
                serving_note="Serve around 13-15 C.",
            )
        ]

    if skill_name == "wine-pairing-vegetables":
        return [
            WineCandidate(
                name="Gruner Veltliner",
                style="crisp white with citrus, green apple, and white pepper",
                grapes=["Gruner Veltliner"],
                region_examples=["Wachau", "Kamptal", "Kremstal"],
                why_it_might_work="Green freshness and peppery notes connect with vegetables while acidity handles bitter edges.",
                serving_note="Serve well chilled, around 7-9 C.",
            )
        ]

    if skill_name == "wine-pairing-desserts":
        return [
            WineCandidate(
                name="Sauternes",
                style="sweet botrytized wine with honey, apricot, saffron, and high acidity",
                grapes=["Semillon", "Sauvignon Blanc", "Muscadelle"],
                region_examples=["Sauternes", "Barsac"],
                why_it_might_work="Sweetness can exceed dessert sweetness while acidity keeps the finish lifted.",
                serving_note="Serve chilled, around 8-10 C.",
            )
        ]

    if skill_name == "wine-pairing-cheese":
        return [
            WineCandidate(
                name="Champagne",
                style="sparkling wine with high acidity, bubbles, citrus, and brioche",
                grapes=["Chardonnay", "Pinot Noir", "Meunier"],
                region_examples=["Champagne"],
                why_it_might_work="Bubbles and acidity cut cheese fat and salt while autolytic notes bridge nutty flavors.",
                serving_note="Serve well chilled, around 6-8 C.",
            )
        ]

    return []


def _dedupe(candidates: list[WineCandidate]) -> list[WineCandidate]:
    seen: set[str] = set()
    unique: list[WineCandidate] = []
    for candidate in candidates:
        if candidate.name not in seen:
            seen.add(candidate.name)
            unique.append(candidate)
    return unique[:4]

