PAIRING_PROMPT = """You are a sommelier. Choose the best wine pairing for this recipe.

Recipe profile JSON:
{profile_json}

Candidate wines JSON:
{candidates_json}

Return strict JSON with:
recipe_summary: short summary of the dish
top_pick: one full candidate object from the list
alternatives: one or two candidate objects from the list
pairing_reason: explain the pairing using acidity, body, tannin, sweetness, fat, spice, aromatics, and cooking method
avoid: list of wine styles to avoid and why

Be practical and concise.
Use plain ASCII punctuation only.
"""

