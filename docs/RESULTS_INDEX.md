# Results Index

This page summarizes checked-in TwinBench artifacts.

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

Notes:

- strong core runtime behavior
- earlier scale interpretation was conservative before provisioning-aware fixes
- Nullalis is treated as the reference runtime, not the benchmark owner

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
