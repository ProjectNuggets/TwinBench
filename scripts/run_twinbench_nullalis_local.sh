#!/usr/bin/env bash
set -euo pipefail

URL="${1:-http://127.0.0.1:3000}"
NAME="${2:-Nullalis Local}"
USER_ID="${3:-1}"
OUT_PREFIX="${4:-results/nullalis-local}"

python3.10 -m harness.runner \
  --url "${URL}" \
  --token-from-nullalis-config \
  --user-id "${USER_ID}" \
  --name "${NAME}" \
  --output "${OUT_PREFIX}.json" \
  --markdown "${OUT_PREFIX}.md" \
  --html "${OUT_PREFIX}.html"

echo
echo "Artifacts:"
echo "  ${OUT_PREFIX}.json"
echo "  ${OUT_PREFIX}.md"
echo "  ${OUT_PREFIX}.html"
