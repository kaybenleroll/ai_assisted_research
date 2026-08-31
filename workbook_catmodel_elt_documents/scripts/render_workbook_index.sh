#!/usr/bin/env bash
set -euo pipefail

source ./render.env
mkdir -p "$OUTPUT_DIR"
quarto render workbook_executable_index.qmd --to html
rm -f "$OUTPUT_DIR/workbook_executable_index.html"
mv workbook_executable_index.html "$OUTPUT_DIR/workbook_executable_index.html"
rm -rf workbook_executable_index_files
rm -rf "$OUTPUT_DIR/workbook_executable_index_files"
