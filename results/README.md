# Results

This directory contains the public-facing TwinBench v1 result surface.

Current contents:

- `reference-example-v1.json` — reference example for the v1 schema
- `chatgpt_baseline_v1.json` — modeled stateless conversational baseline
- `openclaw_baseline_v1.json` — modeled agentic execution baseline
- `zaki_baseline_v1.json` — modeled persistence-oriented baseline

## Artifact Classes

- `reference example`: demonstrates schema and reporting format; not a measured competitive result
- `modeled baseline`: comparison artifact grounded in stated assumptions and observation fixtures; not a live measured run

## Real Measured Repository Artifacts

The repository also contains real first-party measured benchmark outputs in [`legacy/results/`](../legacy/results). Those files come from earlier TwinBench v0.2 harness runs and include multiple Nullalis evaluations, both strong and degraded.

The most important measured artifact currently in the repository is:

- [`legacy/results/nullalis-live-2026-03-25-openended.json`](../legacy/results/nullalis-live-2026-03-25-openended.json)

That file is a recorded first-party run, not a reference example. It uses the earlier v0.2 dimension-based schema rather than the simplified v1 schema used in this directory.

## How To Interpret This Directory

- Use files in this directory for v1 schema examples and modeled baseline comparison.
- Use files in `legacy/results/` when you need the strongest currently recorded measured evidence in the repository.
- Do not compare a modeled v1 baseline directly to a measured v0.2 harness score without stating the schema difference.
