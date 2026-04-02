#!/usr/bin/env bash
set -euo pipefail

URL="${1:-http://127.0.0.1:3000}"
NAME="${2:-Nullalis Local}"
USER_ID="${3:-1}"
OUT_PREFIX="${4:-results/nullalis-local}"
PYTHON_BIN="${PYTHON:-$(command -v python3.10 2>/dev/null || command -v python3)}"

if command -v uv >/dev/null 2>&1 && command -v /opt/homebrew/bin/python3 >/dev/null 2>&1; then
  RUNNER=(uv run --python /opt/homebrew/bin/python3 --with-requirements harness/requirements.txt python)
else
  RUNNER=("${PYTHON_BIN}")
fi

"${RUNNER[@]}" -m harness.runner \
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
