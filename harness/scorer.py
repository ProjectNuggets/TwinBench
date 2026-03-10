"""DTaaS-Bench composite score calculator."""

import math

WEIGHTS = {
    "autonomy_control": 0.15,
    "memory_persistence": 0.15,
    "functional_capability": 0.15,
    "autonomous_execution": 0.12,
    "cross_channel": 0.12,
    "integration_breadth": 0.08,
    "security_privacy": 0.08,
    "scale_cost": 0.05,
    "resilience": 0.05,
    "latency": 0.05,
}

DIMENSION_LABELS = {
    "autonomy_control": "Autonomy Control",
    "memory_persistence": "Memory Persistence",
    "functional_capability": "Functional Capability",
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
    if score >= 85:
        return "Category Leader"
    elif score >= 70:
        return "Production-Grade"
    elif score >= 55:
        return "Competitive"
    elif score >= 40:
        return "Emerging"
    elif score >= 25:
        return "Specialized"
    else:
        return "Early Stage"


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
