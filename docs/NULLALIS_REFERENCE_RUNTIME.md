# Nullalis as the Reference Runtime

DTaaS-Bench exists to define a category that most current AI assistant benchmarks do not measure well.

Nullalis is the first reference runtime in this repository because it appears to implement the full runtime shape DTaaS-Bench is trying to capture:

- durable memory and per-user state
- autonomous scheduling and heartbeat execution
- background-turn guardrails
- multi-channel runtime plumbing
- diagnostics, metrics, and deployment surfaces
- production-oriented runtime operations

## What "Reference Runtime" Means

Nullalis is the benchmark's reference runtime, not the benchmark's judge.

That means:

- Nullalis is the first featured artifact in the repo
- Nullalis helps demonstrate that the category is real
- Nullalis provides examples of what high-evidence runtime capabilities look like
- Nullalis does not get private scoring rules or leaderboard favoritism

The benchmark should remain usable by competing systems on equal terms.

## Why Nullalis Is a Strong Category Example

Based on the current runtime and local evidence pack, Nullalis provides strong support for the DTaaS thesis in several areas:

- `Autonomy Control`: turn origins, background policy, and proactive dedupe surfaces exist
- `Memory Persistence`: multiple memory backends and user-scoped recall paths exist
- `Autonomous Execution`: scheduler and heartbeat paths exist in a real runtime
- `Cross-Channel`: channel catalog and dispatch model point to multi-surface operation
- `Integration Breadth`: tools, channels, memory engines, and integration gates exist
- `Operational Readiness`: health, readiness, metrics, diagnostics, and deployment artifacts exist

This matters because the category claim is much stronger when there is at least one runtime that clearly looks like runtime infrastructure instead of a thin chat wrapper.

## How the Repo Should Talk About Nullalis

Good framing:

- "Nullalis is the first public reference runtime evaluated with DTaaS-Bench."
- "Nullalis demonstrates why this category deserves its own benchmark."
- "The benchmark is open; any runtime can submit a stronger verified artifact."

Bad framing:

- "DTaaS-Bench proves Nullalis is best."
- "Nullalis defines the score."
- "Other systems are ranked by editorial judgment."

## What Makes Nullalis Useful for Open Source Launch

Nullalis gives the benchmark four things that help the repo open-source well:

1. a concrete, non-hypothetical runtime to benchmark
2. a first evidence-rich artifact for the leaderboard
3. a narrative bridge from product story to benchmark methodology
4. a quality bar that competitors can challenge publicly

## Recommended Public Narrative

Use this repo to say:

"DTaaS-Bench was created because existing assistant benchmarks mostly test stateless turn completion. Nullalis is the first reference runtime that made it obvious a stronger benchmark was needed. The benchmark is now open so anyone can reproduce the result, challenge the methodology, or beat the score with a better runtime."
