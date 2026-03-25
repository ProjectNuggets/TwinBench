# Troubleshooting

This page covers the most common TwinBench failures.

## 1. Auth Mismatch

Symptoms:

- `401 Unauthorized`
- diagnostics unavailable
- chat stream rejected immediately

What it usually means:

- wrong internal token
- wrong auth header
- local runtime token changed

What to do:

- verify `/internal/diagnostics` manually
- verify `/api/v1/chat/stream` manually
- for local Nullalis, prefer `--token-from-nullalis-config`

## 2. Missing Diagnostics

Symptoms:

- `/internal/diagnostics` returns HTML, 404, or auth failure

What it usually means:

- runtime does not expose a machine-readable diagnostics surface
- route exists in a control UI only

What to do:

- mark the dimension as unsupported or partially measurable
- do not replace diagnostics with narrative claims

## 3. Missing Bootstrap

Symptoms:

- multi-user scale requests fail with `unknown_user_id`
- `/api/v1/users/provision` fails for benchmark users

What it usually means:

- tenant identity bootstrap is unavailable
- benchmark users do not exist in the runtime’s identity layer

What to do:

- treat multi-user scale as unavailable or partially measured
- do not interpret this as poor throughput by default

## 4. Contract Mismatch

Symptoms:

- no `/api/v1/chat/stream`
- no SSE response
- control plane is WS-first or CLI-first

What it usually means:

- runtime is real, but not directly TwinBench-compatible yet

What to do:

- use [INTEGRATION_PATHS.md](INTEGRATION_PATHS.md)
- classify it honestly as adapter-needed or partial

## 5. Long-Running Turns

Symptoms:

- the benchmark appears stuck on one dimension
- open-ended mode takes a very long time

What it usually means:

- the runtime is still working
- or a turn is blocked and needs bounded timeout policy

What to do:

- prefer bounded or adaptive timeouts for public runs
- use open-ended mode only when “faster is better” is the explicit benchmark policy
