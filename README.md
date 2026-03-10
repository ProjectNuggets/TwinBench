<p align="center">
  <h1 align="center">DTaaS-Bench</h1>
  <p align="center">
    <strong>The first industry benchmark for persistent autonomous AI agent runtimes.</strong>
  </p>
  <p align="center">
    <a href="SPECIFICATION.md">Specification</a> &middot;
    <a href="results/nullalis-v0.1-report.md">Results</a> &middot;
    <a href="CONTRIBUTING.md">Contribute</a> &middot;
    <a href="https://novanuggets.com">Nova Nuggets</a>
  </p>
</p>

---

**SWE-Bench measures coding. APEX-Agents measures task completion. MemoryArena measures recall.**

**None of them measure what a Digital Twin runtime must do: remember durably, act autonomously, operate across multiple channels, enforce safety on background turns, and scale to thousands of users — all at once.**

DTaaS-Bench does. 10 dimensions. One composite score. Open harness. Run it against your runtime today.

---

## Leaderboard (March 2026)

| Runtime | Type | Score | Rating | Best Dimension |
|---------|------|-------|--------|----------------|
| **[Nullalis v0.1](results/nullalis-v0.1-report.md)** | Full runtime | **87** | **Category Leader** | Integration Breadth (97) |
| [OpenClaw](https://github.com/openclaw) (est.) | Full runtime | 62 | Competitive | Channels (75) |
| [NanoBot](https://github.com/hkuds/nanobot) (est.) | Lightweight runtime | 52 | Emerging | Latency (70) |
| [Letta](https://github.com/letta-ai/letta) (est.) | Agent framework | 46 | Emerging | Memory (85) |
| [Mem0](https://mem0.ai) (est.) | Memory platform | 41 | Specialized | Memory (88) |

> Estimated scores based on public documentation (March 2026). **Submit verified results to join the leaderboard.**

<details>
<summary><strong>Full dimension breakdown</strong></summary>

| Dimension (weight) | Nullalis | OpenClaw | NanoBot | Letta | Mem0 |
|--------------------|----------|----------|---------|-------|------|
| Autonomy Control (0.15) | 96 | 45 | 30 | 30 | 15 |
| Memory Persistence (0.15) | 91 | 70 | 55 | 85 | 88 |
| Functional Capability (0.15) | 85 | 75 | 65 | 55 | 50 |
| Autonomous Execution (0.12) | 85 | 55 | 50 | 25 | 10 |
| Cross-Channel (0.12) | 85 | 75 | 50 | 15 | 10 |
| Integration Breadth (0.08) | 97 | 70 | 35 | 35 | 25 |
| Security & Privacy (0.08) | 89 | 35 | 40 | 40 | 30 |
| Scale & Cost (0.05) | 74 | 55 | 65 | 55 | 65 |
| Resilience (0.05) | 78 | 50 | 45 | 55 | 50 |
| Latency (0.05) | 72 | 70 | 70 | 65 | 70 |

</details>

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

---

## Quick Start

```bash
git clone https://github.com/ProjectNuggets/DTaaS-benchmark.git
cd DTaaS-benchmark
pip install -r harness/requirements.txt

# Run all 10 dimensions
python -m harness.runner \
  --url http://localhost:8080 \
  --token YOUR_TOKEN \
  --user-id 1 \
  --name "My Runtime"

# Run specific dimensions
python -m harness.runner \
  --url http://localhost:8080 \
  --token YOUR_TOKEN \
  --user-id 1 \
  --dimensions memory,security,functional

# Full report suite (JSON + Markdown + HTML)
python -m harness.runner \
  --url http://localhost:8080 \
  --token YOUR_TOKEN \
  --user-id 1 \
  --name "My Runtime" \
  --output results/run.json \
  --markdown results/run.md \
  --html results/run.html
```

The harness produces a terminal summary table, a machine-readable JSON file, a Markdown report, and a self-contained HTML report with score bars and tier badges.

---

## How It Works

The harness talks to any runtime via HTTP:

| Endpoint | Method | Purpose | Required |
|----------|--------|---------|----------|
| `/api/v1/chat/stream` | POST (SSE) | Send messages, receive streamed responses | Yes |
| `/health` | GET | Health check | Yes |
| `/internal/diagnostics` | GET | Runtime introspection | Yes |
| `/metrics` | GET | Prometheus metrics | Optional |

Each dimension script sends real requests to the runtime, parses responses, and scores based on the [SPECIFICATION](SPECIFICATION.md). No mocks. No synthetic benchmarks. Real agent behavior.

---

## Submit Your Results

Run the benchmark. Submit your score. Join the leaderboard.

1. `python -m harness.runner --url YOUR_URL --token TOKEN --user-id 1 --name "Your Runtime" --output results/your-runtime.json`
2. Open an issue using the [Submit Results template](.github/ISSUE_TEMPLATE/submit-results.md)
3. Attach your JSON output

All submitted results are published with full transparency. No editorial gatekeeping.

---

## Repository Structure

```
DTaaS-benchmark/
├── README.md                   You are here
├── SPECIFICATION.md            Full benchmark spec (10 dimensions, scoring, rules)
├── CONTRIBUTING.md             How to contribute
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
    ├── nullalis-v0.1.json      Machine-readable reference results
    └── nullalis-v0.1-report.md Human-readable reference report
```

---

## Full Specification

[SPECIFICATION.md](SPECIFICATION.md) contains everything: dimension definitions, test protocols, scoring formulas, rules for fair comparison, and the complete methodology.

---

## License

Apache-2.0 — See [LICENSE](LICENSE).

---

<p align="center">
  <strong>Published by <a href="https://novanuggets.com">Nova Nuggets</a></strong><br>
  Handcrafted Intelligence. Own Your AI.<br><br>
  <strong>Nullalis</strong> (ZAKI BOT) is the reference implementation for DTaaS-Bench<br>
  and the first runtime to achieve <strong>Category Leader</strong> (87/100).
</p>
