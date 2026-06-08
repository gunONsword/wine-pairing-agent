# Wine List Matching Schema

This schema is for future matching against a restaurant or retail wine list.

## Wine List Fields

Expected wine-list tags:

```json
{
  "wine_id": "",
  "name": "",
  "producer": "",
  "vintage": "",
  "grape_varieties": [],
  "country": "",
  "region": "",
  "appellation": "",
  "color": "white|red|rose|orange|sparkling|fortified",
  "style_tags": {
    "acidity": "low|medium|high",
    "body": "light|medium|full",
    "tannin": "low|medium|high",
    "sweetness": "dry|off-dry|medium-sweet|sweet",
    "oak": "none|light|medium|heavy",
    "alcohol": "low|medium|high"
  },
  "aroma_tags": [],
  "price": null,
  "availability": ""
}
```

## Matching Priority

When matching recipe-derived criteria to a wine list:

1. Filter by hard conflicts first, such as high tannin with hot spice.
2. Match required style tags: acidity, body, sweetness, tannin.
3. Match grape varieties.
4. Match region and appellation.
5. Match aromatic bridge.
6. Use price or availability only after pairing fit.

## Output For Future Search

Return search criteria like:

```json
{
  "must_have": {
    "acidity": ["high"],
    "tannin": ["low", "medium"]
  },
  "preferred_grapes": ["Riesling"],
  "preferred_regions": ["Mosel", "Rheingau", "Clare Valley"],
  "avoid": {
    "tannin": ["high"],
    "oak": ["heavy"]
  },
  "ranking_notes": []
}
```

