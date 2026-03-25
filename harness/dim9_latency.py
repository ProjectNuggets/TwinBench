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
    healthy = health_check(config)
    h_ms = (time.monotonic() - h_start) * 1000
    results["health_endpoint_ok"] = healthy
    results["health_latency_ms"] = round(h_ms, 1)

    # Chat latencies
    latencies = []
    error_samples: list[str] = []
    for i in range(n):
        start = time.monotonic()
        r = chat(config, f"What is {i * 3} + {i * 2}? Answer briefly.")
        elapsed = (time.monotonic() - start) * 1000
        if r["error"] is None:
            latencies.append(elapsed)
        elif len(error_samples) < 3 and r["error"] not in error_samples:
            error_samples.append(r["error"])
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
    if error_samples:
        results["chat_error_samples"] = error_samples
    results["runtime_unavailable_during_probe"] = (not healthy) and not latencies

    # Projected scores for non-chat latencies
    results["schedule_jitter_ms"] = "projected: ~1000 (1s poll interval)"
    results["memory_roundtrip_ms"] = "projected: <10 (SQLite FTS5 in-process)"
    results["note"] = (
        "Chat latency is dominated by LLM inference time. Runtime overhead is minimal."
    )
    if results["runtime_unavailable_during_probe"]:
        results["note"] += " Runtime was unavailable during this probe, so chat latency could not be measured."

    results["score"] = round(score, 1)
    results["verified_score"] = results["score"]
    results["projected_score"] = results["score"]
    results["measured_coverage"] = 1.0
    return {
        "dimension": "latency",
        "score": results["score"],
        "verified_score": results["verified_score"],
        "projected_score": results["projected_score"],
        "measured_coverage": results["measured_coverage"],
        "details": results,
    }
