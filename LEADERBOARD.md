# TwinBench Leaderboard

This file is the public template for reported TwinBench results. It is intentionally plain. Benchmark repositories should optimize for comparability, not presentation.

## Reporting Rules

- Benchmark version must be stated explicitly.
- Scenario deviations must be disclosed in `Notes / Caveats`.
- Partial runs may be listed, but incomplete coverage should be made visible.
- Scores are reported on a `0-100` scale.

## Leaderboard Template

| System Name | Version | Date Evaluated | MR | IC | CCC | TC | PG | Total Score | Notes / Caveats |
|-------------|---------|----------------|----|----|-----|----|----|-------------|-----------------|
| Example System | 0.1.0 | 2026-04-03 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | Template row |

## Result Record Template

```json
{
  "benchmark_name": "TwinBench",
  "benchmark_version": "1.0",
  "system_name": "Example System",
  "system_version": "0.1.0",
  "date_evaluated": "2026-04-03",
  "metrics": {
    "MR": 0.0,
    "IC": 0.0,
    "CCC": 0.0,
    "TC": 0.0,
    "PG": 0.0
  },
  "total_score": 0.0,
  "scenario_coverage": 0.0,
  "metric_coverage": 0.0,
  "notes": [
    "List scenario deviations, evaluator caveats, or partial coverage here."
  ]
}
```
