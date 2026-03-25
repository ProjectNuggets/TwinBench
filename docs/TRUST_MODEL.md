# TwinBench Trust Model

TwinBench is designed to do two things at the same time:

1. define a real category in the AI assistant market, and
2. remain trustworthy enough that the category is taken seriously.

That means the benchmark cannot just be a marketing scorecard. It needs clear evidence rules, explicit limits, and reproducible artifacts.

## What TwinBench Measures

TwinBench measures persistent personal AI assistant runtimes:

- systems that remember across sessions and restarts
- systems that act without a user actively typing
- systems that operate across multiple channels
- systems that enforce safety and operator control during background turns
- systems that can be deployed as real runtime infrastructure, not just prompt wrappers

Inside this repo, this is the category we still call `Digital Twin as a Service` (`DTaaS`).

## The Benchmark Integrity Rule

Every published result must separate:

- `verified` score: based only on behavior or evidence actually measured in the run
- `projected` score: includes explicitly stated assumptions for components not fully exercised
- `measured_coverage`: the fraction of total scoring weight that was directly measured
- `coverage_adjusted_verified_score`: the score used for leaderboard tiering

The benchmark never treats an estimate as a verified leaderboard result.

## Evidence Tiers

TwinBench uses three evidence tiers.

### Tier 1: Live Behavioral Evidence

Best evidence. The harness talks to a running runtime and measures what it actually does.

Examples:

- SSE chat responses
- schedule creation and execution
- memory store and recall
- health and diagnostics endpoint responses
- latency and concurrency measurements

### Tier 2: Runtime Introspection Evidence

Useful, but weaker than direct behavior. This includes diagnostics, metrics, and other runtime-provided self-description surfaces.

Examples:

- `/internal/diagnostics`
- `/metrics`
- `runtime_info`

Introspection can support a result, but it should not replace behavioral testing when behavioral testing is possible.

### Tier 3: Architecture or Code-Based Evidence

Valid for context, reference reports, and pre-open-source baseline work, but not sufficient on its own for leaderboard-grade verification.

Examples:

- source code inspection
- internal test counts
- deployment manifests
- design documents

This evidence is useful for explaining why a runtime should perform well, but the open benchmark should prefer live evidence for ranking.

## Result Classes

TwinBench uses three result classes.

### Verified Leaderboard Result

Requirements:

- produced by the public harness
- includes raw JSON artifact
- includes measured coverage and verified/projected separation
- includes reproducible runtime metadata
- includes incident notes when runtime or upstream degradation affected the run
- no missing integrity-critical fields

### Reference Result

Reference results are published to explain the category or show what a strong runtime looks like, but they are not the ranked leaderboard unless they satisfy the full verified result requirements.

Reference results may use:

- internal canary evidence
- code-backed capability ledgers
- partial live runs
- rollout diagnostics

### External Estimate

External estimates are non-ranked comparison rows derived from public materials. They are useful for framing the market, but they are not benchmark results.

## Anti-Gaming Principles

The benchmark should reward real runtime behavior, not polished answers.

TwinBench therefore prefers:

- observed behavior over claims
- endpoint evidence over natural-language self-report
- durable state changes over conversational promises
- attached raw artifacts over screenshots or summaries
- measured coverage over inflated projected totals

Known weak spots should be documented openly. If a dimension currently depends on runtime self-report or architectural inference, that should be stated in the report.

## Incident Attribution

Trusted benchmarking also means being clear about where a failure happened and why a dimension may be unavailable.

When a run degrades, submissions should distinguish between:

- runtime capability failure: the runtime stayed up, but behavior was incorrect or missing
- runtime availability failure: the benchmarked runtime became unavailable during the run
- upstream dependency failure: model provider, vector provider, or external integration instability affected the run
- contract mismatch: the runtime could not be exercised fairly because it needs an adapter or does not implement the benchmark transport

If a run encounters an outage or degraded upstream dependency, that does not invalidate the artifact. It does mean the artifact should say so explicitly.

Public artifacts should also separate:

- measured dimension
- partially measured dimension
- unavailable dimension
- error during dimension execution

Whenever possible, a dimension that is unavailable should include a reason code. Examples:

- `multi_user_bootstrap_unavailable`
- `contract_mismatch`
- `missing_diagnostics_surface`
- `runtime_unavailable_during_probe`

Strong submissions should attach:

- representative error messages
- pre-run and post-run diagnostics when available
- a short note explaining whether the failure appears to be inside the runtime or upstream of it

The benchmark should never hide a bad run. It also should not mislabel a provider outage as a missing product capability when the evidence shows otherwise.

## Why Nullalis Matters

Nullalis is the current reference runtime for this category because it appears to implement the full stack the benchmark is naming:

- persistent per-user runtime state
- background heartbeat and scheduler paths
- turn-origin-aware tool policy
- multi-channel runtime architecture
- diagnostics, metrics, and deployment surfaces
- memory, tools, integrations, and tenant operation

Nullalis should not receive special scoring treatment. Its value is different:

- it proves the category is real
- it provides a strong first public artifact
- it shows what evidence-rich runtime design looks like

The benchmark remains stronger when Nullalis is treated as the first serious reference runtime, not as the owner of truth.

## Minimum Artifact Package

A serious submission should include:

- benchmark JSON result
- markdown or HTML report
- runtime version or commit SHA
- harness commit SHA
- environment summary
- timeout mode and timing metadata
- notes on which dimensions were partially projected

Recommended additions:

- diagnostics snapshot
- metrics snapshot
- logs archive
- run manifest
- incident notes when degradation occurred

## Open Benchmark Position

TwinBench is opinionated about the category, but it should be neutral about who wins.

The benchmark is strongest when:

- Nullalis is the first strong example
- other runtimes can beat it in public
- every claim is attached to an artifact
- the leaderboard is earned, not editorially assigned
