#!/usr/bin/env python3
"""Report D10 filler density using the sole word list in House/Filler.yml."""

import re
import sys
from pathlib import Path


def terms() -> list[str]:
    source = Path(".vale/styles/House/Filler.yml").read_text(encoding="utf-8")
    values = re.findall(r"^  - ((?:\(\?<!not \))?[a-z ]+)$", source, re.MULTILINE)
    if not values:
        raise ValueError("House/Filler.yml has no filler terms")
    return values


def prose(source: str) -> str:
    source = re.sub(r"(?ms)^\s*(`{3,}|~{3,}).*?^\s*\1.*?$", " ", source)
    source = re.sub(r"(?s)\$\$.*?\$\$", " ", source)
    source = re.sub(r"\$[^$\n]+\$", " ", source)
    source = re.sub(r"`[^`\n]+`", " ", source)
    source = re.sub(r"(?m)^\s*>.*$", " ", source)
    source = re.sub(r"\]\([^)]*\)", "]", source)
    return source


def main() -> int:
    patterns = terms()
    filler = re.compile(r"\b(?:" + "|".join(t if t.startswith("(?<!") else re.escape(t) for t in patterns) + r")\b", re.I)
    for path in sys.argv[1:]:
        text = prose(Path(path).read_text(encoding="utf-8"))
        words = len(re.findall(r"\b[\w'-]+\b", text))
        hits = len(filler.findall(text))
        rate = hits * 1000 / words if words else 0.0
        if rate > 1.0:
            print(f"ADVISORY FILLER_DENSITY {path}: {hits}/{words} words ({rate:.2f} per 1,000; threshold 1.00)")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError) as exc:
        print(f"filler density error: {exc}", file=sys.stderr)
        sys.exit(2)
