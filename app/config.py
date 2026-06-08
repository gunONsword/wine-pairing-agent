from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_dotenv(path: Path | None = None) -> None:
    """Load simple KEY=VALUE pairs without adding a dotenv dependency."""
    env_path = path or PROJECT_ROOT / ".env"
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


@dataclass(frozen=True)
class Settings:
    minimax_api_key: str
    minimax_base_url: str = "https://api.minimax.io/v1"
    minimax_model: str = "MiniMax-M3"


def get_settings() -> Settings:
    load_dotenv()
    api_key = os.getenv("MINIMAX_API_KEY", "")
    if not api_key:
        raise RuntimeError("MINIMAX_API_KEY is required. Put it in .env or set it in the shell.")

    return Settings(
        minimax_api_key=api_key,
        minimax_base_url=os.getenv("MINIMAX_BASE_URL", "https://api.minimax.io/v1"),
        minimax_model=os.getenv("MINIMAX_MODEL", "MiniMax-M3"),
    )

