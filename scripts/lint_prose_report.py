#!/usr/bin/env python3
"""Classify Vale JSON findings and verify the House fixtures."""

import json
import sys
from collections import Counter
from pathlib import Path


RULES = (
    "AsciiDash", "Directional", "Filler", "FillerCluster", "HeadingCase", "HeadingMinor",
    "Hedging", "LogicalPunctuation", "Timeless", "USDate", "WeaselWords",
)


def manifest(name: str, primer_only: bool = False) -> set[str]:
    entries: set[str] = set()
    for raw in Path("lint", name).read_text(encoding="utf-8").splitlines():
        path = raw.strip()
        if not path or path.startswith("#"):
            continue
        in_scope = path == "README.md" or ("/" in path and path.split("/", 1)[0].startswith(("primer_", "gaming_silo_rpg")))
        if not in_scope or path.count("/") > 1 or not Path(path).is_file() or (primer_only and not path.startswith("primer_")):
            raise ValueError(f"{name}: stale or out-of-scope path: {path}")
        if path in entries:
            raise ValueError(f"{name}: duplicate path: {path}")
        entries.add(path)
    return entries


def date_baseline() -> set[tuple[str, str]]:
    exceptions: set[tuple[str, str]] = set()
    for raw in Path("lint/vale-usdate-existing.txt").read_text(encoding="utf-8").splitlines():
        row = raw.strip()
        if not row or row.startswith("#"):
            continue
        parts = row.split("|", 1)
        if len(parts) != 2 or not Path(parts[0]).is_file() or not parts[1]:
            raise ValueError(f"invalid US-date baseline row: {row}")
        key = (parts[0], parts[1])
        if key in exceptions:
            raise ValueError(f"duplicate US-date baseline row: {row}")
        exceptions.add(key)
    return exceptions


def main() -> int:
    mode, *paths = sys.argv[1:]
    findings = json.load(sys.stdin)
    if not isinstance(findings, dict):
        raise ValueError("Vale output is not a file-to-alert mapping")
    if mode == "--fixtures":
        expected = {f"lint/fixtures/vale/{rule}-{kind}.md"
                    for rule in RULES for kind in ("pass", "fail")}
        if set(paths) != expected:
            raise ValueError("fixture paths do not match the House rule pairs")
        failures = []
        for rule in RULES:
            passed = f"lint/fixtures/vale/{rule}-pass.md"
            failed = f"lint/fixtures/vale/{rule}-fail.md"
            if findings.get(passed):
                failures.append(f"{passed}: unexpected findings {findings[passed]}")
            if not any(a.get("Check") == f"House.{rule}"
                       for a in findings.get(failed, [])):
                failures.append(f"{failed}: missing House.{rule} finding")
        for failure in failures:
            print(f"FAIL {failure}", file=sys.stderr)
        print(f"SUMMARY Vale fixtures pairs={len(RULES)} failures={len(failures)}")
        return bool(failures)

    if mode != "--report":
        raise ValueError(f"unknown mode: {mode}")
    allowed = set(paths)
    spelling = manifest("enforced-spelling.txt")
    headings = manifest("enforced-headings.txt")
    existing_dates = date_baseline()
    seen_dates: set[tuple[str, str]] = set()
    rules = Counter()
    files = Counter()
    enforced = advisory = 0
    for path in sorted(findings):
        if path not in allowed:
            raise ValueError(f"Vale returned an unexpected path: {path}")
        for alert in findings[path]:
            rule = alert.get("Check", "")
            if not rule.startswith("House."):
                raise ValueError(f"non-House rule in Vale output: {rule}")
            name = rule.removeprefix("House.")
            if name not in RULES:
                raise ValueError(f"unknown House rule: {rule}")
            line = alert.get("Line")
            if not isinstance(line, int):
                raise ValueError(f"missing Vale line for {path}: {alert}")
            severity = alert.get("Severity", "")
            baseline_key = (path, alert.get("Match", ""))
            is_existing_date = name == "USDate" and baseline_key in existing_dates
            if is_existing_date:
                if baseline_key in seen_dates:
                    raise ValueError(f"duplicate US-date baseline finding: {baseline_key}")
                seen_dates.add(baseline_key)
            category = "ENFORCED" if (name == "Hedging" or
                      (name == "USDate" and path in spelling and not is_existing_date) or
                      (name in ("HeadingCase", "HeadingMinor") and path in headings)) else "ADVISORY"
            enforced += category == "ENFORCED"
            advisory += category == "ADVISORY"
            files[path] += 1
            rules[name] += 1
            print(f"{category} {path}:{line} {rule} {severity}: {alert.get('Message', '')}")
    for key in existing_dates:
        if key[0] in allowed and key not in seen_dates:
            raise ValueError(f"stale US-date baseline row: {key[0]}|{key[1]}")
    for path in paths:
        print(f"BASELINE {path}: {files[path]}")
    for rule in RULES:
        print(f"BASELINE House.{rule}: {rules[rule]}")
    print(f"SUMMARY Vale files={len(paths)} enforced={enforced} advisory={advisory}")
    return bool(enforced)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"Vale reporting error: {exc}", file=sys.stderr)
        sys.exit(2)
