# Preflight Checklist

Use this before spending time on a full TwinBench run.

## 1. Health

```bash
curl -s http://localhost:8080/health
```

Expected:

- HTTP `200`
- machine-readable health payload

## 2. Auth

Confirm you can access protected surfaces with the intended token.

```bash
curl -s http://localhost:8080/internal/diagnostics \
  -H "X-Internal-Token: YOUR_TOKEN" \
  -H "X-Zaki-User-Id: 1"
```

Expected:

- not `401`
- not HTML fallback
- machine-readable JSON

## 3. Chat Contract

Confirm the runtime accepts the benchmark chat shape.

```bash
curl -s -N -X POST http://localhost:8080/api/v1/chat/stream \
  -H "Content-Type: application/json" \
  -H "X-Internal-Token: YOUR_TOKEN" \
  -H "X-Zaki-User-Id: 1" \
  --data '{"message":"Say OK","session_key":"agent:zaki-bot:user:1:thread:preflight"}'
```

Expected:

- SSE response
- `done` event

## 4. Metrics

```bash
curl -s http://localhost:8080/metrics
```

Metrics are optional, but useful for trusted interpretation.

## 5. User Provisioning

For tenant-aware runtimes, confirm benchmark users can be provisioned.

```bash
curl -s -X POST http://localhost:8080/api/v1/users/provision \
  -H "Content-Type: application/json" \
  -H "X-Internal-Token: YOUR_TOKEN" \
  -H "X-Zaki-User-Id: 2" \
  --data '{"user_id":"2"}'
```

If this fails with `unknown_user_id`, TwinBench can still run, but multi-user scale should be interpreted as bootstrap-limited.

## 6. Channel and Runtime Checks

Review diagnostics for:

- connected channels
- memory backend
- scheduler or heartbeat presence
- session key policy
- runtime mode and transport counters

If any of these are missing, do not guess. Note the gap in the artifact.
