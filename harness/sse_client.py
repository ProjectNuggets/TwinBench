"""SSE chat client for DTaaS runtimes."""

import json
import time
import requests

from .config import BenchConfig


def chat(config: BenchConfig, message: str, timeout: int | None = None) -> dict:
    """Send a message via SSE chat endpoint and collect the full response.

    Returns:
        {
            "content": str,         # full concatenated response text
            "session_id": str,      # from done event
            "message_id": str,      # from done event
            "latency_ms": float,    # wall-clock time
            "error": str | None,    # error message if failed
            "tokens": int,          # number of token events received
        }
    """
    timeout = timeout or config.timeout
    start = time.monotonic()

    result = {
        "content": "",
        "session_id": "",
        "message_id": "",
        "latency_ms": 0.0,
        "error": None,
        "tokens": 0,
    }

    try:
        resp = requests.post(
            config.chat_url(),
            headers=config.headers,
            json={"message": message},
            stream=True,
            timeout=timeout,
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        result["error"] = str(e)
        result["latency_ms"] = (time.monotonic() - start) * 1000
        return result

    content_parts = []
    current_event = None

    try:
        for line in resp.iter_lines(decode_unicode=True):
            if line is None:
                continue
            line = line.strip()

            if line.startswith("event:"):
                current_event = line[6:].strip()
                continue

            if line.startswith("data:"):
                data_str = line[5:].strip()
                if not data_str:
                    continue

                try:
                    data = json.loads(data_str)
                except json.JSONDecodeError:
                    continue

                if current_event == "token":
                    delta = data.get("delta", "")
                    if delta:
                        content_parts.append(delta)
                    result["tokens"] += 1

                elif current_event == "status":
                    # Status events may contain content
                    content = data.get("content", "")
                    if content and data.get("type") == "statusResponse":
                        content_parts.append(content)

                elif current_event == "error":
                    result["error"] = data.get(
                        "content", data.get("message", "unknown error")
                    )

                elif current_event == "done":
                    result["session_id"] = data.get("session_id", "")
                    result["message_id"] = data.get("message_id", "")
                    break

                current_event = None

    except Exception as e:
        result["error"] = f"SSE parse error: {e}"

    result["content"] = "".join(content_parts)
    result["latency_ms"] = (time.monotonic() - start) * 1000
    return result


def health_check(config: BenchConfig) -> bool:
    """Return True if /health returns 200."""
    try:
        r = requests.get(config.health_url(), timeout=5)
        return r.status_code == 200
    except requests.RequestException:
        return False


def get_diagnostics(config: BenchConfig) -> dict | None:
    """Fetch /internal/diagnostics JSON."""
    try:
        r = requests.get(
            config.diagnostics_url(),
            headers=config.headers,
            timeout=10,
        )
        if r.status_code == 200:
            return r.json()
    except (requests.RequestException, json.JSONDecodeError):
        pass
    return None


def get_metrics(config: BenchConfig) -> str | None:
    """Fetch /metrics text."""
    try:
        r = requests.get(config.metrics_url(), timeout=10)
        if r.status_code == 200:
            return r.text
    except requests.RequestException:
        pass
    return None
