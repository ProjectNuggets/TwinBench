# Getting Started in 10 Minutes

TwinBench is the open benchmark for **personal AI assistant runtimes**.

If your runtime can remember, act, follow up, and stay safe over time, this guide gets you to a first artifact quickly.

## Step 1: Install

```bash
git clone https://github.com/ProjectNuggets/DTaaS-benchmark.git
cd DTaaS-benchmark
python3.10 -m pip install -r harness/requirements.txt
```

## Step 2: Confirm the runtime contract

Your runtime should expose:

- `POST /api/v1/chat/stream`
- `GET /health`
- `GET /internal/diagnostics`
- optionally `GET /metrics`

Use [docs/PREFLIGHT.md](PREFLIGHT.md) if you want a structured check.

## Step 3: Run the benchmark

If you want an agent to do this for you, use [AGENT_RUN_GUIDE.md](AGENT_RUN_GUIDE.md).

Generic runtime:

```bash
python3.10 -m harness.runner \
  --url http://localhost:8080 \
  --token YOUR_TOKEN \
  --user-id 1 \
  --name "My Runtime" \
  --output results/my-runtime.json \
  --markdown results/my-runtime.md \
  --html results/my-runtime.html
```

Local Nullalis:

```bash
python3.10 -m harness.runner \
  --url http://127.0.0.1:3000 \
  --token-from-nullalis-config \
  --user-id 1 \
  --name "Nullalis Local" \
  --output results/nullalis-local.json \
  --markdown results/nullalis-local.md \
  --html results/nullalis-local.html
```

## Step 4: Read the artifact

Pay attention to:

- `verified_composite_score`
- `projected_composite_score`
- `measured_coverage`
- `coverage_adjusted_verified_score`
- `dimension_status`
- `dimension_reason_codes`

## Step 5: Publish it

Use [docs/HOW_TO_SUBMIT.md](HOW_TO_SUBMIT.md) and attach:

- result JSON
- Markdown or HTML report
- runtime version or commit SHA
- diagnostics snapshot
- metrics snapshot when available

## If Your Runtime Is Not Contract-Compatible Yet

Do not force it. Start with:

- [docs/COMPATIBILITY_CHECKLIST.md](COMPATIBILITY_CHECKLIST.md)
- [docs/INTEGRATION_PATHS.md](INTEGRATION_PATHS.md)

TwinBench is strongest when unsupported behavior is reported honestly rather than hidden.

If something goes wrong, start with [TROUBLESHOOTING.md](TROUBLESHOOTING.md).
