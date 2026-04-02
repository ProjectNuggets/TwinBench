#!/usr/bin/env bash
set -euo pipefail

URL="${1:-http://127.0.0.1:8090}"
TOKEN="${2:-demo-internal-token}"
NAME="${3:-TwinBench Demo Runtime}"
USER_ID="${4:-demo-user}"
OUT_PREFIX="${5:-results/twinbench-demo-runtime}"
PYTHON_BIN="${PYTHON:-$(command -v python3.10 2>/dev/null || command -v python3)}"

if command -v uv >/dev/null 2>&1 && command -v /opt/homebrew/bin/python3 >/dev/null 2>&1; then
  RUNNER=(uv run --python /opt/homebrew/bin/python3 --with-requirements harness/requirements.txt python)
else
  RUNNER=("${PYTHON_BIN}")
fi

"${RUNNER[@]}" -m harness.runner \
  --url "${URL}" \
  --token "${TOKEN}" \
  --user-id "${USER_ID}" \
  --name "${NAME}" \
  --skip-schedule-wait \
  --memory-sample-size 5 \
  --scale-concurrency 3 \
  --output "${OUT_PREFIX}.json" \
  --markdown "${OUT_PREFIX}.md" \
  --html "${OUT_PREFIX}.html"

echo
echo "Artifacts:"
echo "  ${OUT_PREFIX}.json"
echo "  ${OUT_PREFIX}.md"
echo "  ${OUT_PREFIX}.html"
