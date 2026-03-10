"""Dimension 7: Scale & Cost Efficiency — concurrent load and resource usage."""

import time
import statistics
import concurrent.futures

from .config import BenchConfig
from .sse_client import chat, get_metrics


def _timed_chat(config: BenchConfig, message: str) -> dict:
    """Chat with timing, return result dict."""
    start = time.monotonic()
    r = chat(config, message)
    elapsed_ms = (time.monotonic() - start) * 1000
    return {
        "latency_ms": elapsed_ms,
        "error": r["error"],
        "tokens": r["tokens"],
        "content_length": len(r["content"]),
    }


def run(config: BenchConfig) -> dict:
    """Test scale under concurrent load."""
    results = {}
    concurrency = config.scale_concurrency

    # Phase 1: Sequential baseline (3 requests)
    baseline_latencies = []
    for i in range(3):
        r = _timed_chat(config, f"What is {i * 7} plus {i * 3}?")
        if r["error"] is None:
            baseline_latencies.append(r["latency_ms"])
        time.sleep(0.5)

    if baseline_latencies:
        results["baseline_p50_ms"] = round(statistics.median(baseline_latencies), 1)
    else:
        results["baseline_p50_ms"] = None
        results["baseline_error"] = "All baseline requests failed"

    # Phase 2: Concurrent load
    latencies = []
    errors = 0
    start_all = time.monotonic()

    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = []
        for i in range(concurrency):
            futures.append(
                pool.submit(
                    _timed_chat,
                    config,
                    f"Concurrent test request {i}: what is {i}+{i}?",
                )
            )
        for f in concurrent.futures.as_completed(futures):
            r = f.result()
            if r["error"]:
                errors += 1
            else:
                latencies.append(r["latency_ms"])

    wall_time_ms = (time.monotonic() - start_all) * 1000

    results["concurrent_requests"] = concurrency
    results["concurrent_errors"] = errors
    results["concurrent_success"] = len(latencies)
    results["wall_time_ms"] = round(wall_time_ms, 1)

    if latencies:
        latencies.sort()
        results["concurrent_p50_ms"] = round(statistics.median(latencies), 1)
        results["concurrent_p95_ms"] = (
            round(latencies[int(len(latencies) * 0.95)], 1)
            if len(latencies) >= 5
            else round(max(latencies), 1)
        )
        results["concurrent_p99_ms"] = (
            round(latencies[int(len(latencies) * 0.99)], 1)
            if len(latencies) >= 10
            else round(max(latencies), 1)
        )

    # Phase 3: Parse metrics for pool/transport stats
    metrics = get_metrics(config)
    if metrics:
        results["metrics_snapshot"] = {}
        for line in metrics.split("\n"):
            if line.startswith("nullalis_http_pool") or line.startswith(
                "nullalis_http_transport"
            ):
                parts = line.split(" ")
                if len(parts) >= 2:
                    results["metrics_snapshot"][parts[0]] = parts[1]

    # Score calculation
    success_rate = len(latencies) / concurrency if concurrency > 0 else 0
    p95 = results.get("concurrent_p95_ms", 60000)

    # inverse_rss (projected — can't measure from outside), inverse_p95, max_users, horizontal, inverse_cost
    p95_score = max(0, 100 - (p95 / 1000))  # 0ms = 100, 100s = 0
    success_score = success_rate * 100
    projected_score = (
        0.70 * 0.25  # inverse_rss: projected (2.6MB binary, ~43MB test RSS)
        + p95_score / 100 * 0.20
        + 0.70 * 0.25  # max_users: projected (~1000/instance)
        + 0.80 * 0.20  # horizontal: projected (tenant lock + Postgres)
        + 0.60 * 0.10  # inverse_cost: projected
    ) * 100

    # Adjust based on actual success rate
    projected_score = projected_score * success_rate
    verified_score = p95_score * success_rate

    results["score"] = round(min(100, projected_score), 1)
    results["verified_score"] = round(min(100, verified_score), 1)
    results["projected_score"] = round(min(100, projected_score), 1)
    results["measured_coverage"] = 0.2
    return {
        "dimension": "scale_cost",
        "score": results["score"],
        "verified_score": results["verified_score"],
        "projected_score": results["projected_score"],
        "measured_coverage": results["measured_coverage"],
        "details": results,
    }
