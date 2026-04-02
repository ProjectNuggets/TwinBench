# TwinBench

**TwinBench: Benchmark for Persistent AI Systems**

*Benchmarking Persistent AI and Digital Twin as a Service Systems*

TwinBench is an open benchmark for persistent AI systems. It evaluates whether a system remains coherent over time: whether it retains user-relevant memory, preserves identity, carries work forward across interruptions, transfers context across surfaces, and becomes more useful through durable personalization. Most current benchmarks evaluate models, tasks, or agents within a single session. TwinBench evaluates the systems layer required for persistent intelligence.

## Why This Benchmark Exists

Current evaluation practice usually answers one of three questions:

- Can a model solve a task?
- Can an agent complete a workflow?
- Can a system retrieve the right information in the current context?

Those are useful questions, but they do not fully answer a more important one for persistent systems:

**Does the system behave like a coherent intelligence over time rather than a sequence of isolated interactions?**

TwinBench exists to evaluate that missing layer.

## What TwinBench Measures

TwinBench v1 defines five core metrics:

- `MR` — Memory Retention
- `IC` — Identity Consistency
- `CCC` — Cross-Context Coherence
- `TC` — Task Continuity
- `PG` — Personalization Gain

Together, these metrics evaluate whether a system can sustain useful continuity across sessions, contexts, and repeated use.

## What TwinBench Does Not Measure

TwinBench is not intended to replace:

- model capability benchmarks
- agent-task completion benchmarks
- broad safety or security certifications
- product UX reviews
- production-scale infrastructure audits

TwinBench sits above model and task benchmarks. It focuses on persistent behavior that depends on system design, memory policy, orchestration, and runtime architecture.

## Who It Is For

- Engineers building persistent AI products, assistants, and runtimes
- Researchers studying longitudinal AI behavior
- Evaluators designing evidence-backed comparisons
- Teams that need a benchmark surface for continuity, persistence, and personalization

## Repository Map

```text
.
├── README.md
├── SPEC.md
├── METRICS.md
├── SCENARIOS.md
├── LEADERBOARD.md
├── benchmarks/
│   ├── configs/
│   ├── fixtures/
│   └── scenarios/
├── eval/
│   ├── runner.py
│   ├── scoring.py
│   └── utils.py
├── examples/
│   ├── minimal_example.md
│   └── sample_results.json
├── results/
│   ├── README.md
│   └── reference-example-v1.json
├── docs/
│   ├── methodology.md
│   └── submitting-results.md
└── legacy/
    ├── docs/
    ├── results/
    └── runtime/
```

The canonical TwinBench v1 surface is the root specification, the `benchmarks/` directory, the `eval/` scaffold, the `results/` example artifact, and the `docs/` methodology and submission notes. Earlier runtime-harness, website, and launch material are preserved in `legacy/`.

## Quickstart

Generate a blank result artifact from the v1 scaffold:

```bash
python3 eval/runner.py \
  --config benchmarks/configs/default.json \
  --system-name "Example System" \
  --system-version "0.1.0" \
  --output results/twinbench-empty-v1.json
```

Generate a scored example from the reference observations:

```bash
python3 eval/runner.py \
  --config benchmarks/configs/default.json \
  --system-name "Reference Example System" \
  --system-version "1.0.0" \
  --observations benchmarks/fixtures/reference_observations.json \
  --output results/reference-example-v1.json
```

The resulting schema is illustrated in [results/reference-example-v1.json](results/reference-example-v1.json).

## Example Result

The repository includes one benchmark-quality example artifact:

- [results/reference-example-v1.json](results/reference-example-v1.json)

This is a documented reference example for the v1 schema. It is not a public competitive submission and should not be treated as a leaderboard entry.

## Limitations

- v1 emphasizes clarity and reproducibility over maximal automation
- several judgments remain evaluator-assisted rather than fully automatic
- long-delay and multi-context evaluations remain sensitive to environment drift
- TwinBench can reveal persistence failures more reliably than it can explain their internal cause

Those limitations are discussed directly in [docs/methodology.md](docs/methodology.md).

## Submitting Results

TwinBench is ready for external result submission, but no public external submissions are listed yet in the canonical leaderboard template.

To prepare a result:

1. Run the benchmark scaffold or an equivalent evaluator against the v1 scenario set.
2. Produce a JSON artifact that matches the documented result schema.
3. Record caveats, evidence links, and any scenario deviations.
4. Add the result to the structure described in [LEADERBOARD.md](LEADERBOARD.md) and [docs/submitting-results.md](docs/submitting-results.md).

## Design Position

TwinBench is benchmark-first and vendor-neutral, but it is built around a systems claim: persistence is a systems property. Stronger prompting alone does not reliably produce durable memory, identity stability, context transfer, or long-horizon task continuity. Those behaviors usually depend on architecture, orchestration, and runtime design. That is why TwinBench is relevant to systems such as Nullalis and products such as ZAKI without becoming a product benchmark.
