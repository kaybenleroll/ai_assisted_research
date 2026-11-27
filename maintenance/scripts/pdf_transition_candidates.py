#!/usr/bin/env python3
"""List page transitions where extracted text begins with a figure caption.

Input is the form-feed-separated output of ``pdftotext -layout PDF -``.
Candidates are a prompt for visual inspection, not a verdict.
"""
import re
import sys
from pathlib import Path

CAPTION = re.compile(r"^(?:Figure|Fig\.)\s+\d+\s*:", re.IGNORECASE)


def candidates(text):
    for page, content in enumerate(text.split("\f"), 1):
        lines = [line.strip() for line in content.splitlines() if line.strip()]
        if page > 1 and lines and CAPTION.match(lines[0]):
            yield page - 1, page, lines[0]


def main():
    if len(sys.argv) != 2:
        print("Usage: pdf_transition_candidates.py EXTRACTED_TEXT", file=sys.stderr)
        return 2
    try:
        text = Path(sys.argv[1]).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(exc, file=sys.stderr)
        return 1
    found = list(candidates(text))
    for previous, page, caption in found:
        print(f"{previous}–{page}: {caption}")
    print(f"{len(found)} candidates; visually inspect both pages. "
          "Unlisted transitions are not cleared.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
