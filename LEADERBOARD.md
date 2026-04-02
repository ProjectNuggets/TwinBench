# TwinBench Leaderboard

TwinBench v1 is ready for external result submission. The canonical leaderboard structure is defined here even though no public external submissions are listed yet.

## Current Status

- Public external submissions: `none listed yet`
- Canonical benchmark version: `1.0`
- Example artifact: [results/reference-example-v1.json](results/reference-example-v1.json)

The example artifact is a schema and reporting reference, not a competitive leaderboard entry.

## Reporting Rules

- Every row must include the benchmark version used.
- Scenario deviations must be disclosed.
- Evidence references should be included whenever available.
- Coverage shortfalls must remain visible.
- Evaluator notes and caveats are part of the result, not optional extras.

## Leaderboard Template

| System Name | System Version | Evaluation Date | Benchmark Version | MR | IC | CCC | TC | PG | Total Score | Coverage | Evidence | Evaluator Notes | Caveats |
|-------------|----------------|-----------------|-------------------|----|----|-----|----|----|-------------|----------|----------|-----------------|---------|
| No public submissions yet | - | - | 1.0 | - | - | - | - | - | - | - | [Reference example](results/reference-example-v1.json) | Template row only | Not a leaderboard entry |

## Result Record Template

```json
{
  "benchmark_name": "TwinBench",
  "benchmark_title": "TwinBench: Benchmark for Persistent AI Systems",
  "benchmark_version": "1.0",
  "system_name": "Example System",
  "system_version": "0.1.0",
  "date_evaluated": "2026-04-03",
  "metrics": {
    "MR": {"score": 0.0},
    "IC": {"score": 0.0},
    "CCC": {"score": 0.0},
    "TC": {"score": 0.0},
    "PG": {"score": 0.0}
  },
  "total_score": 0.0,
  "scenario_coverage": 0.0,
  "metric_coverage": 0.0,
  "evidence": [],
  "evaluator_notes": [],
  "caveats": []
}
```
