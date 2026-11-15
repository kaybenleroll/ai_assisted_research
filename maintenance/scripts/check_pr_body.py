#!/usr/bin/env python3
"""Require an issue reference or a reason for omitting one in a PR body."""

import os
import re
import sys


REFERENCE = re.compile(
    r"(?:Closes|Fixes|Resolves|Refs) "
    r"(?:[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)?#[1-9][0-9]*",
    re.IGNORECASE,
)
NO_ISSUE = re.compile(r"No-issue:\s*\S.*", re.IGNORECASE)


def main() -> int:
    body = os.environ.get("PR_BODY")
    if body is None:
        body = sys.stdin.read()

    first_line = next((line.strip() for line in body.splitlines() if line.strip()), "")
    if REFERENCE.fullmatch(first_line) or NO_ISSUE.fullmatch(first_line):
        return 0

    print(
        "The first non-blank PR body line must be Closes #N, Fixes #N, "
        "Resolves #N, Refs #N (owner/repo#N is also accepted), "
        "or No-issue: <non-empty reason>.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
