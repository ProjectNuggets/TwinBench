# TwinBench Leaderboard

TwinBench currently has two public result classes:

- first-party measured harness artifacts under the earlier TwinBench v0.2 schema
- modeled baseline comparisons under the current simplified TwinBench v1 scaffold

No public third-party submissions are listed yet.

## First-Party Measured Artifacts

These are recorded benchmark runs checked into the repository. They are first-party evaluations and should be read as repository evidence, not neutral external audits.

| System | Version | Benchmark Version | Date Evaluated | MR | IC | CCC | TC | PG | Total Score | Evidence | Caveats / Notes |
|--------|---------|-------------------|----------------|----|----|-----|----|----|-------------|----------|-----------------|
| Nullalis local openended race | local openended race | 0.2 | 2026-03-25 | - | - | - | - | - | 75.9 coverage-adjusted verified | [legacy/results/nullalis-live-2026-03-25-openended.json](legacy/results/nullalis-live-2026-03-25-openended.json) | Real first-party harness run. Uses legacy 10-dimension schema, not v1 five-metric scoring. Measured coverage 83.5%. |
| Nullalis local live baseline | local live | 0.2 | 2026-03-24 | - | - | - | - | - | 68.1 coverage-adjusted verified | [legacy/results/nullalis-local-2026-03-24.json](legacy/results/nullalis-local-2026-03-24.json) | Real first-party harness run. Earlier stable baseline before later failures. |
| Nullalis auth-mismatch degraded run | local live | 0.2 | 2026-03-25 | - | - | - | - | - | 5.8 coverage-adjusted verified | [legacy/results/nullalis-live-2026-03-25.json](legacy/results/nullalis-live-2026-03-25.json) | Real first-party degraded run. Chat turns failed with unauthorized errors; not suitable as headline evidence. |
| Nullalis targeted degraded run | local live | 0.2 | 2026-03-24 | - | - | - | - | - | 0.0 coverage-adjusted verified | [legacy/results/nullalis-targeted-2026-03-24.json](legacy/results/nullalis-targeted-2026-03-24.json) | Real first-party degraded run. Runtime unavailability dominated the result. |

## Modeled Baseline Comparisons

These entries are comparison baselines designed to show what TwinBench distinguishes. They are not live measured runs.

Displayed score scale: `0.0-1.0 normalized`

| System | Version | Benchmark Version | Date Evaluated | MR | IC | CCC | TC | PG | Total Score | Evidence | Caveats / Notes |
|--------|---------|-------------------|----------------|----|----|-----|----|----|-------------|----------|-----------------|
| ChatGPT-like stateless conversational AI | baseline-simulated-v1 | TwinBench v1 | 2026-04-03 | 0.10 | 0.42 | 0.22 | 0.18 | 0.08 | 0.20 | [results/chatgpt_baseline_v1.json](results/chatgpt_baseline_v1.json) | Modeled baseline, not a live product run. |
| OpenClaw-like agent system | baseline-simulated-v1 | TwinBench v1 | 2026-04-03 | 0.40 | 0.35 | 0.33 | 0.56 | 0.20 | 0.37 | [results/openclaw_baseline_v1.json](results/openclaw_baseline_v1.json) | Modeled baseline, not a live product run. |
| ZAKI / Nullalis-like persistent system | baseline-simulated-v1 | TwinBench v1 | 2026-04-03 | 0.78 | 0.74 | 0.71 | 0.76 | 0.80 | 0.76 | [results/zaki_baseline_v1.json](results/zaki_baseline_v1.json) | Modeled persistence-oriented profile. Should not be confused with the measured Nullalis harness runs above. |

## Interpretation Notes

- The strongest measured result in the repository is the Nullalis 2026-03-25 open-ended harness run.
- The v1 baseline rows are easier to compare quickly, but they carry lower evidentiary weight because they are modeled.
- TwinBench should prefer measured artifacts over modeled baselines whenever both exist.
