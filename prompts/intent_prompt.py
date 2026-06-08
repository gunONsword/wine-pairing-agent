PROFILE_PROMPT = """You are a culinary analyst. Extract a compact recipe profile.

Use this project-local recipe analysis skill context as guidance:
{recipe_analysis_context}

Return strict JSON with these keys:
title, main_ingredients, cooking_methods, flavor_notes, intensity, acidity, sweetness, fat, spice, viscosity, oiliness, hardness.
Use plain ASCII punctuation only.

Allowed values:
intensity: light, medium, rich
acidity: low, medium, high
sweetness: low, medium, high
fat: low, medium, high
spice: none, mild, hot
viscosity: low, medium, high
oiliness: low, medium, high
hardness: low, medium, high

Recipe:
{recipe}
"""
