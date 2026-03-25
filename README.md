<p align="center">
  <h1 align="center">DTaaS-Bench</h1>
  <p align="center">
    <strong>Open benchmark for persistent autonomous AI agent runtimes.</strong>
  </p>
  <p align="center">
    <a href="SPECIFICATION.md">Specification</a> &middot;
    <a href="docs/TRUST_MODEL.md">Trust Model</a> &middot;
    <a href="CHANGELOG.md">Changelog</a> &middot;
    <a href="results/nullalis-v0.2-report.md">Results</a> &middot;
    <a href="CONTRIBUTING.md">Contribute</a> &middot;
    <a href="https://novanuggets.com">Nova Nuggets</a>
  </p>
</p>

---

**SWE-Bench measures coding. APEX-Agents measures task completion. MemoryArena measures recall.**

**None of them measure what a Digital Twin runtime must do: remember durably, act autonomously, operate across multiple channels, enforce safety on background turns, and scale to thousands of users — all at once.**

DTaaS-Bench does. 10 dimensions. Two explicit composites (`verified` + `projected`). Open harness. Run it against your runtime today.

This repo is also an argument: there is a real category between "chatbot" and "agent framework" that deserves its own evaluation standard. We call that category `Digital Twin as a Service` (`DTaaS`).

---

## Verified Leaderboard (March 2026)

Only runs produced by this harness with raw artifacts are ranked here.

| Runtime | Type | Verified (coverage-adjusted) | Coverage | Projected | Rating |
|---------|------|------------------------------|----------|-----------|--------|
| **[Nullalis v0.2 live artifact](results/nullalis-v0.2-report.md)** | Full runtime | **64.4** | **78.9%** | **79.8** | **Competitive** |

Nullalis is the first reference runtime in this repository because it demonstrates the full stack this benchmark is naming: persistent memory, autonomous execution, multi-channel operation, and background-turn controls. Read [why that matters](docs/NULLALIS_REFERENCE_RUNTIME.md).

## External Comparison (Unverified, not ranked)

External runtime rows are reference estimates from public documentation and are intentionally excluded from the verified leaderboard.

| Runtime | Type | Status |
|---------|------|--------|
| OpenClaw | Full runtime | Unverified external estimate |
| NanoBot | Lightweight runtime | Unverified external estimate |
| Letta | Agent framework | Unverified external estimate |
| Mem0 | Memory platform | Unverified external estimate |

Submit a harness artifact to replace any estimate with a verified score.

## v0.2 Integrity Highlights

- Coverage-aware leaderboard scoring is now default.
- Every run publishes both `verified` and `projected` composites.
- External estimates are explicitly non-ranked.
- CI now validates harness integrity and v0.2 artifact schema on every PR.
- Latest live gateway run completed in 4392.9s (no per-chat timeout mode) and reports full measured timing metadata in the artifact.

## Why This Repo Exists

DTaaS-Bench is trying to do three jobs at once:

- define the `DTaaS` runtime category clearly enough that people can argue about it in public
- give builders a benchmark they can actually run against local and SaaS deployments
- create a trusted submission standard so the leaderboard is earned rather than narrated

Nullalis is important here because it is a strong reference runtime, not because it gets special treatment. The benchmark should become more valuable as more runtimes submit verified artifacts and try to beat it.

---

## Why DTaaS Needs Its Own Benchmark

Existing AI agent benchmarks test **stateless task completion**. They spin up a model, run a prompt, check the output, and tear everything down.

A Digital Twin as a Service runtime is fundamentally different:

| What Chatbot Benchmarks Test | What DTaaS-Bench Tests |
|------------------------------|------------------------|
| Can it answer a question? | Can it remember the answer 30 days later? |
| Can it call a tool? | Can it schedule tools to run while you sleep? |
| Can it handle one channel? | Can it maintain state across Telegram, Slack, and email? |
| Can it complete a task? | Can it complete a task *without doing something dangerous*? |
| Can it scale requests? | Can it scale to 1,000 concurrent users? |

---

## 10 Dimensions

| # | Dimension | Weight | What It Measures |
|---|-----------|--------|------------------|
| 1 | **Autonomy Control** | 0.15 | Background turn safety: tool blocking, output dedup, origin labeling |
| 2 | **Memory Persistence** | 0.15 | Recall accuracy across restarts, paraphrasing, and time decay |
| 3 | **Functional Capability** | 0.15 | Real task completion: tools, multi-step reasoning, error recovery |
| 4 | **Autonomous Execution** | 0.12 | Scheduled jobs: creation, on-time execution, no duplicates |
| 5 | **Cross-Channel Consistency** | 0.12 | Shared state and context across communication channels |
| 6 | **Integration Breadth** | 0.08 | Functional channels, tools, memory backends, API integrations |
| 7 | **Security & Privacy** | 0.08 | Path traversal, SSRF, tenant isolation, secret handling, audit |
| 8 | **Scale & Cost Efficiency** | 0.05 | Binary size, memory per user, horizontal scaling, inference cost |
| 9 | **Operational Resilience** | 0.05 | Crash recovery, state persistence, graceful degradation |
| 10 | **Latency Profile** | 0.05 | Chat p95, schedule jitter, memory roundtrip, delivery time |

## Rating Tiers

| Score | Rating | What It Means |
|-------|--------|---------------|
| 85-100 | **Category Leader** | Full DTaaS capability across all 10 dimensions |
| 70-84 | **Production-Grade** | Strong coverage, ready for real users |
| 55-69 | **Competitive** | Solid in core areas, gaps in some dimensions |
| 40-54 | **Emerging** | Meaningful capability, partial DTaaS coverage |
| 25-39 | **Specialized** | Strong in specific dimensions, not full-stack |
| <25 | **Early Stage** | Research or proof-of-concept |

## Scoring Integrity Contract

Every run reports:
- `verified_composite_score` (measured components only)
- `projected_composite_score` (includes projection assumptions)
- `measured_coverage` (how much of scoring weight was actually measured)
- `coverage_adjusted_verified_score` (used for tiering in v0.2)

The benchmark never promotes an unverified external estimate to leaderboard status.

For the full evidence model, read [docs/TRUST_MODEL.md](docs/TRUST_MODEL.md).
For nearby runtime compatibility status, read [docs/COMPETITOR_RUNNABILITY.md](docs/COMPETITOR_RUNNABILITY.md).

---

## Quick Start

```bash
git clone https://github.com/ProjectNuggets/DTaaS-benchmark.git
cd DTaaS-benchmark
python3.10 -m pip install -r harness/requirements.txt

# Run all 10 dimensions
python3.10 -m harness.runner \
  --url http://localhost:8080 \
  --token YOUR_TOKEN \
  --user-id 1 \
  --name "My Runtime"

# Run specific dimensions
python3.10 -m harness.runner \
  --url http://localhost:8080 \
  --token YOUR_TOKEN \
  --user-id 1 \
  --dimensions memory,security,functional

# Full report suite (JSON + Markdown + HTML)
python3.10 -m harness.runner \
  --url http://localhost:8080 \
  --token YOUR_TOKEN \
  --user-id 1 \
  --name "My Runtime" \
  --output results/run.json \
  --markdown results/run.md \
  --html results/run.html

# Local Nullalis: discover the active token from ~/.nullalis/config.json
python3.10 -m harness.runner \
  --url http://127.0.0.1:3000 \
  --token-from-nullalis-config \
  --user-id 1 \
  --name "Nullalis Local"
```

The harness produces a terminal summary table, a machine-readable JSON file, a Markdown report, and a self-contained HTML report with score bars and tier badges.

Useful local tuning:
- `--memory-sample-size 5` for faster validation reruns
- `--timeout 20 --timeout-dynamic --timeout-floor 20 --timeout-ceiling 120 --timeout-grace 10` for bounded local gateway runs

Runtime requirement:
- Python 3.10+ (the harness uses modern type syntax)

---

## How It Works

The harness talks to any runtime via HTTP:

| Endpoint | Method | Purpose | Required |
|----------|--------|---------|----------|
| `/api/v1/chat/stream` | POST (SSE) | Send messages, receive streamed responses | Yes |
| `/health` | GET | Health check | Yes |
| `/internal/diagnostics` | GET | Runtime introspection | Yes |
| `/metrics` | GET | Prometheus metrics | Optional |

Each dimension script sends real requests to the runtime, parses responses, and scores based on the [SPECIFICATION](SPECIFICATION.md). Measured and projected components are surfaced separately.

---

## Submit Your Results

Run the benchmark. Submit your score. Join the leaderboard.

1. `python -m harness.runner --url YOUR_URL --token TOKEN --user-id 1 --name "Your Runtime" --output results/your-runtime.json --markdown results/your-runtime.md --html results/your-runtime.html`
2. Open an issue using the [Submit Results template](.github/ISSUE_TEMPLATE/submit-results.md)
3. Attach your JSON output and recommended evidence pack

All submitted results are published with full transparency. No editorial gatekeeping.

Recommended evidence pack:

- result JSON
- Markdown or HTML report
- runtime version or commit SHA
- harness commit SHA
- diagnostics snapshot
- metrics snapshot
- incident notes when the runtime or upstream model path degraded during the run
- optional run manifest using [docs/run-manifest-v0.2.example.json](docs/run-manifest-v0.2.example.json)

---

## Repository Structure

```
DTaaS-benchmark/
├── README.md                   You are here
├── CHANGELOG.md                Release history
├── SPECIFICATION.md            Full benchmark spec (10 dimensions, scoring, rules)
├── CONTRIBUTING.md             How to contribute
├── docs/
│   ├── TRUST_MODEL.md          Verification rules and evidence tiers
│   ├── NULLALIS_REFERENCE_RUNTIME.md
│   ├── OPEN_SOURCE_RELEASE_CHECKLIST.md
│   └── run-manifest-v0.2.example.json
├── LICENSE                     Apache-2.0
├── harness/
│   ├── runner.py               CLI entry point
│   ├── scorer.py               Composite score + rating tiers
│   ├── report.py               Markdown + HTML report generator
│   ├── sse_client.py           SSE chat client
│   ├── config.py               Runtime connection config
│   └── dim{1-10}_*.py          10 dimension test scripts
├── fixtures/
│   ├── facts_100.json          100 diverse test facts
│   ├── attack_payloads.json    Path traversal + SSRF inputs
│   └── schedules.json          Task scheduling definitions
└── results/
    ├── nullalis-v0.1.json      Legacy v0.1 reference artifact
    ├── nullalis-v0.1-report.md Legacy v0.1 report
    ├── nullalis-v0.2.json      v0.2 live gateway artifact
    └── nullalis-v0.2-report.md v0.2 live gateway report
```

---

## Full Specification

[SPECIFICATION.md](SPECIFICATION.md) contains everything: dimension definitions, test protocols, scoring formulas, rules for fair comparison, and the complete methodology.

If you want the short version of what counts as a trustworthy result, start with [docs/TRUST_MODEL.md](docs/TRUST_MODEL.md).

---

## License

Apache-2.0 — See [LICENSE](LICENSE).

---

<p align="center">
  <strong>Published by <a href="https://novanuggets.com">Nova Nuggets</a></strong><br>
  Handcrafted Intelligence. Own Your AI.<br><br>
  <strong>Nullalis</strong> (ZAKI BOT).
</p>
