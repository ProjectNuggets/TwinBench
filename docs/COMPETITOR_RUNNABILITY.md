# Competitor Runnability Notes

TwinBench is intended to be approachable to outside runtime teams. This document exists so compatibility gaps are explained honestly rather than hidden behind optimistic wording.

This document tracks which nearby runtimes can be run directly against TwinBench today, and which still need an adapter or contract shim.

The point is to keep early comparison honest. A repo existing on disk is not the same as a reproducible benchmark submission.

## Local Candidates Seen

### Nullalis

Status: benchmark-ready now

Why:

- exposes `/health`
- exposes `/metrics`
- exposes `/internal/diagnostics`
- exposes `/api/v1/chat/stream`
- supports live benchmark execution with explicit `session_key`

## OpenClaw

Local path: `/Users/nova/Desktop/ALIS24_Final/openclaw-latest`

Status: adapter-ready candidate, not directly runnable on the TwinBench contract yet

Observed shape:

- mature gateway and health surfaces
- multi-channel architecture
- WebSocket-centric control plane
- broad operational docs and CLI tooling

Concrete local evidence from repo sweep:

- health and readiness HTTP routes are implemented in `src/gateway/server-http.ts`
- main gateway examples and dev tooling are centered on `ws://` or `wss://` targets
- no local evidence of the TwinBench chat contract at `/api/v1/chat/stream`
- session concepts exist, but not in the same HTTP+SSE surface the harness currently expects

Current benchmark gap:

- TwinBench expects HTTP + SSE chat on `/api/v1/chat/stream`
- local OpenClaw docs indicate the main control plane is gateway WebSocket / RPC oriented
- this likely requires either:
  - an adapter shim that exposes the TwinBench contract
  - or a benchmark transport extension for OpenClaw-style gateways

## PicoClaw

Local path: `/Users/nova/Desktop/picoclaw`

Status: interesting lightweight runtime, not directly runnable on the TwinBench contract yet

Observed shape:

- Go-based assistant runtime
- channel support and lightweight runtime internals
- strong lightweight/edge positioning

Concrete local evidence from repo sweep:

- `session_key` is present in internal agent and bus types
- multiple channel implementations use WebSocket-oriented transports
- no clear local HTTP gateway contract matching `/api/v1/chat/stream`
- no confirmed benchmark-facing `/internal/diagnostics` or `/metrics` surfaces in the local repo sweep

Current benchmark gap:

- no confirmed `/api/v1/chat/stream` endpoint in the local repo sweep
- no confirmed `/internal/diagnostics` or `/metrics` benchmark surfaces
- may need a benchmark adapter or a custom probe path

## What Counts as a Real Comparison

A runtime should only appear as a verified comparison artifact when:

- the benchmark runs against a live instance
- the runtime uses either the standard TwinBench contract or a documented adapter
- raw result artifacts are attached
- verified/projected separation is preserved

Until then, the repo should use wording like:

- `reference candidate`
- `local contract mismatch`
- `adapter required`

and avoid publishing leaderboard-like scores.

For public launch, the repo should distinguish between:

- `benchmark-ready now`
- `adapter-ready candidate`
- `external estimate only`
