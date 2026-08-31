#!/usr/bin/env bash
set -euo pipefail

MODE="${MODE:-dev}"
source ./render.env

if [[ "$MODE" == "full" ]]; then
  export RENDER_N_SIMS="${FULL_N_SIMS}"
else
  export RENDER_N_SIMS="${DEV_N_SIMS}"
fi

export SEED_R
export SEED_PY
export RETICULATE_PYTHON="/usr/bin/python3"

mkdir -p "$OUTPUT_DIR"
quarto render workbook_elt.qmd --to html
rm -f "$OUTPUT_DIR/workbook_elt.html"
mv workbook_elt.html "$OUTPUT_DIR/workbook_elt.html"
rm -rf workbook_elt_files
rm -rf "$OUTPUT_DIR/workbook_elt_files"
