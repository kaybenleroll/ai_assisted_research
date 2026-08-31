#!/usr/bin/env bash
set -euo pipefail

source ./render.env
mkdir -p "$OUTPUT_DIR"
quarto render workbook_quickstart.qmd --to html
rm -f "$OUTPUT_DIR/workbook_quickstart.html"
mv workbook_quickstart.html "$OUTPUT_DIR/workbook_quickstart.html"
rm -rf workbook_quickstart_files
rm -rf "$OUTPUT_DIR/workbook_quickstart_files"
