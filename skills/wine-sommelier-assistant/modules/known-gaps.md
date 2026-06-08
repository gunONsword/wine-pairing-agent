# Known Gaps

This project does not require a separate research workflow for normal use.

Current gaps are engineering and data gaps:

1. No real wine-list database is connected yet.
2. Wine-list matching currently depends on structured tags being available.
3. Recipe analysis is text-based; image or scanned recipe parsing is not implemented.
4. Pairing scoring is rule-guided and LLM-assisted, not calibrated against a human-rated dataset.
5. User preferences such as budget, color preference, country preference, and inventory are not yet persisted.

These gaps should be solved by adding tools, data, memory, and evaluation tests rather than by adding a mandatory research step.

