# Recipe To Wine Search Profile

Use this module to turn a recipe into wine-search criteria.

## Recipe Tags To Extract

Extract these recipe tags before recommending wine:

- `main_ingredients`: protein, vegetables, starches, cheese, legumes.
- `cooking_methods`: grilled, roasted, fried, braised, steamed, raw, smoked.
- `sauce_base`: cream, butter, tomato, soy, vinegar, citrus, chili oil, curry, stock.
- `flavor_intensity`: light, medium, rich.
- `acidity`: low, medium, high.
- `sweetness`: low, medium, high.
- `fat`: low, medium, high.
- `spice_heat`: none, mild, medium, hot.
- `umami`: low, medium, high.
- `texture`: delicate, firm, crispy, creamy, fatty.
- `aromatics`: herbs, pepper, smoke, earth, floral, citrus, tropical, dried fruit.

## Wine Search Fields

Output these fields for future wine-list matching:

```json
{
  "recommended_grapes": [],
  "recommended_origins": [],
  "recommended_regions": [],
  "required_style_tags": {
    "acidity": "",
    "body": "",
    "tannin": "",
    "sweetness": "",
    "oak": "",
    "alcohol": "",
    "fruit_profile": [],
    "aromatic_profile": []
  },
  "avoid_style_tags": [],
  "pairing_reason": ""
}
```

## Grape And Region Guidelines

- Spicy food: Riesling, Gewurztraminer, Chenin Blanc, off-dry sparkling. Search Mosel, Rheingau, Alsace, Vouvray, Clare Valley.
- Fatty fish or butter sauces: Chardonnay, Pinot Gris, Champagne. Search Burgundy, Sonoma Coast, Margaret River, Champagne.
- Tomato or high-acid sauces: Sangiovese, Barbera, Chianti, Etna Rosso, Sauvignon Blanc. Search Tuscany, Piedmont, Sicily, Sancerre.
- Red meat or braised dishes: Syrah, Cabernet Sauvignon, Nebbiolo, Tempranillo. Search Northern Rhone, Barossa, Bordeaux, Rioja, Barolo.
- Earthy mushrooms or duck: Pinot Noir, Gamay, Nebbiolo. Search Burgundy, Oregon, Beaujolais, Langhe.
- Fresh herbs and green vegetables: Sauvignon Blanc, Gruner Veltliner, Vermentino. Search Sancerre, Marlborough, Wachau, Sardinia.

Always explain why the recommended grape and region fit the recipe tags.

