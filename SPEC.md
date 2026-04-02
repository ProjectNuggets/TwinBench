# TwinBench Specification v1

## Status

- Name: `TwinBench`
- Formal label: `TwinBench: Benchmark for Persistent AI Systems`
- Version: `v1.0`
- Status: `Initial public specification`

## 1. Scope

TwinBench specifies a benchmark for evaluating persistent AI systems: systems expected to retain user-relevant information, preserve behavioral identity, continue work over time, transfer context across surfaces, and improve through accumulated personalization.

The benchmark does not attempt to replace model benchmarks, agent-task benchmarks, or safety benchmarks. It sits above them and evaluates the persistence layer that those benchmarks usually leave unmeasured.

## 2. Benchmark Philosophy

TwinBench is based on five principles:

1. Persistence is a systems property, not a single-prompt property.
2. Longitudinal utility matters more than isolated peak performance.
3. Identity and continuity should be evaluated behaviorally, not assumed from architecture.
4. Evidence and caveats should be reported together.
5. Partial measurement is preferable to inflated certainty.

This philosophy intentionally favors benchmark outputs that are legible, reproducible, and falsifiable over outputs that appear more precise than the underlying evidence allows.

## 3. Evaluation Target

TwinBench evaluates a system instance that claims some form of persistent intelligence. Examples include:

- personal AI systems
- long-lived assistants
- agent runtimes with durable memory
- digital twin style user representations
- multi-surface assistants with continuity expectations

The evaluation target may include model components, memory infrastructure, orchestration logic, scheduling systems, identity layers, and channel adapters. TwinBench evaluates the observable system behavior produced by that stack.

## 4. Assumptions

TwinBench v1 assumes the evaluated system:

- can be interacted with across multiple sessions
- can access or simulate durable state across those sessions
- exposes enough surface behavior for evaluators to inspect outputs over time
- can be evaluated with fixed prompts, structured fixtures, and dated checkpoints

TwinBench does not assume a specific model family, memory backend, agent framework, or product form factor.

## 5. Exclusions

TwinBench v1 does not directly measure:

- frontier model capability in isolation
- raw reasoning depth absent persistence requirements
- enterprise security certification
- economic efficiency at production scale
- subjective companionship quality
- broad social alignment claims

Those may matter in practice, but they are out of scope for the initial benchmark.

## 6. Scoring Philosophy

TwinBench v1 reports five core metrics:

- `MR` — Memory Retention
- `IC` — Identity Consistency
- `CCC` — Cross-Context Coherence
- `TC` — Task Continuity
- `PG` — Personalization Gain

The default v1 scoring profile assigns equal weight to each metric. This is a deliberate choice. At this stage, the benchmark aims to establish a clean and interpretable baseline rather than encode strong priors about which persistence property should dominate the others.

Scores should be reported with:

- metric-level values
- total score
- scenario coverage
- evaluator notes
- caveats

TwinBench prefers explicit incompleteness over hidden extrapolation. If a metric is only partially observed, that should be stated plainly.

## 7. Benchmark Lifecycle

### v1

TwinBench v1 defines:

- five core metrics
- five reference scenarios
- a lightweight scoring scaffold
- a public results template
- methodological caveats

### Future Expansion

Later versions may add:

- delayed evaluation windows with stronger temporal controls
- channel-specific transfer tests
- richer contradiction handling
- longitudinal multi-user benchmarks
- system architecture disclosures for reproducibility
- confidence intervals or evaluator agreement tracking

Future versions should preserve comparability where possible. Breaking metric definitions should require a new benchmark version.

## 8. Reporting Requirements

A TwinBench result should include at minimum:

- system name
- system version
- evaluation date
- benchmark version
- scenario set used
- metric scores
- total score
- notes on evaluator interpretation
- known limitations or caveats

Results without caveats should be treated skeptically.

## 9. Interpretation Guidance

TwinBench scores should be interpreted as evidence about persistent system behavior, not as a universal quality ranking.

High scores suggest the system behaves more like a persistent intelligence layer. They do not imply the system is safer in all contexts, more general across all tasks, or better than another system outside the benchmark scope.

## 10. Positioning

TwinBench is designed to make persistent AI legible as a benchmarkable systems category. That includes architectures in which persistence depends on memory services, identity representations, orchestration runtimes, and long-horizon state management rather than on prompting alone. This framing is intentionally compatible with systems such as Nullalis without making TwinBench a product-specific benchmark.
