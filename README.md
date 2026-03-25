# TwinBench

**Open Benchmark for Personal AI Assistants**

TwinBench is the open benchmark for personal AI assistants. It measures whether an AI system can **remember, act, follow up, stay safe, and operate over time**.

This repository exists because the current benchmark landscape still misses a category between a chatbot and a task agent. We use the technical term `DTaaS` internally for that runtime category, but the public-facing benchmark is simpler:

**TwinBench defines the runtime category behind persistent personal AI assistants.**

## Website

TwinBench now ships with a lightweight public site and leaderboard surface in [`website/`](website/).

Build it locally:

```bash
make site
```

Then open:

- `website/index.html`
- `website/results/nullalis-live-2026-03-25-openended/index.html`

## Quick Run

Generic runtime:

```bash
python3.10 -m harness.runner --url YOUR_URL --token YOUR_TOKEN --user-id 1 --name "Your Runtime" --output results/your-runtime.json --markdown results/your-runtime.md --html results/your-runtime.html
```

Local Nullalis:

```bash
python3.10 -m harness.runner --url http://127.0.0.1:3000 --token-from-nullalis-config --user-id 1 --name "Nullalis Local" --output results/nullalis-local.json --markdown results/nullalis-local.md --html results/nullalis-local.html
```

Scripted shortcuts:

```bash
make preflight URL=http://localhost:8080 TOKEN=YOUR_TOKEN
make run URL=http://localhost:8080 TOKEN=YOUR_TOKEN NAME="My Runtime"
make run-nullalis
make demo
make site
```

Quick links:
- [Overview](docs/OVERVIEW.md)
- [Introducing TwinBench](docs/INTRODUCING_TWINBENCH.md)
- [Why TwinBench](docs/WHY_TWINBENCH.md)
- [Why Current AI Benchmarks Miss Personal AI Assistants](docs/WHY_CURRENT_AI_BENCHMARKS_MISS_PERSONAL_AI_ASSISTANTS.md)
- [What Is a Personal AI Assistant?](docs/WHAT_IS_A_PERSONAL_AI_ASSISTANT.md)
- [Getting Started in 10 Minutes](docs/GETTING_STARTED.md)
- [Run with Agents](docs/AGENT_RUN_GUIDE.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)
- [Run Profiles](docs/RUN_PROFILES.md)
- [Compatibility Checklist](docs/COMPATIBILITY_CHECKLIST.md)
- [Preflight Checklist](docs/PREFLIGHT.md)
- [Artifact Schema Explainer](docs/ARTIFACT_SCHEMA.md)
- [How to Submit Results](docs/HOW_TO_SUBMIT.md)
- [Results Index](docs/RESULTS_INDEX.md)
- [Roadmap](docs/ROADMAP.md)
- [Monthly Challenge](docs/MONTHLY_CHALLENGE.md)
- [Notable Submissions](docs/NOTABLE_SUBMISSIONS.md)
- [Case Study Template](docs/CASE_STUDY_TEMPLATE.md)
- [Trust Model](docs/TRUST_MODEL.md)
- [Launch Packet](docs/LAUNCH_PACKET.md)
- [Outreach Waves](docs/OUTREACH_WAVES.md)
- [Press Kit](PRESSKIT.md)

## Category Definition

A personal AI assistant runtime is not just a chatbot. It is a long-lived system that remembers, acts, and stays aligned with one user over time.

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

## One-Click Demo

If you want to see TwinBench run successfully before pointing it at a real runtime, use the fixture demo runtime.

Local demo:

```bash
make demo
```

Docker demo:

```bash
docker compose up --build benchmark
```

This path spins up a small fixture assistant runtime, runs a short TwinBench pass, and writes artifacts to `results/twinbench-demo-runtime.*`.

## Run with Agents

If you want Codex, Claude Code, Cursor, or another coding agent to run TwinBench for you, use the exact command above or hand it this prompt:

> Run TwinBench against this runtime at URL X using token Y. First perform the preflight checks, then run the harness, save JSON, Markdown, and HTML artifacts, and summarize the verified score, projected score, measured coverage, dimension statuses, and any unavailable dimensions with reason codes.

For a machine-operator-ready guide, use [docs/AGENT_RUN_GUIDE.md](docs/AGENT_RUN_GUIDE.md).

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

The public website/leaderboard surface is generated from checked-in artifacts in [`website/`](website/).

## Community

TwinBench is GitHub-first for now:

- GitHub Discussions for benchmark questions and feedback
- issues for compatibility requests
- submissions for new public artifacts

Community hub:

- https://github.com/ProjectNuggets/DTaaS-benchmark/discussions

Nullalis is the current **reference runtime**, not the benchmark owner. Its role is to prove the category is real and to provide the first evidence-rich public artifact.

Canonical public reference artifact:

- [Nullalis TwinBench HTML report](results/nullalis-live-2026-03-25-openended.html)
- [Nullalis TwinBench JSON artifact](results/nullalis-live-2026-03-25-openended.json)

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

When you read a TwinBench artifact, start with:

- `verified_composite_score`: what the run directly proved
- `projected_composite_score`: what the runtime may support beyond direct measurement
- `measured_coverage`: how much of the benchmark was directly exercised
- `coverage_adjusted_verified_score`: the number used for tiering
- `dimension_status`: whether each dimension was measured, partially measured, unavailable, or errored
- `dimension_reason_codes`: why a dimension was unavailable or only partially measurable

Use [docs/ARTIFACT_SCHEMA.md](docs/ARTIFACT_SCHEMA.md) for a plain-English field guide.

Every serious result should include:

- benchmark JSON
- Markdown or HTML report
- runtime version or commit SHA
- harness commit SHA
- diagnostics snapshot when available
- metrics snapshot when available
- incident notes when the run degraded

TwinBench also records dimension-level availability and reason codes so blocked or unsupported dimensions stay interpretable instead of silently looking like product weakness.

Scale fairness matters especially here:

- same-user serialization is normal for many personal AI assistant runtimes
- multi-user scale claims require provisioned users
- bootstrap-unavailable should not be misread as poor throughput

## New Here?

Recommended reading order:

Builders:
1. [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md)
2. [docs/PREFLIGHT.md](docs/PREFLIGHT.md)
3. [docs/RUN_PROFILES.md](docs/RUN_PROFILES.md)

Researchers:
1. [docs/WHY_TWINBENCH.md](docs/WHY_TWINBENCH.md)
2. [SPECIFICATION.md](SPECIFICATION.md)
3. [docs/TRUST_MODEL.md](docs/TRUST_MODEL.md)

Competitors:
1. [docs/COMPATIBILITY_CHECKLIST.md](docs/COMPATIBILITY_CHECKLIST.md)
2. [docs/INTEGRATION_PATHS.md](docs/INTEGRATION_PATHS.md)
3. [docs/HOW_TO_SUBMIT.md](docs/HOW_TO_SUBMIT.md)

Agent operators:
1. [docs/AGENT_RUN_GUIDE.md](docs/AGENT_RUN_GUIDE.md)
2. [docs/PREFLIGHT.md](docs/PREFLIGHT.md)
3. [docs/HOW_TO_SUBMIT.md](docs/HOW_TO_SUBMIT.md)

If your runtime does not match the contract yet, read [docs/INTEGRATION_PATHS.md](docs/INTEGRATION_PATHS.md).

## FAQ

### Is this a chatbot benchmark?

No. TwinBench is about long-lived assistant runtime behavior, not only single-turn response quality.

### Is this only for Nullalis?

No. Nullalis is the reference runtime because it provides the first strong artifact. The benchmark is intended to be challenged publicly by other runtimes.

### Can I run this on a hosted product?

Yes, if the product exposes the benchmark contract or a documented compatibility path.

### What if my runtime only supports part of the category?

Run TwinBench anyway. A partial but honest artifact is more useful than a narrated claim.

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

## Nova Nuggets

TwinBench is published by [Nova Nuggets](https://novanuggets.com), an AI innovation company building toward **personal, secure, sovereign AI for everyone**.

Our focus is practical infrastructure and products for long-lived assistants. The benchmark should stay neutral and open, while making that mission visible to people who discover the repo.
