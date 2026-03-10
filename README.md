# DTaaS-Bench

**The first industry benchmark for persistent autonomous AI agent runtimes.**

Published by [Nova Nuggets](https://novanuggets.com) — Handcrafted Intelligence. Own Your AI.

---

## What Is This?

DTaaS-Bench evaluates **Digital Twin as a Service** runtimes — persistent, autonomous agent systems that remember, plan, act, and follow up across multiple channels.

Existing benchmarks miss this category:
- **Industrial digital twin benchmarks** (AWS IoT TwinMaker, Azure Digital Twins) measure IoT simulation — not AI agents.
- **AI agent benchmarks** (SWE-Bench, VitaBench, APEX-Agents) measure isolated task completion — not persistent autonomous runtimes.

DTaaS-Bench measures what matters for a production digital twin: memory persistence, autonomy control, cross-channel consistency, security, scale, and resilience.

## Dimensions (9)

| # | Dimension | Weight | What It Tests |
|---|-----------|--------|---------------|
| 1 | Autonomy Control | 0.20 | Safety constraints on background agent behavior |
| 2 | Memory Persistence | 0.20 | Durable recall across restarts, sessions, and time |
| 3 | Autonomous Execution | 0.15 | Scheduled and proactive task completion |
| 4 | Cross-Channel Consistency | 0.15 | Coherent state across communication surfaces |
| 5 | Integration Breadth | 0.10 | Functional channels, tools, backends, APIs |
| 6 | Security & Privacy | 0.08 | Data isolation, secret handling, audit, sandboxing |
| 7 | Scale & Cost Efficiency | 0.05 | Resource consumption per user, horizontal readiness |
| 8 | Operational Resilience | 0.05 | Recovery from crashes, network failures, corruption |
| 9 | Latency Profile | 0.02 | End-to-end responsiveness for critical paths |

## Rating Tiers

| Score | Rating |
|-------|--------|
| 90-100 | SOTA (State of the Art) |
| 75-89 | Production-Ready |
| 60-74 | Beta |
| 40-59 | Prototype |
| <40 | Experimental |

## Quick Start

```bash
git clone https://github.com/ProjectNuggets/DTaaS-benchmark.git
cd DTaaS-benchmark
pip install -r harness/requirements.txt

# Run against a live runtime
python harness/runner.py \
  --url http://localhost:8080 \
  --token YOUR_INTERNAL_TOKEN \
  --user-id 1

# Run specific dimensions only
python harness/runner.py \
  --url http://localhost:8080 \
  --token YOUR_TOKEN \
  --user-id 1 \
  --dimensions memory,security,breadth

# Generate HTML report
python harness/runner.py \
  --url http://localhost:8080 \
  --token YOUR_TOKEN \
  --user-id 1 \
  --output results/my-runtime.json \
  --html results/my-runtime.html
```

## Runtime API Contract

The harness communicates with runtimes via HTTP. Required endpoints:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/v1/chat/stream` | POST (SSE) | Send messages, receive streamed responses |
| `/health` | GET | Health check (200 = healthy) |
| `/internal/diagnostics` | GET | Runtime info (channels, tools, backends, state) |
| `/metrics` | GET | Prometheus metrics (optional) |

### Authentication

```
X-Internal-Token: <token>
X-Zaki-User-Id: <user_id>
```

Or equivalent auth mechanism for your runtime. Configure via `--token` and `--user-id`.

## Results

| Runtime | Score | Rating | Date |
|---------|-------|--------|------|
| [Nullalis v0.1](results/nullalis-v0.1-report.md) | **89** | Production-Ready | 2026-03-09 |

## Submit Your Results

We welcome results from any DTaaS runtime. See [SPECIFICATION.md](SPECIFICATION.md) for the full protocol.

To submit:
1. Run the harness against your runtime
2. Open an issue using the [Submit Results template](.github/ISSUE_TEMPLATE/submit-results.md)
3. Include your `results/<runtime>.json` output

## Full Specification

See [SPECIFICATION.md](SPECIFICATION.md) for complete dimension definitions, metrics, scoring formulas, and rules for fair comparison.

## License

Apache-2.0. See [LICENSE](LICENSE).

## About Nova Nuggets

Nova Nuggets builds secure AI systems that belong to you. Nullalis (ZAKI BOT) is our autonomous agent runtime: a persistent digital twin that remembers, plans, acts, and follows up — across every channel, under your control.

[novanuggets.com](https://novanuggets.com)
