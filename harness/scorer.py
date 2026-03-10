"""DTaaS-Bench composite score calculator."""

import math

WEIGHTS = {
    "autonomy_control": 0.20,
    "memory_persistence": 0.20,
    "autonomous_execution": 0.15,
    "cross_channel": 0.15,
    "integration_breadth": 0.10,
    "security_privacy": 0.08,
    "scale_cost": 0.05,
    "resilience": 0.05,
    "latency": 0.02,
}

DIMENSION_LABELS = {
    "autonomy_control": "Autonomy Control",
    "memory_persistence": "Memory Persistence",
    "autonomous_execution": "Autonomous Execution",
    "cross_channel": "Cross-Channel Consistency",
    "integration_breadth": "Integration Breadth",
    "security_privacy": "Security & Privacy",
    "scale_cost": "Scale & Cost Efficiency",
    "resilience": "Operational Resilience",
    "latency": "Latency Profile",
}


def composite_score(dimension_scores: dict[str, float]) -> float:
    """Calculate weighted composite score (0-100)."""
    total = 0.0
    for dim, weight in WEIGHTS.items():
        score = dimension_scores.get(dim, 0.0)
        total += score * weight
    return round(total, 1)


def rating_tier(score: float) -> str:
    if score >= 90:
        return "SOTA"
    elif score >= 75:
        return "Production-Ready"
    elif score >= 60:
        return "Beta"
    elif score >= 40:
        return "Prototype"
    else:
        return "Experimental"


def log2_breadth_score(
    channels: int, tools: int, backends: int, integrations: int
) -> float:
    """Logarithmic breadth scoring to reward breadth without over-indexing on count."""
    raw = (
        math.log2(max(channels, 1)) * 0.30
        + math.log2(max(tools, 1)) * 0.30
        + math.log2(max(backends, 1)) * 0.20
        + math.log2(max(integrations, 1)) * 0.20
    )
    # Normalize: log2(17)*0.3 + log2(34)*0.3 + log2(9)*0.2 + log2(4)*0.2 ~ 3.7 is near-max
    max_theoretical = 4.0
    return min(100.0, (raw / max_theoretical) * 100)
