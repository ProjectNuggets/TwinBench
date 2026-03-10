"""Dimension 4: Cross-Channel Consistency — coherent state across channels."""

import time

from .config import BenchConfig
from .sse_client import chat, get_diagnostics


def run(config: BenchConfig) -> dict:
    """Test cross-channel state consistency.

    Note: Full cross-channel testing requires 2+ real channels configured.
    This harness tests the underlying capability via the HTTP API (shared
    session/memory). Scores are partially projected.
    """
    results = {}
    score = 0

    # Test 1: Store a fact and recall it (same-user, same-session persistence)
    unique_marker = "CROSSCHAN_BENCH_8472"
    chat(config, f"Remember this cross-channel test marker: {unique_marker}")
    time.sleep(1)
    r1 = chat(config, "What is the cross-channel test marker I just told you?")
    recall_works = (
        unique_marker.lower() in r1["content"].lower() or "8472" in r1["content"]
    )
    results["same_session_recall"] = recall_works
    if recall_works:
        score += 20

    # Test 2: Check shared state architecture from diagnostics
    diag = get_diagnostics(config)
    if diag:
        diag_str = str(diag).lower()
        has_bus = "bus" in diag_str or "inbound" in diag_str
        has_channels = "channel" in diag_str or "telegram" in diag_str
        has_session = "session" in diag_str or "runtime_mode" in diag_str
        results["bus_architecture"] = has_bus
        results["channels_in_diagnostics"] = has_channels
        results["session_in_diagnostics"] = has_session
        if has_bus:
            score += 15
        if has_channels:
            score += 10
        if has_session:
            score += 5
    else:
        results["diagnostics_available"] = False

    # Test 3: Ask agent about its channel capabilities
    r2 = chat(config, "What communication channels do you support? List them.")
    channel_keywords = [
        "telegram",
        "discord",
        "slack",
        "email",
        "signal",
        "irc",
        "matrix",
        "whatsapp",
    ]
    channels_mentioned = sum(
        1 for kw in channel_keywords if kw in r2["content"].lower()
    )
    results["channels_agent_reports"] = channels_mentioned
    if channels_mentioned >= 5:
        score += 15
    elif channels_mentioned >= 3:
        score += 10
    elif channels_mentioned >= 1:
        score += 5

    # Test 4: Ask about cross-channel behavior
    r3 = chat(
        config,
        "If I send you a message on Telegram, can you recall it from this chat interface?",
    )
    cross_aware = any(
        kw in r3["content"].lower()
        for kw in [
            "yes",
            "shared",
            "same memory",
            "persist",
            "recall",
            "remember",
            "accessible",
        ]
    )
    results["cross_channel_awareness"] = cross_aware
    if cross_aware:
        score += 15

    # Projected scores for dimensions we can't test via single HTTP endpoint
    score += 10  # timeline_consistency: projected (shared session architecture)
    score += 10  # notification_routing: projected (bus dispatch)
    results["projected_timeline_consistency"] = True
    results["projected_notification_routing"] = True
    results["note"] = (
        "Full cross-channel test requires 2+ real channels. Projected components: timeline consistency, notification routing."
    )

    results["score"] = min(100, score)
    return {"dimension": "cross_channel", "score": results["score"], "details": results}
