# Agent Run Guide

This guide is optimized for machine operators and coding agents such as Codex, Claude Code, and Cursor.

## Goal

Produce a TwinBench artifact pack for a runtime and summarize the result.

## Generic One-Line Command

```bash
python3.10 -m harness.runner --url YOUR_URL --token YOUR_TOKEN --user-id 1 --name "Your Runtime" --output results/your-runtime.json --markdown results/your-runtime.md --html results/your-runtime.html
```

## Local Nullalis One-Line Command

```bash
python3.10 -m harness.runner --url http://127.0.0.1:3000 --token-from-nullalis-config --user-id 1 --name "Nullalis Local" --output results/nullalis-local.json --markdown results/nullalis-local.md --html results/nullalis-local.html
```

## Copy-Paste Agent Prompt

```text
Run TwinBench against this runtime at URL X using token Y. First perform the preflight checks, then run the harness, save JSON, Markdown, and HTML artifacts, and summarize the verified score, projected score, measured coverage, dimension statuses, and any unavailable dimensions with reason codes.
```

## Scripted Shortcuts

```bash
bash scripts/preflight.sh YOUR_URL YOUR_TOKEN 1
bash scripts/run_twinbench.sh YOUR_URL YOUR_TOKEN "Your Runtime" 1
bash scripts/run_twinbench_nullalis_local.sh
```

Or with `make`:

```bash
make preflight URL=YOUR_URL TOKEN=YOUR_TOKEN
make run URL=YOUR_URL TOKEN=YOUR_TOKEN NAME="Your Runtime"
make run-nullalis
```

## Required Preflight Sequence

1. Check `/health`
2. Check `/internal/diagnostics` with auth
3. Check `/api/v1/chat/stream` with a small SSE probe
4. Check `/metrics` if available
5. For tenant-aware runtimes, test `/api/v1/users/provision`

Use [PREFLIGHT.md](PREFLIGHT.md) for concrete commands.

## Expected Outputs

- `results/<runtime>.json`
- `results/<runtime>.md`
- `results/<runtime>.html`

Recommended extras:

- diagnostics snapshot
- metrics snapshot
- one short incident note

## How to Interpret Failures

- `401` usually means auth mismatch
- `404 unknown_user_id` during multi-user fanout usually means bootstrap is unavailable, not poor throughput
- missing diagnostics or metrics should be recorded as unsupported, not guessed
- same-user serialization is diagnostic behavior, not a failed multi-user scale claim

## Submission Path

After the run:

1. review `verified`, `projected`, `measured_coverage`
2. review `dimension_status` and `dimension_reason_codes`
3. attach the artifact pack using [HOW_TO_SUBMIT.md](HOW_TO_SUBMIT.md)
