# TwinBench Methodology Notes

## What TwinBench Measures Well

TwinBench is strongest when evaluating whether a system behaves like a persistent intelligence layer over repeated interaction. In particular, it measures:

- retention of user-relevant information after delay
- continuity of task state across sessions
- stability of identity and role framing
- transfer of context across surfaces or interaction modes
- practical gains from remembered preferences

These are behavioral properties that many model and agent benchmarks leave under-specified.

## What TwinBench Does Not Measure Well Yet

TwinBench v1 does not yet provide strong coverage for:

- adversarial security testing
- large-scale operational reliability
- economic efficiency under production traffic
- open-domain capability breadth
- emotional or relational quality
- multi-user contention in shared environments

Those areas may matter for deployment, but they are not the focus of the initial benchmark.

## Why Some Scoring Is Approximate

Several TwinBench metrics require interpretation rather than binary checking. Examples include whether a resumed task is meaningfully coherent, whether role drift is substantive, and whether later outputs represent genuine personalization gain rather than chance alignment.

For that reason, v1 allows evaluator notes, partial evidence, and scenario-level caveats. This is a feature, not a defect. False precision would make the benchmark look stronger than it is.

## Reproducibility Limits

Persistent-system evaluation is harder to reproduce than single-turn task evaluation because:

- behavior changes over elapsed time
- product updates may alter memory policy between checkpoints
- context transfer can depend on channel instrumentation
- personalization tests are sensitive to task selection
- some systems expose partial state while others hide it behind interfaces

TwinBench addresses this by publishing reference scenarios, dated result artifacts, and explicit caveat reporting. It does not eliminate the problem entirely.

## Why Architecture Matters

TwinBench is intentionally agnostic about implementation, but the benchmark is built around a systems claim: persistence depends on architecture. Durable memory, identity stability, context transfer, and long-horizon task handling usually require runtime support, not just stronger prompting. This is one reason the benchmark is relevant to persistent AI runtimes such as Nullalis without being tied to any single product.

## Future Work

Likely v2 directions include:

- stronger delay-window controls
- reference annotation protocols for evaluator agreement
- benchmark packs for channel transfer and contradiction handling
- improved scoring for partially automated systems
- richer fixture sets for user preference and identity drift
