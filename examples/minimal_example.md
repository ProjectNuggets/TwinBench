# Minimal TwinBench Example

This scaffold is intentionally lightweight. It does two things:

1. loads the v1 benchmark configuration and scenario set
2. produces a structured results artifact from supplied observations

Generate a blank-ish result scaffold:

```bash
python3 eval/runner.py \
  --config benchmarks/configs/default.json \
  --system-name "Example System" \
  --system-version "0.1.0" \
  --output results/twinbench-v1-example.json
```

Generate a scored example from fixture observations:

```bash
python3 eval/runner.py \
  --config benchmarks/configs/default.json \
  --system-name "Example System" \
  --system-version "0.1.0" \
  --observations benchmarks/fixtures/sample_observations.json \
  --output results/twinbench-v1-scored.json
```

The resulting artifact is compatible with the template in [LEADERBOARD.md](../LEADERBOARD.md).
