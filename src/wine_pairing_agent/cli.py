from __future__ import annotations

import argparse
from pathlib import Path

from wine_pairing_agent.graph import recommend_wine


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Recommend wine for a recipe with pairing reasons.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--recipe", help="Recipe text or short dish description.")
    source.add_argument("--file", type=Path, help="Path to a text file containing the recipe.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    recipe = args.recipe if args.recipe else args.file.read_text(encoding="utf-8")
    print(recommend_wine(recipe))


if __name__ == "__main__":
    main()

