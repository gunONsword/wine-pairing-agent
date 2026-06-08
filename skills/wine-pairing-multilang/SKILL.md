---
name: wine-pairing-multilang
description: Multilingual abstract-level knowledge base for food and wine pairing. Use when an AI agent needs general (non-recipe-specific) wine pairing principles, rules, food↔wine matching heuristics, or canonical pairing examples to recommend a wine for a dish, a dish for a wine, or to explain why a pairing works. Sources are abstract-to-abstract guides aggregated from French, Italian, Spanish, German and English-language wine education sites (Pattern 4). Use this skill when the user mentions "pairing", "accord mets-vins", "abbinamento cibo-vino", "maridaje", "Weinbegleitung", "wine pairing", "what wine with X", "what to eat with X", or asks for pairing rules/principles in the original language.
---

# Wine Pairing — Multilingual Abstract Knowledge Base

This skill consolidates abstract food↔wine pairing principles collected from Pattern 4 sources (abstract dish ↔ abstract wine) across five languages. Each section preserves the **original language** of the source so the agent can quote, translate, or reason with native terminology.

When an agent needs to:

- explain *why* a pairing works,
- pick a wine style for an unknown recipe,
- pick a dish family for a given wine style,
- pre-filter candidates before consulting a concrete (Pattern 1) recipe-to-wine database,

it should consult the **Universal Principles** section first, then drill into the language-specific section that best matches the cuisine origin (Italian cuisine → Italian section; Bordeaux → French section; Rioja/Iberian → Spanish section, etc.).

---

## 1. Universal Principles (synthesised across languages)

These principles appear in every source. They are the "first pass" any pairing decision should run.

### 1.1 Two core strategies

| Strategy | FR | IT | ES | EN |
|---|---|---|---|---|
| Similar / complementary | concordance / complémentarité | concordanza | concordancia / complementación | complementary / "like with like" |
| Contrast / opposition | contraste / contrapposition | contrapposizione / contrasto | contraste | contrast / "opposites attract" |

- **Concordance/Similarity** — match characteristics: rich+rich, sweet+sweet, herbaceous+herbaceous, regional+regional. Maximises and confirms the dominant flavour.
- **Contrast** — oppose characteristics so each balances the other: acidic wine cuts fat; sweet wine softens spicy heat; tannin cuts protein/fat.

### 1.2 The intensity / weight rule

- The intensity (weight, body) of the wine and the intensity of the dish must match.
- Light dish → light, low-alcohol, fresh, fruity wine.
- Heavy/rich dish → structured, full-bodied, possibly tannic or oaked wine.
- Stated in every source — this is the single most-cited rule.

### 1.3 The acidity rule

- The wine should usually have **at least as much acidity** as the dish, otherwise it tastes flat/washed out.
- High-acidity wines cleanse the palate against fat, cream, fried foods.

### 1.4 The sweetness rule

- For desserts: **the wine must be sweeter than the dessert**, otherwise the dessert strips the wine and it tastes bitter/sour.
- Dry sparkling (brut/extra brut) with sweet dessert = the most-warned-against mismatch.

### 1.5 The tannin rule

- Tannins bind to protein and fat → softer in the mouth.
- High-tannin reds want grilled red meat, game, mature cheese, succulent (high protein/fat) dishes.
- Avoid high tannin with delicate fish, light vegetables, very bitter foods (tannin amplifies bitterness).

### 1.6 The salt rule (Wine Enthusiast)

- Salt distorts oaky whites, strips fruit from reds, makes high-alcohol bitter.
- Two reliable rescues: (a) sweet wine + salty (Sauternes + blue cheese; Port + Stilton) ; (b) sparkling + salty fried (the bubbles + yeasty acid behave like beer and reset the palate).

### 1.7 The sauce / preparation rule

- Pair the wine to the **sauce and the cooking method**, not only to the protein.
- Same protein, different sauce → different wine (chicken roast vs. chicken curry vs. chicken cream sauce → three different wines).
- Grilled / smoked → wines with smoky or mineral notes.
- Braised / mijoté → fresh acidic wines that lift the dish.
- Boiled / delicate → light reds or crisp whites.

### 1.8 The terroir rule ("what grows together, goes together")

- Regional cuisine and regional wine almost always agree.
- Examples: Barolo + ossobuco / Pizzoccheri + Valtellina / Boeuf Bourguignon + Pinot Noir / Rioja + lamb / Chianti + Tuscan beef.

### 1.9 Service order (multi-wine meal)

- Light before heavy. Young before old. Fresh before tempered. Dry before sweet. White before red is *not* a rule per se — weight is.

### 1.10 The myths to discard

- ❌ "Red with meat, white with fish" — depends on cut/preparation (oily fish with red OK; chicken curry with white OK).
- ❌ "Rosé is a halfway compromise" — it is its own category with its own pairings.
- ❌ "Sparkling pairs with everything" — sparkling fails against very sweet desserts.

---

## 2. Français — Accords mets-vins

*Sources : elixirs-dexception.com, eccevino.com*

### 2.1 Principes
- Les accords mets et vins créent un équilibre lors d'un repas entre les plats et les vins servis ; vins et plats sont complémentaires.
- Servir les vins raffinés avec les plats raffinés et les vins simples avec les plats simples.
- Test d'un accord : goûter le vin, le plat, puis le vin. Un accord parfait quand aucun ne domine l'autre.

### 2.2 Méthodologie "deux astuces infaillibles" (eccevino)
- Identifier le **goût de base du plat** : aigre/acide, salé, sucré, piquant, gras, amer.
- Identifier le **goût de base de la boisson** : vin rouge → un peu amer ; vin doux → sucré ; rosé/mousseux → plus acides.
- Choisir : (a) **contraste** (goûts opposés — vin doux + plat acide ou piquant ; vin blanc acide + plat gras) ou (b) **concordance** (même goût — vin doux + plat sucré).

### 2.3 Vin Blanc

| Style | Plats |
|---|---|
| Vin blanc sec | Fromage de chèvre, volaille rôtie/grillée, poissons grillés à chair fondante, fruits de mer, crudités, salades d'été, guacamole, verrines à la crevette |
| Vin blanc doux | Foie gras, fromages à pâte persillée (Fourme d'Ambert, Bleu), plats exotiques aux douces épices, desserts |
| Vin blanc demi-sec | Foie gras, fromages à pâte persillée (entre sec et moelleux) |

#### Vin blanc & fromage
- Chèvre/brebis → demi-sec ou moelleux
- Pâte persillée → moelleux
- Pâte pressée → sec (Chardonnay, Sauvignon Blanc)
- Pâte molle croûte fleurie (Camembert, Brie) → sec
- Pâte molle croûte lavée (Munster, Maroilles) → sec très fruité aromatique ou demi-sec

#### Vin blanc & viande
- Veau → blanc gras (Chardonnay)
- Volaille blanche (dinde, chapon, poulet) → sec
- Volaille en sauce → blanc puissant
- Volaille à chair rouge (canard, pintade) → sec

#### Vin blanc & poisson
- Cabillaud, dorade → sec (Sauvignon Blanc) ou minéral/fumé
- Poisson gras (bar, saumon) → vin plus rond/gras (Chardonnay)
- Poisson en sauce → Chardonnay

#### Vin blanc & cuisine asiatique
- Poisson cru → sec
- Plats gras / canard / sucré-salé → vin orange (macération)

### 2.4 Vin Rouge

| Style | Plats |
|---|---|
| Vin rouge sec | Bœuf, veau grillé, porc, brochettes ; fromages (plus le vin est vieux, plus le fromage doit être mûr) ; tartelettes viande/foie/pâté en apéritif |
| Vin rouge tannique / corsé / charpenté | Canard, gibier, viandes au goût affirmé ; couscous, tajine, samoussas, kefta ; aligot, magret de canard, côte de bœuf ; nombreux fromages |
| Vin rouge léger | Volaille, viande blanche, poisson, légumes crus, plats à base de tomates, pâtes, pizzas, cuisine italienne ; tartes, barbecues, poulets rôtis ⚠ pas de viande rouge trop puissante |

#### Vin rouge & moments du repas
- Entrée : charcuterie / salade composée vinaigrée / thon, rouget
- Plat principal : viandes rouges, gratins, plats mijotés, volaille, tomates, pizza — **toujours un vin de la même puissance que l'accompagnement**
- Dessert : fromage (rouge léger) ; chocolat noir ≥75 % (les tanins du chocolat noir font écho aux tanins du vin)

### 2.5 Accords vins-viandes (eccevino)
- Viandes rouges (agneau, bœuf) → rouges (syrah, cabernet-sauvignon)
- Viandes blanches (veau, poulet) → blancs (chardonnay, chasselas)
- Rosés → composantes légères et relevées
- Menus épicés → vins aromatiques (syrah, merlot) — **exception** : plats asiatiques → bouquets moins prononcés et pétillants
- Viandes grillées → notes fumées/minérales (rioja, pinot noir)
- Saveurs intenses → corsés forts en alcool (primitivo, merlot)
- Viandes grasses → tanniques (contraste neutralise la lourdeur)

### 2.6 Mode de préparation
- Braisée (ragoût, rôti mijoté) → cépage frais à forte acidité, notes fruitées légères
- Feu vif (croûte, arômes puissants) → rouge tannique (chianti, barolo)
- Bouillie (saveurs délicates) → blanc ou rouge léger (riesling-sylvaner, gamay)

---

## 3. Italiano — Abbinamento cibo-vino

*Fonti: giordanovini.it, bitofwine.it, enotecaravazzani.com, buonissimo.it, italysfinestwines.it*

### 3.1 Principi fondamentali (enotecaravazzani)
- L'abbinamento si basa su **2 principi**: **concordanza** (caratteristiche simili → si confermano) e **contrapposizione** (caratteristiche opposte → si bilanciano).
- Bilanciare **grasso, acidità, dolcezza, consistenza** dei *cibi* con **alcolicità, tannini, acidità, dolcezza** dei *vini*.
- Regola di struttura: la struttura del vino deve corrispondere alla struttura del piatto.

### 3.2 Esempi di interazione
- Sauvignon Blanc (acidità marcata) ↔ piatti ricchi e grassi → pulisce il palato
- Riesling (dolcezza) ↔ piccante (curry thailandese) → mitiga
- Chardonnay barricato (vaniglia/burro) ↔ salse cremose (concordanza)
- Cabernet Sauvignon (alti tannini) ↔ bistecca alla griglia (tannini legano proteine/grassi)
- Pinot Noir (leggero, poco tannico) ↔ pollo, pesce delicato

### 3.3 Sei abbinamenti per contrasto (enotecaravazzani)
- **Piccante + Dolce**: gorgonzola piccante + vino passito
- **Sapido + Morbido**: frutti di mare, formaggi stagionati, affumicati + Chardonnay barricato o Merlot
- **Grasso + Acidità**: foie gras, fritti, formaggi cremosi + spumante metodo classico
- **Succulento + Tannico**: bistecca + Cabernet Sauvignon o Barolo
- **Amaro + Morbido**: verdure a foglia, carciofi, cioccolato fondente + Merlot o Chardonnay in barrique
- **Dolce + Dolce (concordanza)**: dolce della pasticceria + Moscato

### 3.4 Falsi miti sfatati
- ❌ "Carne = vino rosso" → pollo al curry (carne bianca speziata) → bianco poco alcolico, fresco, morbido
- ❌ "Pesce = vino bianco" → pesce spada alla pizzaiola (carne grassa + sughetto acido) → rosso morbido, non troppo alcolico
- ❌ "Formaggi = vino rosso" → tagliere misto fresco+stagionato → bianco passito (alcol+zucchero+rotondità abbinano entrambi)
- ❌ "Rosato = ibrido bianco/rosso" → ha tecnica e caratteristiche proprie
- ❌ "Bollicine vanno con tutto" → falso
- ❌ "Spumante brut con dolce" → l'acidità viene amplificata; usare Moscato

### 3.5 Piatti tipici italiani (giordanovini)

| Piatto | Caratteristiche | Vino |
|---|---|---|
| Insalata di riso classica | Pomodorini, olive, verdure, mais — sapori delicati | Bianco secco con punta di acidità (Pecorino Terre di Chieti IGT) |
| Insalata di riso con tonno | Sapidità del mare | Vermentino di Gallura DOCG (minerale, fruttato, floreale) |
| Pasta al pesto | Erbaceo, sapido, retrogusto di pinoli | Bianco giovane fresco con toni erbacei (Fiano Puglia IGT, Vermentino) |
| Spaghetti allo scoglio | Cozze, vongole, gamberi, scampi | Pinot Grigio Delle Venezie DOC oppure rosato pugliese |
| Risotto allo zafferano | Aroma intenso, retrogusto amarognolo | Rosato leggero aromatico oppure Prosecco/spumante |
| Pasta alla Norma | Melanzane, ricotta, pomodoro, basilico | Nero d'Avola Sicilia DOC oppure Grillo bianco siciliano |

### 3.6 Quando il vino è giovane/fresco vs strutturato
- Estate, ricette leggere: vini **giovani, freschi, leggeri, aromatici ma poco corposi**.
- Selvaggina, brasati, arrosti: vini **strutturati, tannici, evoluti**.

### 3.7 Riferimenti regionali (buonissimo, italysfinestwines)
- Barbaresco (Piemonte) ↔ arrosti, selvaggina, agnello, brasati
- Montepulciano d'Abruzzo ↔ pasta asciutta, carni grigliate, arrosti
- Verdicchio dei Castelli di Jesi ↔ pesce
- Nobile di Montepulciano ↔ selvaggina (cinghiale, faraona, anatra), Pici al ragù, Chianina, Cinta Senese, Pecorino di Pienza

---

## 4. Español — Maridaje

*Fuentes: kommen.es, bodeboca.com, estudiahosteleria.com, vinoseleccion.com, mulecarajonero.com*

### 4.1 Principios fundamentales
- El maridaje es el arte de crear armonías perfectas entre el vino y la comida — una danza donde cada elemento complementa y realza al otro.
- La clave: **equilibrio entre la intensidad del vino y la del plato**.
- Dos enfoques: **complementación** (sabores que se complementan) o **contraste** (sabores opuestos que se equilibran).

### 4.2 Elementos clave del vino
- **Acidez**: vinos ácidos limpian el paladar con platos grasos/cremosos
- **Cuerpo**: peso/consistencia debe equilibrarse con la del plato
- **Taninos**: tintos — interacción ideal con proteínas de carnes

### 4.3 Cinco reglas de oro (bodeboca)
1. La comida y el vino deben tener la misma intensidad
2. El vino debe tener siempre mayor acidez que la comida
3. Vino tánico → platos con grasa
4. Postre dulce → vino aún más dulce
5. La clave está en el tipo de salsa de la receta

### 4.4 Análisis del plato (bodeboca - preguntas guía)
- ¿Dulce, salado, ácido, amargo, umami?
- ¿Graso o ligero?
- ¿Salsa picante/especiada/herbácea/cremosa/afrutada?
- ¿Ahumado, encurtido, en salazón?
- ¿Horno, parrilla, plancha?

### 4.5 Vinos Blancos

| Estilo | Platos |
|---|---|
| Blanco seco (Riesling seco, Chardonnay, Sauvignon Blanc) | Pescados/mariscos con limón o salsas ligeras; ensaladas con tomate o vinagreta de limón |
| Blanco afrutado (Gewürztraminer, Riesling semi-seco) | Cocina asiática (curry tailandés, rollitos), platos especiados/picantes; quesos frescos (cabra, brie) |
| Blanco passito | Tablas mixtas de queso (fresco + curado) |

### 4.6 Vinos Tintos

| Estilo | Platos |
|---|---|
| Tinto ligero (Pinot Noir, Gamay) | Aves de corral (pato, pollo asado); Sauerbraten |
| Tinto robusto (Cabernet Sauvignon, Syrah, Tempranillo) | Carnes rojas, codillo, quesos curados (manchego, cheddar añejo); platos especiados |

### 4.7 Vinos Dulces (Tokaji, Sauternes, Eiswein)
- Postres: foie gras, tarta de manzana caramelizada (Sauternes); postres helados, tartas de frutas (Eiswein)
- Contraste: queso azul, curry picante (Tokaji)

### 4.8 Maridajes estrella (bodeboca)
- **Champagne** + pollo frito Kentucky / ostras / caviar / marisco / jamón ibérico / salsas cremosas
- **Riesling** + cerdo ibérico asado (contraste — corta la grasa)
- **Albariño** + ceviche de vieira (congruente — frescura, salinidad, herbáceo)
- **Pinot Noir** + salmón al horno / a la plancha / ahumado
- **Syrah** + hamburguesas a la parrilla (tanino + grasa; ahumado + ahumado)
- **Manzanilla** + gamba blanca / olivas / almendras / jamón ibérico
- **Sauvignon Blanc** + ensalada Caprese
- **Sangiovese** + berenjena parmesana

### 4.9 Maridaje regional (principio "lo que crece junto, va junto")
- Pasta con trufa blanca de Alba + Barbaresco (Piamonte)
- Boeuf Bourguignon + Pinot Noir (Borgoña)
- Chuletillas de cordero al sarmiento + Rioja Gran Reserva

### 4.10 Platos calientes españoles (estudiahosteleria)

| Plato | Vino |
|---|---|
| Cocido madrileño | Cava o champán brut/brut nature ; o tinto joven, fresco, afrutado con crianza breve |
| Sopas/pescado ligero | Manzanilla de Sanlúcar ; blancos secos (macabeo, viura, verdejo) |
| Guisos con caza | Tintos carnosos afrutados sin mucha crianza (Garnacha, Tempranillo de Rioja/La Mancha/Madrid) |
| Cordero + setas | Tintos con crianza o media crianza (Mencía del Bierzo, Garnachas castellanas, Baboso Negro del Hierro) |

### 4.11 Maridaje de vino con pasta (vinoseleccion)
*Lo que importa es la salsa, no el tipo de pasta.*

| Salsa | Vino |
|---|---|
| Tomate | Chianti, Sangiovese ; Tempranillo (Ribera del Duero, Rioja) |
| Almejas (spaghetti alle vongole) | Pinot Grigio ligero |
| Pesto | Vermentino |
| Queso | Prosecco o Cava (limpia el paladar) |
| Setas | Pinot Noir del Alto Adige ; Mencía (notas terrosas + umami) |

### 4.12 Orden de servicio (mulecarajonero)
- Blanco joven → blanco crianza → rosado → tinto joven → tinto envejecido

---

## 5. Deutsch — Weinbegleitung (sintesi multilingue)

*Riferimenti: contenuti adattati da kommen.es e dalla cultura tedesca delle "Weinbegleitung".*

- **Riesling seco alemán** — blanco seco con notas cítricas, alta acidez; ideal para pescado, marisco, ensaladas con limón.
- **Gewürztraminer** — semi-seco aromático; cocina asiática picante, queso fresco.
- **Riesling semi-seco / Eiswein** — postres dulces, queso azul (contraste con dulzura).
- **Spätburgunder** (Pinot Noir alemán) — aves de corral, asados marinados (Sauerbraten), salmón.
- **Sekt** (espumoso alemán) — apéritifs, ostras, fritos.
- **Codillo alemán (Schweinshaxe)** — tinto robusto (Cabernet, Syrah, Tempranillo).

---

## 6. English — Wine Pairing Fundamentals

*Sources: wineenthusiast.com, laithwaites.co.uk, melaniemay.com, cellarbeastwine.com*

### 6.1 The Six Elements (Wine Enthusiast)

#### Fat
- Wine has no fat → balance with **acid**, cut with **tannin**, or match richness with **alcohol**.
- Classic: prime steak + Cabernet (fat softens tannins, releases fruit notes).

#### Acid
- For acidic dishes: the wine's perceived acidity must be ≥ the food's.
- Salads: moderate dressing acid; pair with herbaceous SB or Sémillon.

#### Salt
- Salt distorts oaky Chardonnay, strips fruit from reds, makes high alcohol bitter.
- Rescues: sweet wine + salty (Sauternes + blue cheese) ; sparkling + salty fried; acidic wine + oysters.

#### Sweetness
- Light sweetness (fruit sauce over pork) → rich whites (Chardonnay) — high alcohol reads as sweetness.
- Desserts: wine **must be sweeter than the dessert**.
- Red + chocolate: only bitter dark + slightly sweet red (late-harvest Zinfandel). Never sweet chocolate dessert + dry red.

#### Bitterness
- Avoid in most cuisines. Bitter wine + bitter food do not cancel — they compound.

#### Texture
- Safe: light with light, heavy with heavy.
- Adventurous: contrast (light food + heavy wine) — requires testing.

### 6.2 Nine fundamentals (Laithwaites)
1. **Balance** — similar weight/body
2. **Alcohol level** — never high-alcohol wine with spicy food (intensifies heat)
3. **Acidity** — wine more acidic than the meal
4. **Like with like** — savoury+savoury, sweet+sweet, earthy+earthy
5. **Opposites attract** — sweet white balances spicy heat
6. **Wine sweeter than the food**
7. **Sauce guides the wine** — citrus sauce → SB; cream/mushroom → Chardonnay; peppercorn → Shiraz
8. **Cooking methods matter** — grill/BBQ → smoky/mineral wines; poached/steamed → crisp, bright, simple
9. **"What grows together, goes together"** — regional pairings

### 6.3 Cellar Beast pro-tips
- Match wine body to dish body.
- Pair wine to the **sauce or most pungent flavour** on the plate, not just the protein.

### 6.4 Sparkling pairing (melaniemay)
- Pet Nat / natural sparkling — funky cheese, sourdough, fermented foods, lentils, mushrooms; chilled but not icy.
- Sparkling wine, picked in the right style, pairs with almost anything (except very sweet desserts).

### 6.5 Classic English-language pairings

| Wine | Dish |
|---|---|
| Sauvignon Blanc | Sea bass; New Zealand SB + avocado/tomato/spinach crepes; Sémillon for tangy salads |
| Burgundy red (Pinot Noir) | Duck breast with caramelised apples; salmon with dill (oily fish + light tannic red) |
| Cabernet Sauvignon | Steak (Napa Cab + slow-cooked rack of lamb) |
| Chardonnay | Roast chicken (Australian Chardonnay + chicken sate burger; California SB + wild mushroom soup) |
| Sangiovese / Chianti | Pizza, pepperoni |
| Zinfandel | BBQ — ribs, sausages, bacon cheeseburger |
| Champagne (Brut) | Oysters, caviar, fish & chips, fried foods, chicken liver pâté |
| Riesling | Cucumber soup; spicy Asian dishes |
| Prosecco | Summer melon + prosciutto |
| Tavel/Bandol Rosé | Tomato salad, tuna baguette |
| Beaujolais | Lamb shanks with olives |
| Albariño | Chicken and mushroom paella |
| Vermentino | Pesto pasta |
| Greco di Tufo | Spaghetti with cockles |
| Mencía | Spicy grilled shrimp stew |
| Vouvray | Chicken tostadas |
| Soave | Crispy artichokes |
| Agiorgitiko | Moussaka |
| Saint-Joseph | Lamb with apricots |

---

## 7. Cross-language decision shortcut (for the agent)

Given an unfamiliar dish, the agent can build a candidate wine style by walking these axes:

1. **Body** (light → full) — match to the dish's heaviness.
2. **Acidity** (low → high) — at least as high as the dish (esp. tomato, vinaigrette, citrus, raw fish).
3. **Tannin** (low → high) — raise with red meat, protein, fat; lower with delicate proteins.
4. **Sweetness** (dry → sweet) — raise to meet the dish's sweetness; raise to soften spice/heat.
5. **Alcohol** (low → high) — lower for spicy; higher for rich braises.
6. **Aroma profile** — pick **concordance** (mirror dominant flavour) or **contrast** (balance dominant flavour).
7. **Region** — when in doubt, regional cuisine + regional wine is rarely wrong.

Then the agent can output either:
- a **wine style** (e.g. "young, fresh, low-alcohol white with high acidity, citrus profile"), to query a concrete wine database, **OR**
- a **named example** from sections 2–6.

---

## 8. Source attribution

| Language | Pattern 4 sources used |
|---|---|
| Français | elixirs-dexception.com (Guide accords ; Vin blanc ; Vin rouge) ; eccevino.com (Accords vins-viandes ; Deux astuces infaillibles) |
| Italiano | giordanovini.it (Primi piatti estivi) ; bitofwine.it (15 consigli) ; enotecaravazzani.com (Segreti dell'abbinamento ; Regole ed errori) ; buonissimo.it (Abbinamenti) ; italysfinestwines.it (Nobile di Montepulciano) |
| Español | kommen.es (Guía maridaje) ; bodeboca.com (Secretos y claves del maridaje) ; estudiahosteleria.com (Platos calientes) ; vinoseleccion.com (Maridaje vino-pasta) ; mulecarajonero.com (Recetas y maridajes) |
| English | wineenthusiast.com (Mastering the Art) ; laithwaites.co.uk (Pairing For Beginners) ; melaniemay.com (Sparkling) ; cellarbeastwine.com (Wine Pairing Guide) |

All extracts above are abstract-to-abstract (Pattern 4) general principles, not concrete recipe-to-bottle pairings.
