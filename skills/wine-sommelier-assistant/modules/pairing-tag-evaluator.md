# Pairing Tag Evaluator

Use this module when both recipe tags and wine tags are available.

## Inputs

Recipe tags:

```json
{
  "intensity": "light|medium|rich",
  "acidity": "low|medium|high",
  "sweetness": "low|medium|high",
  "fat": "low|medium|high",
  "spice_heat": "none|mild|medium|hot",
  "umami": "low|medium|high",
  "aromatics": []
}
```

Wine tags:

```json
{
  "grape": "",
  "origin": "",
  "region": "",
  "acidity": "low|medium|high",
  "body": "light|medium|full",
  "tannin": "low|medium|high",
  "sweetness": "dry|off-dry|medium-sweet|sweet",
  "oak": "none|light|medium|heavy",
  "alcohol": "low|medium|high",
  "fruit_profile": [],
  "aromatic_profile": []
}
```

## Scoring

Start from 70 and adjust:

- Add 10-15 when wine acidity balances recipe fat, fried texture, cream, tomato, vinegar, or citrus.
- Add 8-12 when wine body matches recipe intensity.
- Add 8-12 when wine sweetness or fruit intensity softens spice heat.
- Add 5-10 when aromatics bridge the dish, such as herbs with Sauvignon Blanc or pepper with Syrah.
- Subtract 10-20 when high tannin meets chili heat, delicate fish, high acidity, or bitter vegetables.
- Subtract 8-15 when wine is too light for rich food or too heavy for delicate food.
- Subtract 8-15 when heavy oak clashes with spice, delicate seafood, or subtle herbs.

## Verdict

- 90-100: excellent
- 80-89: good
- 65-79: acceptable
- 50-64: risky
- 0-49: poor

## Required Response

Return:

```json
{
  "pairing_score": 0,
  "verdict": "",
  "matches": [],
  "conflicts": [],
  "adjustments": [],
  "better_alternatives": []
}
```

