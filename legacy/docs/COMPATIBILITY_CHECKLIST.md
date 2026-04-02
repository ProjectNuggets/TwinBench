# Compatibility Checklist

Use this checklist to determine whether a runtime is ready for TwinBench.

## Required

- `POST /api/v1/chat/stream` with SSE output
- `GET /health`
- `GET /internal/diagnostics`
- internal auth mechanism for protected surfaces
- explicit user context, usually via `X-Zaki-User-Id`

## Strongly Recommended

- `GET /metrics`
- explicit session key support
- runtime diagnostics that expose channels, memory, scheduler, and transport
- benchmark-user provisioning for tenant-aware deployments

## Auth Expectations

The harness currently supports:

- `X-Internal-Token`
- optional token discovery for local Nullalis via `--token-from-nullalis-config`

If your runtime uses another contract, document it before submitting results.

## User Provisioning Expectations

If your runtime is tenant-aware, one of these must be true:

- benchmark users can be provisioned before fanout
- benchmark users already exist and are documented

Otherwise TwinBench will treat multi-user readiness as unavailable, not as a clean throughput failure.

## Unsupported Is Fine

If your runtime is missing:

- diagnostics
- metrics
- multi-channel surfaces
- multi-user bootstrap

you can still run TwinBench. The result just needs to be honest about what was and was not measured.
