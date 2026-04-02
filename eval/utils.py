"""Utility helpers for the TwinBench scaffold."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any


def load_json(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: str | Path, payload: dict[str, Any]) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def utc_date() -> str:
    return datetime.now().date().isoformat()
