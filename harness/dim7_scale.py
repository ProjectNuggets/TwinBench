"""Dimension 7: Scale & Cost Efficiency — concurrent load and resource usage."""

import time
import statistics
import concurrent.futures

from .config import BenchConfig
from .sse_client import chat, get_metrics, provision_user


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


def _run_concurrency_scenario(
    configs: list[BenchConfig], message_prefix: str
) -> tuple[list[float], int, float, list[str]]:
    """Run one concurrency scenario and return latencies, errors, wall time, and sample errors."""
    latencies: list[float] = []
    errors = 0
    error_samples: list[str] = []
    start_all = time.monotonic()

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(configs)) as pool:
        futures = []
        for i, cfg in enumerate(configs):
            futures.append(
                pool.submit(
                    _timed_chat,
                    cfg,
                    f"{message_prefix} {i}: what is {i}+{i}?",
                )
            )
        for f in concurrent.futures.as_completed(futures):
            r = f.result()
            if r["error"]:
                errors += 1
                if len(error_samples) < 3 and r["error"] not in error_samples:
                    error_samples.append(r["error"])
            else:
                latencies.append(r["latency_ms"])

    wall_time_ms = (time.monotonic() - start_all) * 1000
    return latencies, errors, wall_time_ms, error_samples


def _latency_stats(latencies: list[float]) -> dict:
    if not latencies:
        return {}
    ordered = sorted(latencies)
    return {
        "p50_ms": round(statistics.median(ordered), 1),
        "p95_ms": round(
            ordered[int(len(ordered) * 0.95)] if len(ordered) >= 5 else max(ordered),
            1,
        ),
        "p99_ms": round(
            ordered[int(len(ordered) * 0.99)] if len(ordered) >= 10 else max(ordered),
            1,
        ),
    }


def run(config: BenchConfig) -> dict:
    """Test scale in three modes:
    1) same-session contention (single user)
    2) multi-user parallel (one request per user)
    3) transport/pool metric snapshot
    """
    results = {}
    concurrency = config.scale_concurrency

    # Phase 1: Sequential baseline (3 requests)
    baseline_latencies = []
    baseline_errors: list[str] = []
    for i in range(3):
        r = _timed_chat(config, f"What is {i * 7} plus {i * 3}?")
        if r["error"] is None:
            baseline_latencies.append(r["latency_ms"])
        elif len(baseline_errors) < 3 and r["error"] not in baseline_errors:
            baseline_errors.append(r["error"])
        time.sleep(0.5)

    if baseline_latencies:
        results["baseline_p50_ms"] = round(statistics.median(baseline_latencies), 1)
    else:
        results["baseline_p50_ms"] = None
        results["baseline_error"] = "All baseline requests failed"
    if baseline_errors:
        results["baseline_error_samples"] = baseline_errors

    # Phase 2a: Same-user same-session contention (diagnostic only; not primary scale metric)
    same_session_cfgs = [config for _ in range(concurrency)]
    same_latencies, same_errors, same_wall_ms, same_error_samples = _run_concurrency_scenario(
        same_session_cfgs,
        "Same-session contention request",
    )
    same_stats = _latency_stats(same_latencies)
    results["same_session"] = {
        "requests": concurrency,
        "errors": same_errors,
        "success": len(same_latencies),
        "wall_time_ms": round(same_wall_ms, 1),
        "p50_ms": same_stats.get("p50_ms"),
        "p95_ms": same_stats.get("p95_ms"),
        "p99_ms": same_stats.get("p99_ms"),
        "error_samples": same_error_samples,
    }

    # Phase 2b: Multi-user parallel (primary scale metric)
    try:
        base_user_num = int(config.user_id)
        user_ids = [str(base_user_num + i) for i in range(concurrency)]
    except ValueError:
        user_ids = [f"{config.user_id}-bench-{i}" for i in range(concurrency)]
    candidate_cfgs = [config.clone_for_user(uid) for uid in user_ids]

    provisioned_cfgs: list[BenchConfig] = []
    provisioned_users: list[str] = []
    unavailable_users: list[str] = []
    provisioning_error_samples: list[str] = []
    for cfg in candidate_cfgs:
        provision_result = provision_user(cfg)
        if provision_result["ok"]:
            provisioned_cfgs.append(cfg)
            provisioned_users.append(cfg.user_id)
            continue

        reason = provision_result.get("reason") or "unknown"
        if reason == "unknown_user_id":
            unavailable_users.append(cfg.user_id)
        elif len(provisioning_error_samples) < 3:
            sample = (
                f"user={cfg.user_id} status={provision_result.get('status_code')} "
                f"reason={reason}"
            )
            if sample not in provisioning_error_samples:
                provisioning_error_samples.append(sample)

    results["multi_user_provisioning"] = {
        "requested_users": concurrency,
        "provisioned_users": len(provisioned_cfgs),
        "provisioned_user_ids": provisioned_users[:5],
        "unavailable_users": len(unavailable_users),
        "unavailable_user_ids": unavailable_users[:5],
        "error_samples": provisioning_error_samples,
    }

    if len(provisioned_cfgs) >= 2:
        multi_latencies, multi_errors, multi_wall_ms, multi_error_samples = _run_concurrency_scenario(
            provisioned_cfgs,
            "Multi-user concurrent request",
        )
        multi_stats = _latency_stats(multi_latencies)
        results["multi_user"] = {
            "requests": len(provisioned_cfgs),
            "errors": multi_errors,
            "success": len(multi_latencies),
            "wall_time_ms": round(multi_wall_ms, 1),
            "p50_ms": multi_stats.get("p50_ms"),
            "p95_ms": multi_stats.get("p95_ms"),
            "p99_ms": multi_stats.get("p99_ms"),
            "error_samples": multi_error_samples,
        }
        identity_bootstrap_available = True
    else:
        results["multi_user"] = {
            "requests": len(provisioned_cfgs),
            "errors": 0,
            "success": 0,
            "wall_time_ms": 0.0,
            "p50_ms": None,
            "p95_ms": None,
            "p99_ms": None,
            "error_samples": [],
        }
        identity_bootstrap_available = False
        results["note"] = (
            "Multi-user scale measurement unavailable: benchmark users could not be "
            "provisioned through /api/v1/users/provision on this runtime."
        )

    same_p95 = results["same_session"].get("p95_ms")
    multi_p95 = results["multi_user"].get("p95_ms")
    if same_p95 and multi_p95 and multi_p95 > 0:
        results["contention_ratio_same_session_over_multi_user"] = round(
            same_p95 / multi_p95, 2
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
    if not identity_bootstrap_available:
        results["score"] = 0.0
        results["verified_score"] = 0.0
        results["projected_score"] = 0.0
        results["measured_coverage"] = 0.0
        return {
            "dimension": "scale_cost",
            "score": results["score"],
            "verified_score": results["verified_score"],
            "projected_score": results["projected_score"],
            "measured_coverage": results["measured_coverage"],
            "status": "unavailable",
            "reason_code": "multi_user_bootstrap_unavailable",
            "details": results,
        }

    multi_requests = results["multi_user"]["requests"]
    multi_success_rate = len(multi_latencies) / multi_requests if multi_requests > 0 else 0
    multi_p95 = results["multi_user"].get("p95_ms") or 60000

    # Primary measured scale signal should use multi-user throughput, not same-session contention.
    multi_p95_score = max(0, 100 - (multi_p95 / 1000))  # 0ms = 100, 100s = 0
    verified_score = multi_p95_score * multi_success_rate

    # Projection still includes unmeasured dimensions.
    projected_score = (
        0.70 * 0.25  # inverse_rss: projected
        + (multi_p95_score / 100) * 0.20
        + 0.70 * 0.25  # max_users: projected
        + 0.80 * 0.20  # horizontal: projected
        + 0.60 * 0.10  # inverse_cost: projected
    ) * 100
    projected_score = projected_score * multi_success_rate

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
        "status": "partially_measured",
        "reason_code": "multi_user_scale_measured_with_provisioned_subset",
        "details": results,
    }
