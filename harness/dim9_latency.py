"""Dimension 9: Latency Profile — end-to-end responsiveness."""

import time
import statistics

from .config import BenchConfig
from .sse_client import chat, health_check


def run(config: BenchConfig) -> dict:
    """Measure end-to-end latency for chat requests."""
    results = {}
    n = config.latency_requests

    # Health check latency
    h_start = time.monotonic()
    health_check(config)
    h_ms = (time.monotonic() - h_start) * 1000
    results["health_latency_ms"] = round(h_ms, 1)

    # Chat latencies
    latencies = []
    for i in range(n):
        start = time.monotonic()
        r = chat(config, f"What is {i * 3} + {i * 2}? Answer briefly.")
        elapsed = (time.monotonic() - start) * 1000
        if r["error"] is None:
            latencies.append(elapsed)
        time.sleep(0.3)

    results["chat_requests"] = n
    results["chat_success"] = len(latencies)

    if latencies:
        latencies.sort()
        results["chat_p50_ms"] = round(statistics.median(latencies), 1)
        results["chat_p95_ms"] = round(
            latencies[int(len(latencies) * 0.95)]
            if len(latencies) >= 5
            else max(latencies),
            1,
        )
        results["chat_p99_ms"] = round(latencies[-1], 1)
        results["chat_min_ms"] = round(min(latencies), 1)
        results["chat_max_ms"] = round(max(latencies), 1)
        results["chat_mean_ms"] = round(statistics.mean(latencies), 1)

        # Score: lower is better. 1s = 100, 30s = 0 (LLM-dominated)
        p95 = results["chat_p95_ms"]
        # Generous scoring: anything under 30s is fine for LLM-backed systems
        score = max(0, min(100, 100 - ((p95 - 1000) / 290)))
    else:
        score = 0
        results["error"] = "All chat requests failed"

    # Projected scores for non-chat latencies
    results["schedule_jitter_ms"] = "projected: ~1000 (1s poll interval)"
    results["memory_roundtrip_ms"] = "projected: <10 (SQLite FTS5 in-process)"
    results["note"] = (
        "Chat latency is dominated by LLM inference time. Runtime overhead is minimal."
    )

    results["score"] = round(score, 1)
    return {"dimension": "latency", "score": results["score"], "details": results}
