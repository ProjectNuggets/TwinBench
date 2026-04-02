# TwinBench Specification

**Formal title:** `TwinBench: Benchmark for Persistent AI Systems`  
**Version:** `1.0`  
**Status:** `Canonical public specification`

## 1. Scope

TwinBench specifies a benchmark for evaluating persistent AI systems. Its purpose is to measure whether a system preserves useful continuity over time rather than performing well only within isolated sessions.

The benchmark covers systems that claim durable user memory, longitudinal task handling, identity stability, cross-context transfer, or personalization that improves with use.

## 2. Benchmark Object of Evaluation

The TwinBench object of evaluation is a system instance, not a model in isolation.

The evaluated object may include:

- foundation models
- memory services
- orchestration logic
- tool and channel adapters
- scheduling systems
- identity or profile layers
- retrieval and storage infrastructure

TwinBench evaluates the externally observable behavior of that full stack.

## 3. Position Relative to Other Benchmark Types

TwinBench is distinct from two common benchmark families:

- `Model benchmarks` measure model competence, often with fixed prompts and single-run scoring.
- `Agent-task benchmarks` measure task completion within a bounded workflow or episode.

TwinBench measures a third layer:

- `Persistent intelligence benchmarks` measure whether the system remains coherent, useful, and identity-consistent across time, context changes, and repeated use.

TwinBench therefore should not be interpreted as a replacement for model or agent benchmarks. It complements them by measuring what they usually leave untested.

## 4. Assumptions

TwinBench v1 assumes that the evaluated system:

- can be engaged across multiple sessions or checkpoints
- can access or simulate durable state across those checkpoints
- exposes enough behavioral evidence for evaluators to inspect continuity claims
- can be tested with fixed scenario definitions and recorded dates

TwinBench does not assume any particular model family, API design, storage system, or product form factor.

## 5. Exclusions

TwinBench v1 does not directly attempt to measure:

- frontier reasoning capability in isolation
- enterprise security certification
- benchmark-resistant social behavior
- production cost efficiency at large scale
- broad product quality outside persistence
- general intelligence claims

These areas may matter for deployment, but they are outside the benchmark scope of v1.

## 6. Core Metrics

TwinBench v1 defines five metrics:

- `MR` — Memory Retention
- `IC` — Identity Consistency
- `CCC` — Cross-Context Coherence
- `TC` — Task Continuity
- `PG` — Personalization Gain

Metric definitions are normative in [METRICS.md](METRICS.md).

## 7. Scoring Philosophy

TwinBench favors interpretable scoring over aggressive aggregation.

The v1 default scoring profile:

- scores each metric on a `0-100` scale
- uses equal metric weighting
- reports scenario coverage
- reports metric coverage
- requires caveats and evaluator notes alongside scores

TwinBench prefers explicit partial coverage to hidden extrapolation. If a system is only partially observed, the result should show that directly rather than imply complete evidence.

## 8. Reproducibility Philosophy

TwinBench treats reproducibility as a graded property, not an absolute.

The benchmark is designed to improve reproducibility through:

- fixed scenario definitions
- explicit metric formulas
- dated evaluation artifacts
- disclosed caveats
- stable result schema

At the same time, persistent-system evaluation remains sensitive to environmental drift, delayed checkpoints, interface changes, and evaluator interpretation. v1 therefore requires transparent reporting instead of pretending full determinism where it does not exist.

## 9. Evaluation Lifecycle

TwinBench v1 defines a minimal but stable public surface:

- one canonical specification
- five core metrics
- five reference scenarios
- a lightweight evaluation scaffold
- a public result template
- one reference example artifact

Later versions may add:

- stronger delayed-checkpoint controls
- richer evidence requirements
- evaluator agreement procedures
- contradiction-resolution scenarios
- multi-user persistence scenarios

## 10. Versioning Policy

TwinBench uses benchmark-level versioning.

- `Patch` changes may clarify wording, examples, or non-normative guidance.
- `Minor` changes may add optional scenarios or tooling without breaking result comparability.
- `Major` changes are required when metric definitions, scoring rules, or normative scenario behavior change in ways that break comparability.

The canonical benchmark version must always be recorded in published results.

## 11. Reporting Requirements

A valid TwinBench result should include at minimum:

- benchmark name
- benchmark version
- system name
- system version
- evaluation date
- scenario-level observations
- per-metric scores
- total score
- coverage values
- evaluator notes
- caveats
- evidence references, if available

## 12. Interpretation Guidance

TwinBench scores are evidence about persistent-system behavior. They are not universal rankings of intelligence, safety, or product quality.

High TwinBench scores suggest that a system behaves more like a coherent persistent intelligence layer. They do not establish superiority outside the benchmark scope.

## 13. Architectural Thesis

TwinBench is vendor-neutral, but it is grounded in a clear systems thesis: persistence is not reducible to prompting. Durable continuity usually depends on runtime architecture, state management, orchestration, and identity handling. This makes TwinBench especially relevant to persistent AI runtimes while keeping the benchmark independent of any single implementation.
