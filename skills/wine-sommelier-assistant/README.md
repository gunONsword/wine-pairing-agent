# Wine Sommelier Assistant

This project-local skill supports the LangGraph wine-pairing agent.

Primary goals:

1. Analyze recipes, then recommend matching wines from a wine list using grape varieties, countries, regions, and style tags.
2. Compare recipe tags and wine tags to judge whether a pairing is strong, acceptable, risky, or poor.

Start with:

- `SKILL.md` for the main workflow.
- `_toc.md` for the module list.
- `modules/recipe-to-wine-profile.md` for recommendation output.
- `modules/pairing-tag-evaluator.md` for recipe/wine tag comparison.
- `modules/wine-list-matching-schema.md` for future wine-list matching.

No separate research workflow is required for normal use. The primary workflow starts from recipe analysis and wine-list tags.
