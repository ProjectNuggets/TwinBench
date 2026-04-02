#!/usr/bin/env python3
"""Minimal TwinBench v1 evaluation scaffold."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from .scoring import build_metric_scores, total_score
    from .utils import load_json, utc_date, write_json
except ImportError:
    from scoring import build_metric_scores, total_score
    from utils import load_json, utc_date, write_json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="TwinBench v1 scaffold runner")
    parser.add_argument("--config", required=True, help="Path to benchmark config JSON")
    parser.add_argument("--system-name", required=True, help="System name under evaluation")
    parser.add_argument("--system-version", required=True, help="System version under evaluation")
    parser.add_argument("--scenario-dir", help="Optional override for scenario directory")
    parser.add_argument("--observations", help="Optional structured observations JSON")
    parser.add_argument("--output", required=True, help="Destination result JSON path")
    parser.add_argument("--date-evaluated", default=utc_date(), help="Evaluation date (YYYY-MM-DD)")
    return parser.parse_args()


def load_scenarios(config: dict, scenario_dir: str | None) -> list[dict]:
    scenario_paths = config.get("scenarios", [])
    scenarios = []

    for raw_path in scenario_paths:
        path = Path(raw_path)
        if scenario_dir:
            path = Path(scenario_dir) / path.name
        scenarios.append(load_json(path))

    return scenarios


def main() -> None:
    args = parse_args()
    config = load_json(args.config)
    scenarios = load_scenarios(config, args.scenario_dir)
    observations = load_json(args.observations) if args.observations else {}

    scenario_scores = observations.get("scenario_scores", {})
    metric_overrides = observations.get("metric_overrides", {})
    notes = observations.get("notes", [])
    metric_weights = config.get("metric_weights", {})
    metric_scores = build_metric_scores(metric_weights, scenario_scores, metric_overrides)
    scenario_coverage = round(
        sum(1 for scenario in scenarios if scenario["id"] in scenario_scores) / len(scenarios),
        3,
    ) if scenarios else 0.0
    metric_coverage = round(
        sum(1 for item in metric_scores.values() if item.get("score") is not None)
        / len(metric_scores),
        3,
    ) if metric_scores else 0.0

    payload = {
        "benchmark_name": config.get("benchmark_name", "TwinBench"),
        "benchmark_version": config.get("benchmark_version", "1.0"),
        "benchmark_subtitle": config.get("subtitle", "Benchmark for Persistent AI Systems"),
        "system_name": args.system_name,
        "system_version": args.system_version,
        "date_evaluated": args.date_evaluated,
        "scenarios": [
            {
                "id": scenario["id"],
                "title": scenario["title"],
                "primary_metrics": scenario.get("primary_metrics", []),
                "observed_score": scenario_scores.get(scenario["id"]),
            }
            for scenario in scenarios
        ],
        "metrics": metric_scores,
        "total_score": total_score(metric_scores),
        "scenario_coverage": scenario_coverage,
        "metric_coverage": metric_coverage,
        "notes": notes,
    }

    write_json(args.output, payload)


if __name__ == "__main__":
    main()
