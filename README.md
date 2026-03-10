# DTaaS-Bench v0.1

### The first industry benchmark for persistent autonomous AI agent runtimes.

> No existing benchmark measures what a Digital Twin runtime must do: remember durably, act autonomously, operate across channels, and stay safe — all at once. DTaaS-Bench does.

Published by [Nova Nuggets](https://novanuggets.com) — Handcrafted Intelligence. Own Your AI.

---

## Why This Exists

The AI agent space has benchmarks for coding (SWE-Bench), task completion (APEX-Agents), tool calling (TAU2-Bench), and memory recall (MemoryArena). None of them evaluate a **persistent autonomous runtime** — an agent that runs 24/7, schedules its own work, talks to you on Telegram and Slack, remembers what you said last month, and does it all without going rogue.

That's what Digital Twin as a Service (DTaaS) requires. DTaaS-Bench is the first benchmark designed for this category.

---

## 10 Dimensions

| # | Dimension | Weight | What It Tests |
|---|-----------|--------|---------------|
| 1 | Autonomy Control | 0.15 | Safety constraints on background agent behavior |
| 2 | Memory Persistence | 0.15 | Durable recall across restarts, sessions, and time |
| 3 | Functional Capability | 0.15 | End-to-end task completion, multi-step reasoning, error recovery |
| 4 | Autonomous Execution | 0.12 | Scheduled and proactive task completion |
| 5 | Cross-Channel Consistency | 0.12 | Coherent state across communication surfaces |
| 6 | Integration Breadth | 0.08 | Functional channels, tools, memory backends, APIs |
| 7 | Security & Privacy | 0.08 | Data isolation, secret handling, audit, sandboxing |
| 8 | Scale & Cost Efficiency | 0.05 | Resource consumption per user, horizontal scaling |
| 9 | Operational Resilience | 0.05 | Recovery from crashes, network failures, corruption |
| 10 | Latency Profile | 0.05 | End-to-end responsiveness for critical user paths |

---

## Leaderboard (March 2026)

| Runtime | Type | Composite | Rating | Autonomy | Memory | Functional | Execution | Channels | Breadth | Security | Scale | Resilience | Latency |
|---------|------|-----------|--------|----------|--------|------------|-----------|----------|---------|----------|-------|------------|---------|
| **[Nullalis v0.1](results/nullalis-v0.1-report.md)** | Full runtime | **87** | **Category Leader** | 96 | 91 | 85 | 85 | 85 | 97 | 89 | 74 | 78 | 72 |
| OpenClaw (est.) | Full runtime | 62 | Competitive | 45 | 70 | 75 | 55 | 75 | 70 | 35 | 55 | 50 | 70 |
| NanoBot (est.) | Lightweight runtime | 52 | Emerging | 30 | 55 | 65 | 50 | 50 | 35 | 40 | 65 | 45 | 70 |
| Letta (est.) | Agent framework | 46 | Emerging | 30 | 85 | 55 | 25 | 15 | 35 | 40 | 55 | 55 | 65 |
| Mem0 (est.) | Memory platform | 41 | Specialized | 15 | 88 | 50 | 10 | 10 | 25 | 30 | 65 | 50 | 70 |

**Type** indicates what the product is designed to be. Not every entry is a full DTaaS runtime — some are frameworks or specialized components. The benchmark measures the full DTaaS surface; products focused on a subset will naturally score lower on dimensions outside their scope.

**Estimated scores** are based on publicly available documentation and architecture analysis (March 2026). OpenClaw supports 20+ channels and hybrid semantic memory search. NanoBot is a 4,000-line minimalist agent with Telegram/WhatsApp, scheduling, and persistent memory. Letta provides tiered self-editing memory with an agent development environment. Mem0 is a $24M-funded graph memory platform used as a component in larger systems. **We invite all runtimes to submit verified results.**

---

## Rating Tiers

| Score | Rating | Meaning |
|-------|--------|---------|
| 85-100 | **Category Leader** | Full DTaaS capability across all dimensions |
| 70-84 | **Production-Grade** | Strong coverage, ready for real users |
| 55-69 | **Competitive** | Solid in core areas, gaps in some dimensions |
| 40-54 | **Emerging** | Meaningful capability, partial DTaaS coverage |
| 25-39 | **Specialized** | Strong in specific dimensions, not full-stack DTaaS |
| <25 | **Early Stage** | Research or proof-of-concept |

---

## Quick Start

```bash
git clone https://github.com/ProjectNuggets/DTaaS-benchmark.git
cd DTaaS-benchmark
pip install -r harness/requirements.txt

# Run all 10 dimensions against a live runtime
python -m harness.runner \
  --url http://localhost:8080 \
  --token YOUR_INTERNAL_TOKEN \
  --user-id 1 \
  --name "My Runtime v1.0"

# Run specific dimensions
python -m harness.runner \
  --url http://localhost:8080 \
  --token YOUR_TOKEN \
  --user-id 1 \
  --dimensions memory,security,functional

# Generate reports (JSON + Markdown + HTML)
python -m harness.runner \
  --url http://localhost:8080 \
  --token YOUR_TOKEN \
  --user-id 1 \
  --name "My Runtime v1.0" \
  --output results/my-runtime.json \
  --markdown results/my-runtime.md \
  --html results/my-runtime.html
```

---

## Runtime API Contract

The harness tests any runtime that exposes these HTTP endpoints:

| Endpoint | Method | Purpose | Required |
|----------|--------|---------|----------|
| `/api/v1/chat/stream` | POST (SSE) | Send messages, receive streamed responses | Yes |
| `/health` | GET | Health check (200 = healthy) | Yes |
| `/internal/diagnostics` | GET | Runtime introspection (channels, tools, state) | Yes |
| `/metrics` | GET | Prometheus-format metrics | Optional |

### Authentication

```
X-Internal-Token: <token>
X-Zaki-User-Id: <user_id>
```

Or equivalent. Configure via `--token` and `--user-id` flags.

---

## What Gets Tested

### Autonomy Control
Does the runtime enforce safety constraints on background turns? Can it prevent shell access, block unauthorized auth flows, and suppress repeated spam — while still allowing bounded inspection and scheduling?

### Memory Persistence
Can the agent recall 100 facts after a restart? Does it handle paraphrased queries? Does recall hold up after 30 days of active use?

### Functional Capability
Can the agent actually do useful work? 23 tests across single-tool tasks, multi-step reasoning chains, error recovery, and conversational quality.

### Autonomous Execution
Can the agent schedule its own work and execute it on time? One-shot reminders, recurring jobs, conditional triggers — measured over real runtime operation.

### Cross-Channel Consistency
Does a fact stored via Telegram appear when queried via Slack? Does the conversation timeline stay coherent across channels?

### Integration Breadth
How many channels, tools, memory backends, and API integrations are functional (not stubbed)?

### Security & Privacy
Can the agent be tricked into path traversal, SSRF, or leaking secrets? Is tenant data isolated? Are background turns prevented from initiating auth flows?

### Scale & Cost Efficiency
How many concurrent users can one instance handle? What's the memory footprint per user? Can it scale horizontally?

### Operational Resilience
What happens when the process crashes mid-turn? Does state survive? Are messages duplicated?

### Latency Profile
How fast is the response path end-to-end? How much jitter do scheduled jobs have?

---

## Submit Your Results

We welcome results from any DTaaS runtime.

1. Run the harness against your runtime
2. Open an issue using the [Submit Results template](.github/ISSUE_TEMPLATE/submit-results.md)
3. Include your `results/<runtime>.json` output

All submitted results are published in the leaderboard with full transparency.

---

## Full Specification

See [SPECIFICATION.md](SPECIFICATION.md) for complete dimension definitions, scoring formulas, test protocols, and rules for fair comparison.

---

## Repository Structure

```
DTaaS-benchmark/
├── README.md               This file
├── SPECIFICATION.md         Full benchmark specification
├── LICENSE                  Apache-2.0
├── harness/
│   ├── runner.py            CLI entry point
│   ├── scorer.py            Composite score calculator
│   ├── report.py            Markdown + HTML report generator
│   ├── sse_client.py        SSE chat client
│   ├── config.py            Runtime connection config
│   └── dim1-10_*.py         10 dimension test scripts
├── fixtures/
│   ├── facts_100.json       100 test facts for memory dimension
│   ├── attack_payloads.json Path traversal + SSRF inputs
│   └── schedules.json       Task definitions
└── results/
    ├── nullalis-v0.1.json   Machine-readable results
    └── nullalis-v0.1-report.md  Human-readable report
```

---

## License

Apache-2.0. See [LICENSE](LICENSE).

---

## About Nova Nuggets

[Nova Nuggets](https://novanuggets.com) builds secure AI systems that belong to you. We don't believe in generic AI or rented intelligence. We design AI infrastructure that delivers from day one, automates real work, and evolves with your operations.

**Nullalis** (ZAKI BOT) is our autonomous agent runtime — a persistent digital twin that remembers, plans, acts, and follows up across every channel, under your control. It is the reference implementation for DTaaS-Bench and the first runtime to score Production-Ready (87/100).
