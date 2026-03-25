#!/usr/bin/env bash
set -euo pipefail

URL="${1:-}"
TOKEN="${2:-}"
USER_ID="${3:-1}"

if [[ -z "${URL}" ]]; then
  echo "usage: scripts/preflight.sh <url> [token] [user_id]"
  exit 1
fi

echo "== TwinBench preflight =="
echo "URL: ${URL}"
echo "User: ${USER_ID}"

echo
echo "-- /health"
curl -sS "${URL%/}/health" || true

echo
echo
echo "-- /internal/diagnostics"
if [[ -n "${TOKEN}" ]]; then
  curl -sS "${URL%/}/internal/diagnostics" \
    -H "X-Internal-Token: ${TOKEN}" \
    -H "X-Zaki-User-Id: ${USER_ID}" || true
else
  echo "token not provided, skipping authenticated diagnostics probe"
fi

echo
echo
echo "-- /api/v1/chat/stream"
if [[ -n "${TOKEN}" ]]; then
  curl -sS -N -X POST "${URL%/}/api/v1/chat/stream" \
    -H "Content-Type: application/json" \
    -H "X-Internal-Token: ${TOKEN}" \
    -H "X-Zaki-User-Id: ${USER_ID}" \
    --data "{\"message\":\"Say OK\",\"session_key\":\"agent:zaki-bot:user:${USER_ID}:thread:preflight\"}" || true
else
  echo "token not provided, skipping authenticated chat probe"
fi

echo
echo
echo "-- /metrics"
curl -sS "${URL%/}/metrics" || true

echo
echo
echo "-- /api/v1/users/provision"
if [[ -n "${TOKEN}" ]]; then
  curl -sS -X POST "${URL%/}/api/v1/users/provision" \
    -H "Content-Type: application/json" \
    -H "X-Internal-Token: ${TOKEN}" \
    -H "X-Zaki-User-Id: ${USER_ID}" \
    --data "{\"user_id\":\"${USER_ID}\"}" || true
else
  echo "token not provided, skipping provisioning probe"
fi

echo
echo
echo "== preflight complete =="
