#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"

INPUT_PDF="${1:-${REPO_ROOT}/pdfs/sagemaker-dg-8318.pdf}"
OUTPUT_DIR="${2:-${REPO_ROOT}/ml-output}"

if [[ ! -f "${INPUT_PDF}" ]]; then
  echo "Input PDF not found: ${INPUT_PDF}" >&2
  exit 1
fi

LOGICAL_CPU="$(sysctl -n hw.logicalcpu 2>/dev/null || echo 8)"
WORKERS="${WORKERS:-$(( LOGICAL_CPU > 2 ? LOGICAL_CPU - 2 : 1 ))}"
if (( WORKERS > 8 )); then
  WORKERS=8
fi

"${REPO_ROOT}/tools/setup_venv.sh"

"${REPO_ROOT}/.venv/bin/python3" "${REPO_ROOT}/tools/pdf_to_markdown.py" \
  --input "${INPUT_PDF}" \
  --output-dir "${OUTPUT_DIR}" \
  --workers "${WORKERS}" \
  --chunk-size 12 \
  --image-dpi 170 \
  --min-image-width 180 \
  --min-image-height 140 \
  --min-image-area 50000 \
  --overwrite

echo "Conversion complete. Output: ${OUTPUT_DIR}"
