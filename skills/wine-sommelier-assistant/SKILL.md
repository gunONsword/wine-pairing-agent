---
name: wine-sommelier-assistant
description: Analyze recipes and wine tags to recommend grape varieties, wine origins, and pairing quality for future wine-list matching
license: Proprietary
---

# Wine Sommelier Assistant

This skill is the domain guide for the wine-pairing-agent project.

It has two primary jobs:

1. Analyze a recipe with recipe-analysis skills, then use the analysis result to recommend matching wines from a wine list.
2. Evaluate whether a recipe and a wine are a good pairing by comparing their structured tags.

## When To Use This Skill

Use this skill when the user wants to:

- Recommend wine for a recipe.
- Convert a recipe into wine-list search criteria.
- Match recipe-derived tags against wines in a wine list.
- Explain why certain grape varieties or regions fit a dish.
- Compare recipe tags and wine tags to judge pairing quality.
- Prepare structured output that can later match wines from a wine list.

## Core Workflow

```text
Recipe text
  -> Extract recipe tags
  -> Build pairing profile
  -> Recommend grape varieties, origin, country, region
  -> Generate wine-list search criteria
  -> Match against available wine-list wines when provided
  -> Explain pairing reason
```

For wine-list evaluation:

```text
Recipe tags + Wine tags
  -> Compare acidity, body, tannin, sweetness, aroma, intensity, fat, spice, umami
  -> Score pairing quality
  -> Explain matches and conflicts
  -> Decide excellent / good / acceptable / risky / poor
```

## Required Output For Recipe-To-Wine Recommendation

When analyzing a recipe, produce structured output with:

- `recipe_profile`: main ingredients, cooking methods, sauce, flavor intensity, acidity, sweetness, fat, spice, umami, herbs, texture.
- `recommended_grapes`: grape varieties that fit the dish.
- `recommended_origins`: countries or broad origins that fit the style.
- `recommended_regions`: specific regions or appellations to search in a wine list.
- `wine_style_tags`: acidity, body, tannin, sweetness, oak, alcohol, fruit profile, mineral/herbal notes.
- `wine_list_query`: normalized fields useful for matching wines two years later.
- `wine_list_matches`: matching wines from the provided wine list, when a wine list is available.
- `pairing_reason`: concise but explicit reason.
- `avoid`: wine styles, grapes, or regions likely to clash.

## Required Sommelier Answer Sections

Every final pairing answer must include:

1. 风味分析
2. 单宁
3. 酸度
4. 酒体
5. Pairing理由

## Required Output For Pairing Evaluation

When given both recipe tags and wine tags, evaluate:

- `pairing_score`: 0-100.
- `verdict`: excellent, good, acceptable, risky, or poor.
- `matches`: tag-level reasons the pairing works.
- `conflicts`: tag-level risks or clashes.
- `adjustments`: serving temperature, decanting, sauce adjustment, or alternate wine style.

## Modules

Read these modules as needed:

- [Recipe to wine search profile](modules/recipe-to-wine-profile.md)
- [Pairing tag evaluator](modules/pairing-tag-evaluator.md)
- [Wine list matching schema](modules/wine-list-matching-schema.md)
- [Core guidance](modules/core-guidance.md)
- [Known gaps](modules/known-gaps.md)

## Practical Principles

- Recommend grape and region based on food structure, not only dish name.
- Prioritize acidity for fatty, fried, creamy, tomato-based, or citrus-driven dishes.
- Use sweetness or fruit intensity to manage heat and spice.
- Avoid heavy tannin with chili heat, delicate fish, bitter greens, or very acidic sauces.
- Match body and intensity: light food with lighter wines, rich food with fuller wines.
- Consider aroma bridges: herbs, pepper, smoke, earth, citrus, tropical fruit, florals.
- Return structured fields that are stable enough to match a future wine list.
