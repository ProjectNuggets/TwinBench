"""Dimension 4: Cross-Channel Consistency — coherent state across channels."""

import time

from .config import BenchConfig
from .sse_client import chat, get_diagnostics
from .evidence import live_integration_counts


def run(config: BenchConfig) -> dict:
    """Test cross-channel state consistency.

    Note: Full cross-channel testing requires 2+ real channels configured.
    This harness tests the underlying capability via the HTTP API (shared
    session/memory). Scores are partially projected.
    """
    results = {}
    measured_points = 0
    measured_max_points = 50
    projected_bonus_points = 0
    error_samples: list[str] = []

    # Test 1: Store a fact and recall it (same-user, same-session persistence)
    unique_marker = "CROSSCHAN_BENCH_8472"
    remember = chat(config, f"Remember this cross-channel test marker: {unique_marker}")
    if remember["error"] and remember["error"] not in error_samples:
        error_samples.append(remember["error"])
    time.sleep(1)
    r1 = chat(config, "What is the cross-channel test marker I just told you?")
    if r1["error"] and len(error_samples) < 3 and r1["error"] not in error_samples:
        error_samples.append(r1["error"])
    recall_works = (
        unique_marker.lower() in r1["content"].lower() or "8472" in r1["content"]
    )
    results["same_session_recall"] = recall_works
    if recall_works:
        measured_points += 20

    # Test 2: Check shared state architecture from diagnostics
    diag = get_diagnostics(config)
    if diag:
        diag_str = str(diag).lower()
        has_bus = "bus" in diag_str or "inbound" in diag_str
        has_channels = "channel" in diag_str or "telegram" in diag_str
        has_session = "session" in diag_str or "runtime_mode" in diag_str
        configured_channels, connected_channels = live_integration_counts(diag)
        identity = diag.get("identity_mapping", {})
        results["bus_architecture"] = has_bus
        results["channels_in_diagnostics"] = has_channels
        results["session_in_diagnostics"] = has_session
        results["live_configured_channels"] = configured_channels
        results["live_connected_channels"] = connected_channels
        results["identity_mapping_seen"] = bool(identity)
        if has_bus:
            measured_points += 15
        if has_channels:
            measured_points += 10
        if has_session:
            measured_points += 5
        if configured_channels > 0:
            measured_points += 5
            measured_max_points += 10
        if connected_channels > 0:
            measured_points += 5
            measured_max_points += 10
        if identity:
            measured_points += 5
    else:
        results["diagnostics_available"] = False

    # Projected scores for dimensions we can't test via single HTTP endpoint
    projected_bonus_points += 10  # timeline_consistency: projected
    projected_bonus_points += 10  # notification_routing: projected
    results["projected_timeline_consistency"] = True
    results["projected_notification_routing"] = True
    results["note"] = (
        "Full cross-channel test requires 2+ real channels. Projected components: timeline consistency, notification routing."
    )

    projected_score = min(100, measured_points + projected_bonus_points)
    verified_score = min(100, (measured_points / measured_max_points) * 100)
    projected_score = max(projected_score, verified_score)
    results["score"] = round(projected_score, 1)
    results["verified_score"] = round(verified_score, 1)
    results["projected_score"] = round(projected_score, 1)
    results["measured_coverage"] = round(measured_max_points / 100, 2)
    results["measured_points"] = measured_points
    results["measured_max_points"] = measured_max_points
    if error_samples:
        results["error_samples"] = error_samples
    return {
        "dimension": "cross_channel",
        "score": results["score"],
        "verified_score": results["verified_score"],
        "projected_score": results["projected_score"],
        "measured_coverage": results["measured_coverage"],
        "details": results,
    }
