#!/usr/bin/env python3
"""Validate the structural contract for a primer brief and evidence audit.

This checker deliberately validates form and completeness only.  It does not
decide whether a cited passage teaches the claimed mechanism.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROUTE_TIERS = {"primary", "alternative", "reference-only"}
STATUSES = {"verified", "gap", "scope-reduced", "not-checked"}
READINESS = {"ready", "not-ready"}
ID_RE = re.compile(r"^[a-z][a-z0-9_-]*$")
REVISION_RE = re.compile(r"^[0-9a-f]{7,64}$|^[A-Za-z0-9._/-]+@[0-9a-f]{7,64}$")
LOCATOR_RE = re.compile(r"^(?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_.-]+:[1-9][0-9]*$")
MISSING_RE = re.compile(r"^MISSING(?:\s+[—-].+|\s*:.+)?$", re.I)
PLACEHOLDER_RE = re.compile(r"<[^>]+>|\b(?:TODO|TBD|FIXME)\b|^\.\.\.$", re.I)

BRIEF_FIELDS = (
    "Issue and milestone", "Brief revision", "Source revision", "Reader", "Prerequisites", "Problem and motivation",
    "Intended outcome", "Scope", "Exclusions", "Proposed dependency-led route",
    "Teaching-case contract", "Core-concept depth matrix",
    "Route classification and teaching spines",
)
AUDIT_FIELDS = (
    "Starting branch", "Audit revision", "Source revision", "Reviewer(s)", "Date", "Reviewed revision",
    "Brief reviewed", "Review boundary", "Core-concept depth matrix",
)


class Row:
    def __init__(self, values: dict[str, str], line: int, malformed: bool = False):
        self.values = values
        self.line = line
        self.malformed = malformed


def _clean(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().strip("`"))


def _is_placeholder(value: str) -> bool:
    return not value or bool(PLACEHOLDER_RE.search(value))


def _metadata(text: str, required: tuple[str, ...], errors: list[str], kind: str) -> dict[str, str]:
    found: dict[str, str] = {}
    for number, line in enumerate(text.splitlines(), 1):
        match = re.match(r"^\s*-\s*([^:]+):\s*(.*?)\s*$", line)
        if match:
            found[_clean(match.group(1))] = _clean(match.group(2))
    for field in required:
        value = found.get(field, "")
        if _is_placeholder(value):
            errors.append(f"{kind}: missing or placeholder metadata '{field}'")
    return found


def _headings(text: str) -> set[str]:
    return {match.group(1).strip() for line in text.splitlines()
            if (match := re.match(r"^##\s+(.+?)\s*$", line))}


def _tables(text: str) -> list[tuple[int, list[str], list[Row]]]:
    lines = text.splitlines()
    result = []
    index = 0
    while index < len(lines) - 1:
        if "|" not in lines[index] or not re.match(r"^\s*\|?\s*:?-{3,}", lines[index + 1]):
            index += 1
            continue
        headers = [_clean(x) for x in lines[index].strip().strip("|").split("|")]
        rows: list[Row] = []
        index += 2
        while index < len(lines) and "|" in lines[index] and lines[index].strip():
            values = [_clean(x) for x in lines[index].strip().strip("|").split("|")]
            rows.append(Row(dict(zip(headers, values)), index + 1, len(values) != len(headers)))
            index += 1
        result.append((index - len(rows) - 2, headers, rows))
    return result


def _pick(headers: list[str], *names: str) -> str | None:
    normal = {re.sub(r"[^a-z0-9]", "", h.lower()): h for h in headers}
    for name in names:
        key = re.sub(r"[^a-z0-9]", "", name.lower())
        if key in normal:
            return normal[key]
    return None


def _require_table(tables, required: tuple[str, ...], kind: str, errors: list[str]):
    for _, headers, rows in tables:
        if all(_pick(headers, field) for field in required):
            return headers, rows
    errors.append(f"{kind}: required matrix table is missing or has wrong columns")
    return [], []


def _check_ids(rows: list[Row], route_col: str, concept_col: str, errors: list[str], kind: str):
    seen: set[tuple[str, str]] = set()
    for row in rows:
        route = row.values.get(route_col, "")
        concept = row.values.get(concept_col, "")
        if not ID_RE.fullmatch(route):
            errors.append(f"{kind}:{row.line}: invalid route_id '{route}'")
        if not ID_RE.fullmatch(concept):
            errors.append(f"{kind}:{row.line}: invalid concept_id '{concept}'")
        key = (route, concept)
        if key in seen:
            errors.append(f"{kind}:{row.line}: duplicate route_id/concept_id '{route}/{concept}'")
        seen.add(key)


def validate(brief_path: Path, audit_path: Path) -> list[str]:
    errors: list[str] = []
    try:
        brief = brief_path.read_text(encoding="utf-8")
        audit = audit_path.read_text(encoding="utf-8")
    except OSError as exc:
        return [str(exc)]
    except UnicodeDecodeError as exc:
        return [f"non-UTF-8 evidence file: {exc.filename}"]

    brief_meta = _metadata(brief, BRIEF_FIELDS, errors, "brief")
    audit_meta = _metadata(audit, AUDIT_FIELDS, errors, "audit")
    if "Core-concept depth matrix" not in _headings(brief):
        errors.append("brief: required section 'Core-concept depth matrix' is missing")
    if "Adversarial depth gate" not in _headings(audit):
        errors.append("audit: required section 'Adversarial depth gate' is missing")
    if "Readiness decision" not in audit_meta:
        errors.append("audit: missing metadata 'Readiness decision'")
    brief_revision = brief_meta.get("Source revision", "")
    audit_revision = audit_meta.get("Reviewed revision", "")
    if brief_revision and not REVISION_RE.fullmatch(brief_revision):
        errors.append("brief: Reviewed revision is not a commit-like revision")
    if audit_revision and not REVISION_RE.fullmatch(audit_revision):
        errors.append("audit: Reviewed revision is not a commit-like revision")
    if brief_revision and audit_revision and brief_revision != audit_revision:
        errors.append("brief and audit: Source/Reviewed revision does not match")
    if brief_revision and audit_meta.get("Source revision") and brief_revision != audit_meta["Source revision"]:
        errors.append("brief and audit: Source revision does not match")

    brief_required = ("Route tier", "Route ID", "Concept ID", "Reader action", "Mechanism or reasoning",
                      "Significance", "Teaching device", "Worked evidence", "Interpretation", "Limitations",
                      "Downstream use", "Evidence/source plan")
    _, brief_rows = _require_table(_tables(brief), brief_required, "brief", errors)
    audit_required = ("Route tier", "Route ID", "Concept ID", "Explanation locator", "Example/action locator",
                      "Interpretation locator", "Limitation locator", "Evidence revision", "Reviewer", "Status",
                      "Finding", "Scope decision")
    _, audit_rows = _require_table(_tables(audit), audit_required, "audit", errors)
    if not brief_rows:
        errors.append("brief: core-concept depth matrix must contain at least one row")
    if not audit_rows:
        errors.append("audit: adversarial depth gate must contain at least one row")
    if not brief_rows or not audit_rows:
        return errors

    brief_headers = brief_rows[0].values
    audit_headers = audit_rows[0].values
    bcols = {re.sub(r"[^a-z0-9]", "", key.lower()): key for key in brief_headers}
    acols = {re.sub(r"[^a-z0-9]", "", key.lower()): key for key in audit_headers}
    def b(name): return bcols[re.sub(r"[^a-z0-9]", "", name.lower())]
    def a(name): return acols[re.sub(r"[^a-z0-9]", "", name.lower())]
    _check_ids(brief_rows, b("Route ID"), b("Concept ID"), errors, "brief")
    _check_ids(audit_rows, a("Route ID"), a("Concept ID"), errors, "audit")
    expected: dict[tuple[str, str], str] = {}
    for row in brief_rows:
        if row.malformed:
            errors.append(f"brief:{row.line}: malformed matrix row has the wrong number of columns")
            continue
        tier = row.values[b("Route tier")]
        if tier not in ROUTE_TIERS:
            errors.append(f"brief:{row.line}: invalid route tier '{tier}'")
        for field in brief_required[3:]:
            if _is_placeholder(row.values[b(field)]):
                errors.append(f"brief:{row.line}: missing or placeholder '{field}'")
        expected[(row.values[b("Route ID")], row.values[b("Concept ID")])] = tier

    audited: set[tuple[str, str]] = set()
    for row in audit_rows:
        if row.malformed:
            errors.append(f"audit:{row.line}: malformed matrix row has the wrong number of columns")
            continue
        key = (row.values[a("Route ID")], row.values[a("Concept ID")])
        if key not in expected:
            errors.append(f"audit:{row.line}: row has no matching brief route/concept ID")
        else:
            if row.values[a("Route tier")] != expected[key]:
                errors.append(f"audit:{row.line}: route tier disagrees with brief for '{key[0]}/{key[1]}'")
        audited.add(key)
        status = row.values[a("Status")]
        if status not in STATUSES:
            errors.append(f"audit:{row.line}: invalid status '{status}'")
        if row.values[a("Route tier")] not in ROUTE_TIERS:
            errors.append(f"audit:{row.line}: invalid route tier '{row.values[a('Route tier')]}'")
        for field in ("Explanation locator", "Example/action locator", "Interpretation locator", "Limitation locator"):
            locator = row.values[a(field)]
            if status == "verified":
                valid_locator = bool(LOCATOR_RE.fullmatch(locator))
            else:
                valid_locator = bool(LOCATOR_RE.fullmatch(locator) or MISSING_RE.fullmatch(locator))
            if not valid_locator:
                errors.append(f"audit:{row.line}: invalid exact locator in '{field}'")
        if not REVISION_RE.fullmatch(row.values[a("Evidence revision")]):
            errors.append(f"audit:{row.line}: invalid evidence revision")
        if row.values[a("Evidence revision")] != audit_revision:
            errors.append(f"audit:{row.line}: evidence revision does not match audit revision")
        for field in ("Reviewer", "Finding", "Scope decision"):
            if _is_placeholder(row.values[a(field)]):
                errors.append(f"audit:{row.line}: missing or placeholder '{field}'")
        if status == "scope-reduced" and not row.values[a("Scope decision")].strip():
            errors.append(f"audit:{row.line}: scope-reduced status requires a scope rationale")
    for key in expected:
        if key not in audited:
            errors.append(f"audit: missing coverage for '{key[0]}/{key[1]}'")

    readiness = audit_meta.get("Readiness decision", "")
    if _is_placeholder(readiness) or readiness not in READINESS:
        errors.append("audit: Readiness decision must be 'ready' or 'not-ready'")
    if readiness == "ready":
        for row in audit_rows:
            key = (row.values[a("Route ID")], row.values[a("Concept ID")])
            if expected.get(key) in {"primary", "alternative"} and row.values[a("Status")] in {"gap", "not-checked"}:
                errors.append(f"audit:{row.line}: blocking {row.values[a('Status')]} prevents ready status")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("brief", type=Path)
    parser.add_argument("audit", type=Path)
    args = parser.parse_args(argv)
    errors = validate(args.brief, args.audit)
    if errors:
        print("primer evidence check failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"primer evidence check passed: {args.brief} + {args.audit}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
