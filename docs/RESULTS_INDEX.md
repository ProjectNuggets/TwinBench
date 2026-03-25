# Results Index

This page summarizes checked-in TwinBench artifacts and gives a public-facing way to read them.

## Current Reference Result

### Nullalis Local Open-Ended Race

Artifact:

- [Open-ended JSON](../results/nullalis-live-2026-03-25-openended.json)
- [Open-ended Markdown](../results/nullalis-live-2026-03-25-openended.md)
- [Open-ended HTML](../results/nullalis-live-2026-03-25-openended.html)

Headline:

- Coverage-adjusted verified: `75.9`
- Verified raw: `90.9`
- Projected: `87.6`
- Rating: `Production-Grade`
- Result class: `reference runtime artifact`
- Submit your runtime: [HOW_TO_SUBMIT.md](HOW_TO_SUBMIT.md)

Notes:

- strong core runtime behavior
- earlier scale interpretation was conservative before provisioning-aware fixes
- Nullalis is treated as the reference runtime, not the benchmark owner
- scale interpretation is conservative relative to later provisioning-aware fixes

## How to Read a Result

Start with:

- `coverage_adjusted_verified_score`: the leaderboard-facing tiering score
- `verified_composite_score`: the directly measured score
- `projected_composite_score`: the wider estimate with explicit assumptions
- `measured_coverage`: how much of the benchmark was directly exercised

Then check:

- `dimension_status`
- `dimension_reason_codes`

These fields tell you whether a weak dimension was truly measured, only partially measured, unavailable, or blocked by environment or contract limitations.

Use [ARTIFACT_SCHEMA.md](ARTIFACT_SCHEMA.md) for the field guide.
See [REFERENCE_RESULT_POLICY.md](REFERENCE_RESULT_POLICY.md) for how TwinBench treats canonical, supporting, degraded, and external artifacts.

## Supporting Artifacts

- [Nullalis scale probe](../results/nullalis-scale-probe.json)
- [Nullalis local 2026-03-24](../results/nullalis-local-2026-03-24.json)
- [Nullalis targeted 2026-03-24](../results/nullalis-targeted-2026-03-24.json)
- [Nullalis live 2026-03-25 auth-poisoned run](../results/nullalis-live-2026-03-25.json)

## Interpretation

Reference artifacts are useful because they show:

- the benchmark is runnable
- degraded runs are preserved rather than hidden
- score trust comes from artifacts, not narration

## Leaderboard Intent

TwinBench should become a public place where competing runtimes can publish artifact-backed results and challenge each other openly.
