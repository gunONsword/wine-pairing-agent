from __future__ import annotations

from wine_pairing_agent.models import RecipeProfile, WineCandidate


def candidate_wines(profile: RecipeProfile) -> list[WineCandidate]:
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
                serving_note="Serve around 15-17 C; decant young bottles.",
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

    return _dedupe(candidates)


def _dedupe(candidates: list[WineCandidate]) -> list[WineCandidate]:
    seen: set[str] = set()
    unique: list[WineCandidate] = []
    for candidate in candidates:
        if candidate.name not in seen:
            seen.add(candidate.name)
            unique.append(candidate)
    return unique[:4]

