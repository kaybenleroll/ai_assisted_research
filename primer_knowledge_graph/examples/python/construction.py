"""A deliberately narrow, deterministic source-to-claim demonstration."""

import json
from pathlib import Path
import re

SOURCE_RECORDS = Path(__file__).resolve().parents[1] / "source_records.json"
METHOD = "northbridge-patterns-v1"
DATE = r"\d{4}-\d{2}-\d{2}"
PATTERNS = (
    re.compile(rf"Travel Policy v(?P<version>[12]) applies to Atlas from (?P<start>{DATE}) until (?P<end>{DATE})\."),
    re.compile(rf"On (?P<start>{DATE}), version (?P<version>[12]) (?P<verb>applies|does not apply) to Atlas\."),
    re.compile(rf"Travel Policy v(?P<version>[12]) applies to Atlas from (?P<start>{DATE}) without a stated end\."),
)


def extract(record):
    """Extract only the declared sentence forms; return span and method metadata."""
    candidates = []
    for pattern_number, pattern in enumerate(PATTERNS):
        for match in pattern.finditer(record["text"]):
            fields = match.groupdict()
            start, end = match.span()
            span = match.group()
            assert record["text"][start:end] == span
            kind = ("bounded", "unknown", "unbounded")[pattern_number]
            candidates.append({
                "subject": f"policy:travel-v{fields['version']}",
                "predicate": "applies_to", "object": "project:atlas",
                "source": record["source"], "valid_from": fields["start"],
                "valid_to": fields.get("end"), "end_kind": kind,
                "supported_through": fields["start"] if kind == "unknown" else None,
                "polarity": fields.get("verb") != "does not apply",
                "evidence": {"locator": record["locator"], "start": start, "end": end,
                             "text": span, "method": METHOD},
            })
    if not candidates:
        return [], {"source": record["source"], "reason": "no supported date and sentence pattern", "method": METHOD}
    return candidates, None


def resolve(name, directory_id, directory):
    """Use a shared identifier as evidence; abstain on an ambiguous name."""
    candidates = [row for row in directory if row["name"] == name]
    if directory_id is None:
        return {"decision": "abstain", "candidate": None, "candidates": [row["id"] for row in candidates],
                "reason": "the meeting gives no distinguishing identifier"}
    matches = [row for row in candidates if row["directory_id"] == directory_id]
    if len(matches) == 1:
        return {"decision": "accept", "candidate": matches[0]["id"], "reason": "same issuing directory identifier in the source record"}
    return {"decision": "reject", "candidate": None, "reason": "incompatible directory identifier"}


def construct():
    records = json.loads(SOURCE_RECORDS.read_text(encoding="utf-8"))
    extracted = []
    refusals = []
    for record in records["records"]:
        if not record.get("extract_claims", True):
            continue
        candidates, refusal = extract(record)
        extracted.extend(candidates)
        if refusal:
            refusals.append(refusal)
    register = records["records"][0]["text"]
    identity = re.search(r"Owner (Morgan Lee) has directory ID (NB-\d+)\.", register)
    assert identity and register[identity.start():identity.end()] == identity.group()
    minutes = records["records"][1]["text"]
    attendee = re.search(r"(Alex Kim) attended\.", minutes)
    assert attendee and minutes[attendee.start():attendee.end()] == attendee.group()
    accepted = resolve(identity.group(1), identity.group(2), records["directory"])
    rejected = resolve(identity.group(1), "NB-999", records["directory"])
    abstained = resolve(attendee.group(1), None, records["directory"])
    assert accepted["decision"] == "accept" and accepted["candidate"] == "person:morgan-lee"
    assert rejected["decision"] == "reject" and rejected["reason"]
    assert abstained["decision"] == "abstain" and set(abstained["candidates"]) == {"person:alex-kim-1", "person:alex-kim-2"}
    assert len(refusals) == 1 and refusals[0]["source"] == "synthetic-refusal"
    return extracted, refusals, {"m-morgan": accepted, "m-alex": abstained}, rejected


def canonical_claims(candidates, fixture_claims):
    """Match three extracted claims to ledger IDs and compare every canonical field."""
    selection = {("s-register", "policy:travel-v1"): ("c1", "m-policy-v1"),
                 ("s-minutes", "policy:travel-v2"): ("c4", "m-policy-v2-meeting"),
                 ("s-minutes", "policy:travel-v1"): ("c5", "m-policy-v1-meeting")}
    expected = {claim["id"]: claim for claim in fixture_claims}
    built = {}
    for candidate in candidates:
        key = (candidate["source"], candidate["subject"])
        if key not in selection:
            continue
        claim_id, mention = selection[key]
        if claim_id in built:
            raise ValueError(f"duplicate extracted claim {claim_id}")
        claim = {key: value for key, value in candidate.items() if key != "evidence"}
        claim.update(id=claim_id, mention=mention)
        if claim != expected[claim_id]:
            raise ValueError(f"constructed claim {claim_id} differs from fixture")
        built[claim_id] = {**claim, "evidence": candidate["evidence"]}
    if set(built) != {"c1", "c4", "c5"}:
        raise ValueError("missing constructed claims")
    return built
