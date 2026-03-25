#!/usr/bin/env bash
set -euo pipefail

URL="${1:-}"
TOKEN="${2:-}"
NAME="${3:-External Runtime}"
USER_ID="${4:-1}"

if [[ -z "${URL}" || -z "${TOKEN}" ]]; then
  echo "usage: scripts/run_twinbench.sh <url> <token> [name] [user_id]"
  exit 1
fi

SLUG="$(echo "${NAME}" | tr '[:upper:]' '[:lower:]' | tr ' /' '--' | tr -cd 'a-z0-9-_')"
OUT_JSON="results/${SLUG}.json"
OUT_MD="results/${SLUG}.md"
OUT_HTML="results/${SLUG}.html"

python3.10 -m harness.runner \
  --url "${URL}" \
  --token "${TOKEN}" \
  --user-id "${USER_ID}" \
  --name "${NAME}" \
  --output "${OUT_JSON}" \
  --markdown "${OUT_MD}" \
  --html "${OUT_HTML}"

echo
echo "Artifacts:"
echo "  ${OUT_JSON}"
echo "  ${OUT_MD}"
echo "  ${OUT_HTML}"

python3.10 - <<PY
import json
from pathlib import Path
p = Path("${OUT_JSON}")
results = json.loads(p.read_text())
print("Verified:", results.get("verified_composite_score"))
print("Projected:", results.get("projected_composite_score"))
print("Coverage:", results.get("measured_coverage"))
print("Coverage-adjusted verified:", results.get("coverage_adjusted_verified_score"))
print("Dimension status:", results.get("dimension_status"))
print("Dimension reason codes:", results.get("dimension_reason_codes"))
PY
