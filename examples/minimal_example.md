# Minimal TwinBench Example

The v1 scaffold is intentionally small. It loads the canonical configuration, applies structured observations, and emits a stable JSON result artifact.

Generate an empty result shell:

```bash
python3 eval/runner.py \
  --config benchmarks/configs/default.json \
  --system-name "Example System" \
  --system-version "0.1.0" \
  --output results/twinbench-empty-v1.json
```

Generate the canonical reference example:

```bash
python3 eval/runner.py \
  --config benchmarks/configs/default.json \
  --system-name "Reference Example System" \
  --system-version "1.0.0" \
  --observations benchmarks/fixtures/reference_observations.json \
  --output results/reference-example-v1.json
```

The output schema is aligned with [LEADERBOARD.md](../LEADERBOARD.md) and the example artifact in [results/reference-example-v1.json](../results/reference-example-v1.json).
