# TwinBench

**TwinBench — Benchmarking Persistent AI and Digital Twin as a Service Systems**

TwinBench is an open benchmark for persistent AI systems. It evaluates whether a system behaves coherently over time: retaining memory across sessions, preserving identity, carrying work forward, transferring context across surfaces, and improving through user-specific knowledge. Existing benchmarks are useful for model quality, task completion, and agent execution, but they mostly evaluate single-session behavior. TwinBench measures the missing layer: whether an AI system functions as a persistent intelligence system rather than a sequence of isolated runs.

## Why TwinBench Exists

Current benchmarks tend to answer one of three questions:

- Can a model solve a task?
- Can an agent complete a workflow?
- Can a system retrieve the right fact in the current session?

They usually do not answer a harder systems question:

**Does the system remain coherent, useful, and identifiable across time, context shifts, and repeated interaction?**

TwinBench exists to evaluate that question directly.

## What TwinBench Measures

TwinBench v1 focuses on five benchmark dimensions:

- `MR` — Memory Retention
- `IC` — Identity Consistency
- `CCC` — Cross-Context Coherence
- `TC` — Task Continuity
- `PG` — Personalization Gain

These dimensions are designed to test persistent behavior, not just one-turn correctness.

## Who It Is For

- Researchers studying persistent or longitudinal AI behavior
- Builders of AI assistants, memory systems, and agent runtimes
- Infrastructure teams designing persistent intelligence architectures
- Evaluators who need a reproducible benchmark above model-only or task-only tests

## Benchmark Thesis

Persistence is not a prompt feature. It is a systems property. A benchmark for persistent intelligence therefore has to evaluate memory policy, identity stability, state transfer, longitudinal task handling, and user-specific adaptation together. This is why TwinBench is relevant to systems such as Nullalis while remaining benchmark-first and vendor-neutral.

## Repository Map

```text
.
├── README.md
├── SPEC.md
├── METRICS.md
├── SCENARIOS.md
├── LEADERBOARD.md
├── benchmarks/
│   ├── scenarios/
│   ├── fixtures/
│   └── configs/
├── eval/
│   ├── runner.py
│   ├── scoring.py
│   └── utils.py
├── examples/
│   ├── minimal_example.md
│   └── sample_results.json
├── docs/
│   └── methodology.md
└── harness/
    └── ...
```

`harness/` contains earlier implementation work and legacy runtime-facing evaluation code. The benchmark-standard v1 surface is defined by the top-level documents and the `benchmarks/` and `eval/` directories.

## Quick Start

Create a baseline result artifact from the v1 scaffold:

```bash
python3 eval/runner.py \
  --config benchmarks/configs/default.json \
  --system-name "Example System" \
  --system-version "0.1.0" \
  --output results/twinbench-v1-example.json
```

Score a run from structured observations:

```bash
python3 eval/runner.py \
  --config benchmarks/configs/default.json \
  --system-name "Example System" \
  --system-version "0.1.0" \
  --observations benchmarks/fixtures/sample_observations.json \
  --output results/twinbench-v1-scored.json
```

## Roadmap

- Publish v1 metric definitions and reference scenarios
- Add reference implementations for delayed and multi-session execution
- Expand scoring guidance for human-in-the-loop and partially observable systems
- Add reproducibility fixtures for multi-channel and longitudinal evaluations
- Open public submissions and a filled leaderboard

## Limitations

- v1 emphasizes benchmark shape and metric rigor over full automation
- Some persistence behaviors still require evaluator judgment or partial annotation
- Long-horizon evaluations remain sensitive to environment drift and product updates
- Cross-channel and personalization tests are easier to specify than to verify perfectly

These limitations are documented explicitly in [docs/methodology.md](docs/methodology.md).

## Contributing

TwinBench is intended to become a benchmark category, not a closed internal scorecard. Contributions are welcome in four forms:

- scenario proposals
- scoring critiques
- reproducibility improvements
- result submissions with evidence and caveats

Please read [SPEC.md](SPEC.md), [METRICS.md](METRICS.md), and [SCENARIOS.md](SCENARIOS.md) before proposing benchmark changes.
