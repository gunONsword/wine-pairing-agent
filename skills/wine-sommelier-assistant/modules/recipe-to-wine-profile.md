# Recipe To Wine Search Profile

Use this module to turn recipe-analysis results into wine-list search criteria.

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
- `viscosity`: low, medium, high. Use high for thick sauces, stews, sticky glazes, dense purees, or creamy reductions.
- `oiliness`: low, medium, high. Use high for fried, oily, greasy, or oil-coated dishes.
- `hardness`: low, medium, high. Use high for firm, chewy, dense, or hard-textured foods.
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
  "wine_list_matches": [],
  "pairing_reason": ""
}
```

If a wine list is provided, use the wine search fields to rank real wines from that list. Do not stop at abstract grape or region recommendations when specific wine-list items are available.

## Grape And Region Guidelines

- Spicy food: Riesling, Gewurztraminer, Chenin Blanc, off-dry sparkling. Search Mosel, Rheingau, Alsace, Vouvray, Clare Valley.
- Fatty fish or butter sauces: Chardonnay, Pinot Gris, Champagne. Search Burgundy, Sonoma Coast, Margaret River, Champagne.
- Oily or fried dishes: Champagne, Cava, Franciacorta, high-acid sparkling. Use bubbles and acidity to cut oiliness.
- Thick or viscous sauces: Chardonnay, Viognier, Pinot Gris, or fuller whites when body and texture need matching.
- Hard or chewy textures: structured reds such as Syrah, Cabernet Sauvignon, Nebbiolo, or Tempranillo when protein and intensity support tannin.
- Tomato or high-acid sauces: Sangiovese, Barbera, Chianti, Etna Rosso, Sauvignon Blanc. Search Tuscany, Piedmont, Sicily, Sancerre.
- Red meat or braised dishes: Syrah, Cabernet Sauvignon, Nebbiolo, Tempranillo. Search Northern Rhone, Barossa, Bordeaux, Rioja, Barolo.
- Earthy mushrooms or duck: Pinot Noir, Gamay, Nebbiolo. Search Burgundy, Oregon, Beaujolais, Langhe.
- Fresh herbs and green vegetables: Sauvignon Blanc, Gruner Veltliner, Vermentino. Search Sancerre, Marlborough, Wachau, Sardinia.

Always explain why the recommended grape and region fit the recipe tags.
