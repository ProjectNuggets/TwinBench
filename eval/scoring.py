"""Scoring helpers for TwinBench v1."""

from __future__ import annotations

from typing import Any

METRIC_SCENARIO_MAP = {
    "MR": ["return_after_delay", "preference_learning", "identity_stability_over_time"],
    "IC": ["identity_stability_over_time", "multi_context_transfer"],
    "CCC": ["multi_context_transfer", "longitudinal_task_progression"],
    "TC": ["return_after_delay", "longitudinal_task_progression"],
    "PG": ["preference_learning"],
}


def clamp_score(value: float) -> float:
    return round(max(0.0, min(100.0, float(value))), 1)


def score_from_scenarios(metric: str, scenario_scores: dict[str, float]) -> float | None:
    scenario_ids = METRIC_SCENARIO_MAP.get(metric, [])
    matched = [float(scenario_scores[sid]) for sid in scenario_ids if sid in scenario_scores]
    if not matched:
        return None
    return clamp_score(sum(matched) / len(matched))


def build_metric_scores(
    weights: dict[str, float],
    scenario_scores: dict[str, float],
    metric_overrides: dict[str, Any] | None = None,
) -> dict[str, dict[str, Any]]:
    metric_overrides = metric_overrides or {}
    results: dict[str, dict[str, Any]] = {}

    for metric in weights:
        override = metric_overrides.get(metric)
        if override and "score" in override:
            score = clamp_score(override["score"])
            source = "override"
            note = override.get("note")
        else:
            derived = score_from_scenarios(metric, scenario_scores)
            score = derived if derived is not None else None
            source = "scenario_average" if derived is not None else "unscored"
            note = None

        results[metric] = {
            "score": score,
            "weight": float(weights[metric]),
            "source": source,
            "note": note,
        }

    return results


def total_score(metric_scores: dict[str, dict[str, Any]]) -> float | None:
    weighted = 0.0
    covered = 0.0

    for item in metric_scores.values():
        score = item.get("score")
        weight = float(item.get("weight", 0.0))
        if score is None:
            continue
        weighted += float(score) * weight
        covered += weight

    if covered == 0.0:
        return None
    return clamp_score(weighted / covered)
