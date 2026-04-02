# TwinBench Methodology Notes

## What TwinBench Measures Well

TwinBench is strongest when the question is whether a system behaves like a persistent intelligence layer over time. In v1, it measures well:

- delayed recall of user-relevant facts and preferences
- continuity of multi-step work across interruptions
- stability of user identity and system role
- transfer of task state across contexts
- practical gains from remembered preferences

These are the behavioral properties most often missing from model-only and task-only benchmarks.

## What TwinBench Does Not Yet Measure Well

TwinBench v1 is intentionally narrower than a full system audit. It does not yet measure well:

- adversarial robustness and security depth
- production reliability under sustained scale
- infrastructure cost efficiency
- open-domain capability breadth
- emotional or social interaction quality
- multi-user persistence under heavy contention

## Where Evaluator Judgment Is Required

Evaluator judgment remains necessary in several places:

- deciding whether a resumed task is genuinely coherent or merely plausible
- separating stylistic variation from identity drift
- deciding whether later improvement is true personalization gain or prompt luck
- judging whether omitted context is harmless compression or a continuity failure

TwinBench v1 treats that subjectivity honestly. Results should report notes and caveats instead of pretending complete automation where it does not exist.

## Reproducibility Limits

Persistent-system evaluation is less deterministic than single-turn task evaluation because:

- elapsed time affects system state
- deployments change between checkpoints
- context transfer may depend on product instrumentation
- preference-learning scenarios depend on task comparability
- some systems expose internal state while others expose only outputs

TwinBench addresses these limits through fixed scenario definitions, stable metric formulas, explicit dates, and artifact-based reporting. It does not fully eliminate drift.

## What “Good Enough v1” Means

TwinBench v1 is considered good enough if it does four things reliably:

1. defines the persistence layer as a benchmarkable object
2. gives evaluators a stable vocabulary and result schema
3. makes partial coverage and caveats explicit
4. supports comparable example runs without overstating certainty

That is a stronger and more trustworthy v1 than a more automated benchmark that hides uncertainty.

## Why the Systems Thesis Matters

TwinBench is benchmark-first and vendor-neutral, but its methodology reflects a clear technical position: persistence is a systems property. Durable memory, identity stability, context transfer, and long-horizon continuity usually depend on architecture and runtime design, not only on prompt quality. This is why persistent runtimes matter to the benchmark without making the benchmark product-specific.
