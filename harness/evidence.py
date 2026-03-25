"""Helpers for parsing benchmark evidence from chat responses and diagnostics."""

import json


def extract_json_object(text: str) -> dict | None:
    """Extract the first top-level JSON object from free-form text."""
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return None
    try:
        payload = json.loads(text[start : end + 1])
    except json.JSONDecodeError:
        return None
    return payload if isinstance(payload, dict) else None


def used_tool(response: dict, tool_name: str) -> bool:
    """Return True if progress events show the named tool was invoked."""
    for event in response.get("progress_events", []):
        if event.get("phase") == "tool" and event.get("tool") == tool_name:
            return True
    return False


def live_integration_counts(diag: dict | None) -> tuple[int, int]:
    """Return (configured_count, connected_count) from diagnostics.integrations."""
    if not isinstance(diag, dict):
        return 0, 0
    integrations = diag.get("integrations")
    if not isinstance(integrations, dict):
        return 0, 0

    configured = 0
    connected = 0
    for value in integrations.values():
        if not isinstance(value, dict):
            continue
        if value.get("configured") is True:
            configured += 1
        if value.get("connected") is True:
            connected += 1
    return configured, connected


def as_int(value, default: int = 0) -> int:
    """Best-effort integer coercion."""
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return default
    return default
