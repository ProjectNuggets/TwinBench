# Integration Paths

This document helps runtime authors get to a valid TwinBench artifact without pretending they already match the full contract.

## Path 1: Native Contract

Best case.

Your runtime already exposes:

- `/api/v1/chat/stream`
- `/health`
- `/internal/diagnostics`
- optionally `/metrics`

Action:

- run the benchmark directly

## Path 2: Native Runtime, Different Public Shape

Your runtime is real and persistent, but the transport contract differs.

Examples:

- OpenAI-compatible chat surface
- WebSocket-first runtime
- CLI or control-plane-only diagnostics

Action:

- expose a documented TwinBench-compatible surface, or
- document a benchmark-native alternate profile before submission

Do not fake compatibility by rewriting results manually.

## Path 3: Tenant-Aware Runtime With Identity Bootstrap

Your runtime supports multiple users but requires provisioning or identity bootstrap first.

Action:

- ensure `/api/v1/users/provision` or equivalent is available
- run preflight
- attach a note if the runtime only supports a subset of benchmark users locally

## Path 4: Partial Runtime

Your runtime may only support some of the category today.

Action:

- run TwinBench anyway
- publish the artifact
- let measured coverage show what is real

This is better than an estimated or narrated score.
