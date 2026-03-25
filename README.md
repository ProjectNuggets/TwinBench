# TwinBench

**Open Benchmark for Personal AI Assistant Runtimes**

TwinBench measures whether an AI runtime can behave like a real personal AI assistant: **remember, act, follow up, stay safe, and operate over time**.

This repository exists because the current benchmark landscape still misses a category between a chatbot and a task agent. We use the technical term `DTaaS` internally for that runtime category, but the public-facing benchmark is simpler:

**TwinBench defines the runtime category behind persistent personal AI assistants.**

Quick links:
- [Overview](docs/OVERVIEW.md)
- [Getting Started in 10 Minutes](docs/GETTING_STARTED.md)
- [Run Profiles](docs/RUN_PROFILES.md)
- [Compatibility Checklist](docs/COMPATIBILITY_CHECKLIST.md)
- [Preflight Checklist](docs/PREFLIGHT.md)
- [How to Submit Results](docs/HOW_TO_SUBMIT.md)
- [Results Index](docs/RESULTS_INDEX.md)
- [Trust Model](docs/TRUST_MODEL.md)
- [Press Kit](PRESSKIT.md)

## What TwinBench Measures

TwinBench is for runtimes that aim to behave like persistent personal AI assistants:

- remember across sessions and restarts
- execute tasks autonomously
- keep state coherent across channels and surfaces
- protect users during background turns
- operate as real runtime infrastructure, not just a single prompt loop

The benchmark reports two composites:

- `verified`: based only on behavior or evidence directly measured in the run
- `projected`: includes clearly labeled assumptions for not-yet-measured parts

The leaderboard tiers on `coverage_adjusted_verified_score`, not on the most flattering number.

## Who This Is For

- runtime builders shipping personal AI assistant products
- agent framework teams adding persistence and autonomous execution
- infra and platform teams building agent runtimes
- researchers studying long-lived assistants
- advanced indie builders who want a serious benchmark, not a demo script

## What This Is Not

- not a chatbot benchmark
- not a coding benchmark
- not a single-turn task benchmark
- not a marketing scorecard for one vendor

## Verified Results

Current reference artifacts derived from checked-in runs are listed in [docs/RESULTS_INDEX.md](docs/RESULTS_INDEX.md).

Nullalis is the current **reference runtime**, not the benchmark owner. Its role is to prove the category is real and to provide the first evidence-rich public artifact.

## Getting Started in 10 Minutes

```bash
git clone https://github.com/ProjectNuggets/DTaaS-benchmark.git
cd DTaaS-benchmark
python3.10 -m pip install -r harness/requirements.txt
```

Run a full benchmark:

```bash
python3.10 -m harness.runner \
  --url http://localhost:8080 \
  --token YOUR_TOKEN \
  --user-id 1 \
  --name "My Runtime" \
  --output results/run.json \
  --markdown results/run.md \
  --html results/run.html
```

Run local Nullalis with auto token discovery:

```bash
python3.10 -m harness.runner \
  --url http://127.0.0.1:3000 \
  --token-from-nullalis-config \
  --user-id 1 \
  --name "Nullalis Local"
```

Then:

1. open the generated JSON
2. review the verified score, projected score, and measured coverage
3. attach the artifact through [docs/HOW_TO_SUBMIT.md](docs/HOW_TO_SUBMIT.md)

If you are new here, start with [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md) instead of the full specification.

## Official Run Profiles

TwinBench currently documents three first-class run shapes:

- `local reference`: for a locally running runtime with direct access to internal auth
- `saas runtime`: for a remotely hosted runtime that exposes the benchmark contract
- `multi-tenant-ready`: for runtimes that support benchmark user provisioning and fair multi-user fanout

Details and commands are in [docs/RUN_PROFILES.md](docs/RUN_PROFILES.md).

## Benchmark Contract

Required runtime surfaces:

| Endpoint | Method | Purpose | Required |
|----------|--------|---------|----------|
| `/api/v1/chat/stream` | POST (SSE) | Send a message and receive streamed output | Yes |
| `/health` | GET | Health check | Yes |
| `/internal/diagnostics` | GET | Runtime introspection and evidence support | Yes |
| `/metrics` | GET | Prometheus-style metrics | Optional |

Before a full run, use the [Preflight Checklist](docs/PREFLIGHT.md) and [Compatibility Checklist](docs/COMPATIBILITY_CHECKLIST.md).

## Benchmark Principles

- neutral to vendor
- evidence over claims
- unsupported is not the same as failure
- missing bootstrap should be reported distinctly
- same-user contention is a diagnostic, not the primary multi-user scale claim

The full scoring and evidence rules live in [SPECIFICATION.md](SPECIFICATION.md) and [docs/TRUST_MODEL.md](docs/TRUST_MODEL.md).

## How Results Work

Every serious result should include:

- benchmark JSON
- Markdown or HTML report
- runtime version or commit SHA
- harness commit SHA
- diagnostics snapshot when available
- metrics snapshot when available
- incident notes when the run degraded

TwinBench also records dimension-level availability and reason codes so blocked or unsupported dimensions stay interpretable instead of silently looking like product weakness.

## New Here?

Recommended reading order:

1. [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md)
2. [docs/RUN_PROFILES.md](docs/RUN_PROFILES.md)
3. [docs/COMPATIBILITY_CHECKLIST.md](docs/COMPATIBILITY_CHECKLIST.md)
4. [docs/HOW_TO_SUBMIT.md](docs/HOW_TO_SUBMIT.md)
5. [SPECIFICATION.md](SPECIFICATION.md)

If your runtime does not match the contract yet, read [docs/INTEGRATION_PATHS.md](docs/INTEGRATION_PATHS.md).

## Repository Guide

```text
DTaaS-benchmark/
├── README.md
├── SPECIFICATION.md
├── PRESSKIT.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── docs/
│   ├── GETTING_STARTED.md
│   ├── RUN_PROFILES.md
│   ├── PREFLIGHT.md
│   ├── COMPATIBILITY_CHECKLIST.md
│   ├── GLOSSARY.md
│   ├── INTEGRATION_PATHS.md
│   ├── HOW_TO_SUBMIT.md
│   ├── RESULTS_INDEX.md
│   ├── OUTREACH_PACKET.md
│   ├── OUTREACH_TARGETS.md
│   └── TRUST_MODEL.md
├── harness/
└── results/
```

## Contributing

Contributions are welcome, especially:

- new verified runtime artifacts
- benchmark fairness improvements
- docs that make the benchmark easier to adopt
- better test coverage and report generation

Start with [CONTRIBUTING.md](CONTRIBUTING.md).
