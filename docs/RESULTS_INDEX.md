# Results Index

This page is the public landing page for checked-in TwinBench artifacts. It highlights one canonical current result, shows benchmark progression without clutter, and keeps supporting artifacts available for audit.

## Current Reference Result

### Nullalis Local Open-Ended Race

Current public reference artifact:

- [Canonical JSON](../results/nullalis-live-2026-03-25-openended.json)
- [Canonical Markdown](../results/nullalis-live-2026-03-25-openended.md)
- [Canonical HTML](../results/nullalis-live-2026-03-25-openended.html)

Headline:

- Coverage-adjusted verified: `75.9`
- Verified raw: `90.9`
- Projected: `87.6`
- Rating: `Production-Grade`
- Result class: `reference runtime artifact`

Short interpretation:

- strong evidence of real personal AI assistant runtime behavior
- best-in-repo proof so far across memory, execution, resilience, and latency
- current public score is conservative on scale because the multi-user fairness fix landed after this full run
- Nullalis is the reference runtime, not the benchmark owner

Next step:

- Submit your runtime: [HOW_TO_SUBMIT.md](HOW_TO_SUBMIT.md)

## Benchmark Progression

TwinBench keeps earlier artifacts for audit, but only one result is promoted as the current public reference artifact.

| Date | Artifact | Coverage-Adjusted Verified | Verified Raw | Projected | Note |
|------|----------|----------------------------|--------------|-----------|------|
| 2026-03-24 | [Nullalis local baseline](../results/nullalis-local-2026-03-24.json) | `68.1` | `81.6` | `77.9` | Early strong baseline before later runtime instability. |
| 2026-03-24 | [Nullalis targeted degraded run](../results/nullalis-targeted-2026-03-24.json) | `0.0` | `0.0` | `6.9` | Captured real provider and gateway collapse instead of hiding it. |
| 2026-03-25 | [Nullalis auth-poisoned run](../results/nullalis-live-2026-03-25.json) | `5.8` | `8.4` | `17.4` | Invalid as a headline artifact because chat turns were rejected by token mismatch. |
| 2026-03-25 | [Nullalis full reference run](../results/nullalis-live-2026-03-25-openended.json) | `75.9` | `90.9` | `87.6` | Canonical full TwinBench artifact and current public reference result. |
| 2026-03-25 | [Nullalis scale fairness probe](../results/nullalis-scale-probe.json) | `1.0` | `96.0` | `3.8` | Supporting evidence only; validates the later provisioning-aware scale fix. |

Progression note:

The canonical full Nullalis result remains the public reference artifact. Scale interpretation in that run is conservative relative to the later provisioning-aware scale fix.

## Supporting Artifacts

These artifacts matter for trust, but they are not visually elevated to equal status with the canonical reference result.

- [Nullalis scale probe](../results/nullalis-scale-probe.json)
- [Nullalis local baseline Markdown](../results/nullalis-local-2026-03-24.md)
- [Nullalis targeted degraded Markdown](../results/nullalis-targeted-2026-03-24.md)
- [Nullalis auth-poisoned Markdown](../results/nullalis-live-2026-03-25.md)

Why keep them:

- they show benchmark evolution
- they preserve degraded behavior instead of silently deleting it
- they make the scoring story auditable

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

## Leaderboard Intent

TwinBench should become the public place where competing personal AI assistant runtimes publish artifact-backed results and challenge each other openly.
