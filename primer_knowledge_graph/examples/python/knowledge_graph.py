#!/usr/bin/env python3
"""Construct and query a synthetic, source-backed graph in file-backed DuckDB.

End kinds distinguish bounded, explicitly unbounded and unknown temporal scope.
Sources describe evidence, not truth. Negative and positive claims can coexist.
Queries use valid time, not the date when evidence became available.
SOURCE_RECORDS_PATH selects source-records JSON for the main graph. It supports
a valid end-date edit in the existing version-1 register sentence, retaining
all other records, ordering and identity data; it is not a general importer.
Fixture-dependent expected answers are skipped when constructed claims drift.
The separate repair and correction trace always uses the checked-in sources.
Use a fresh EXAMPLE_OUT directory for each run.
"""

from copy import deepcopy
from datetime import date
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from construction import SOURCE_RECORDS, build_claims, compare_with_fixture, construct

FIXTURE = Path(__file__).resolve().parents[1] / "fixture.json"
CLASSIFICATION = """CASE WHEN day < valid_from THEN 'outside'
    WHEN end_kind = 'bounded' THEN CASE WHEN day < valid_to THEN 'applicable' ELSE 'outside' END
    WHEN end_kind = 'unbounded' THEN 'applicable'
    WHEN end_kind = 'unknown' THEN CASE WHEN day <= supported_through THEN 'applicable' ELSE 'indeterminate' END
    ELSE 'invalid' END"""


def iso_date(value):
    if not isinstance(value, str):
        raise ValueError("expected ISO date string")
    try:
        parsed = date.fromisoformat(value)
    except ValueError as error:
        raise ValueError("expected ISO date string") from error
    if parsed.isoformat() != value:
        raise ValueError("expected ISO date string")
    return parsed


def validate(data):
    """Reject broken references, malformed intervals and inconsistent mentions."""
    indexes = {}
    for table in ("sources", "entities", "mentions", "claims", "resolution_decisions"):
        rows = data[table]
        ids = [row["id"] for row in rows]
        if len(ids) != len(set(ids)):
            raise ValueError(f"duplicate {table} id")
        indexes[table] = {row["id"]: row for row in rows}
    for source in data["sources"]:
        iso_date(source["published"])
    for mention in data["mentions"]:
        if (mention["source"] not in indexes["sources"] or
                (mention["entity"] is not None and mention["entity"] not in indexes["entities"])):
            raise ValueError("mention has an unknown source or entity")
    for decision in data["resolution_decisions"]:
        if decision["mention"] not in indexes["mentions"]:
            raise ValueError("resolution decision has an unknown mention")
        if decision["decision"] not in {"accept", "reject", "abstain"}:
            raise ValueError("invalid resolution decision")
        candidates = decision["candidates"]
        if not candidates or any(candidate not in indexes["entities"] for candidate in candidates):
            raise ValueError("resolution decision has an unknown candidate")
        if decision["decision"] == "abstain" and decision["candidate"] is not None:
            raise ValueError("abstention cannot select a candidate")
        if decision["decision"] == "accept" and decision["candidate"] not in candidates:
            raise ValueError("accepted candidate is not in candidate set")
    for claim in data["claims"]:
        if claim["subject"] not in indexes["entities"] or claim["object"] not in indexes["entities"]:
            raise ValueError("claim has an unknown entity")
        if claim["source"] not in indexes["sources"]:
            raise ValueError("claim has an unknown source")
        if type(claim["polarity"]) is not bool or not claim["predicate"]:
            raise ValueError("invalid claim polarity or predicate")
        if not {"valid_from", "valid_to", "end_kind", "supported_through"} <= claim.keys():
            raise ValueError("missing temporal field")
        start = iso_date(claim["valid_from"])
        end = iso_date(claim["valid_to"]) if claim["valid_to"] is not None else None
        horizon = iso_date(claim["supported_through"]) if claim["supported_through"] is not None else None
        kind = claim["end_kind"]
        if kind == "bounded":
            valid = end is not None and end > start and horizon is None
        elif kind == "unbounded":
            valid = end is None and horizon is None
        elif kind == "unknown":
            valid = end is None and horizon is not None and horizon >= start
        else:
            valid = False
        if not valid:
            raise ValueError("invalid temporal interval fields")
        if claim["mention"] is not None:
            mention = indexes["mentions"].get(claim["mention"])
            if (mention is None or mention["source"] != claim["source"] or
                    mention["entity"] not in {claim["subject"], claim["object"]}):
                raise ValueError("claim mention must identify a participant in its source")
    # Analytical projection is the set of positive claims, not resolved truth.
    projection = {(c["subject"], c["object"], c["predicate"]) for c in data["claims"] if c["polarity"]}
    relations = data["relations"]
    keys = [(r["source"], r["target"], r["type"]) for r in relations]
    if len(keys) != len(set(keys)) or set(keys) != projection or any(r["weight"] <= 0 for r in relations):
        raise ValueError("relations must be a unique positive-claim projection with positive weights")


def expect_invalid(data, change, message):
    broken = deepcopy(data)
    change(broken)
    try:
        validate(broken)
    except ValueError as error:
        assert message in str(error), str(error)
    else:
        raise AssertionError(f"validation accepted {message}")


def main():
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    validate(data)
    source_records_path = Path(os.environ.get("SOURCE_RECORDS_PATH", SOURCE_RECORDS))
    print("Main graph source records:", source_records_path)
    records = json.loads(source_records_path.read_text(encoding="utf-8"))
    source_texts = {record["source"]: record for record in records["records"]}
    for source in data["sources"]:
        assert source_texts[source["id"]]["locator"] == source["locator"]
    for mention in data["mentions"]:
        assert mention["text"] in source_texts[mention["source"]]["text"]
    candidates, refusals, decisions, test_rejection = construct(source_records_path)
    for row in data["resolution_decisions"]:
        generated = decisions[row["mention"]]
        assert all(row[key] == generated[key] for key in ("decision", "candidate", "reason"))
        generated_candidates = generated.get("candidates", [generated.get("candidate")])
        assert set(row["candidates"]) == set(generated_candidates)
        assert next(m for m in data["mentions"] if m["id"] == row["mention"])["entity"] == row["candidate"]
    constructed = build_claims(candidates)
    fixture_differences = compare_with_fixture(constructed, data["claims"])
    # These rows are constructed from retained text; the other ledger rows are curated.
    data["claims"] = [constructed.get(claim["id"], claim) for claim in data["claims"]]
    curated_ids = sorted(c["id"] for c in data["claims"] if c["id"] not in constructed)
    validate(data)
    expect_invalid(data, lambda d: d["claims"][0].update(object="missing"), "unknown entity")
    expect_invalid(data, lambda d: d["claims"][0].update(valid_to="1843-01-01"), "interval")
    for change in (
        {"valid_to": None}, {"supported_through": "2024-01-01"},
        {"end_kind": "unbounded"}, {"end_kind": "unknown"},
        {"end_kind": "unbounded", "valid_to": None, "supported_through": "2024-01-01"},
        {"end_kind": "unknown", "valid_to": None},
        {"end_kind": "unknown", "valid_to": None, "supported_through": "2023-12-31"},
        {"end_kind": "unknown", "supported_through": "2024-01-01"},
        {"end_kind": "invalid"}, {"end_kind": None},
    ):
        expect_invalid(data, lambda d, fields=change: d["claims"][0].update(fields), "interval")
    for field in ("valid_from", "valid_to", "end_kind", "supported_through"):
        expect_invalid(data, lambda d, key=field: d["claims"][0].pop(key), "missing temporal")
    for field in ("valid_from", "valid_to", "supported_through"):
        expect_invalid(data, lambda d, key=field: d["claims"][0].update({key: "20240101"}), "ISO date")
    expect_invalid(data, lambda d: d["claims"][0].update(mention="m-policy-v2-meeting"), "claim mention")
    expect_invalid(data, lambda d: d["entities"].append(d["entities"][0]), "duplicate")
    expect_invalid(data, lambda d: d["resolution_decisions"][1].update(candidate="person:alex-kim-1"), "abstention")
    resolution = {decision["mention"]: decision for decision in data["resolution_decisions"]}
    assert resolution["m-alex"]["decision"] == "abstain"
    assert resolution["m-alex"]["candidate"] is None

    import duckdb  # Runtime dependency; deliberately no alternate database.

    output_dir = Path(os.environ.get("EXAMPLE_OUT", Path.cwd()))
    output_dir.mkdir(parents=True, exist_ok=True)
    db_path = output_dir / "knowledge_graph.duckdb"
    def populate_database(path, graph, extracted_claims):
        db = duckdb.connect(str(path))
        db.execute("""CREATE TABLE claims (id VARCHAR, subject VARCHAR, predicate VARCHAR,
            object VARCHAR, source VARCHAR, mention VARCHAR, valid_from DATE,
            valid_to DATE, end_kind VARCHAR, supported_through DATE, polarity BOOLEAN)""")
        db.execute("CREATE TABLE extraction_evidence (claim_id VARCHAR, locator VARCHAR, span_start INTEGER, span_end INTEGER, span_text VARCHAR, method VARCHAR)")
        db.executemany("INSERT INTO extraction_evidence VALUES (?, ?, ?, ?, ?, ?)",
            [(claim_id, e["locator"], e["start"], e["end"], e["text"], e["method"])
             for claim_id, claim in extracted_claims.items() for e in [claim["evidence"]]])
        db.execute("CREATE TABLE sources (id VARCHAR, title VARCHAR, published DATE, locator VARCHAR)")
        db.execute("CREATE TABLE mentions (id VARCHAR, source VARCHAR, text VARCHAR, entity VARCHAR)")
        db.executemany("INSERT INTO claims VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [tuple(c[k] for k in ("id", "subject", "predicate", "object", "source", "mention", "valid_from", "valid_to", "end_kind", "supported_through", "polarity")) for c in graph["claims"]])
        db.executemany("INSERT INTO sources VALUES (?, ?, ?, ?)", [(s["id"], s["title"], s["published"], s["locator"]) for s in graph["sources"]])
        db.executemany("INSERT INTO mentions VALUES (?, ?, ?, ?)", [(m["id"], m["source"], m["text"], m["entity"]) for m in graph["mentions"]])
        db.close()

    populate_database(db_path, data, constructed)
    # Reopen the file before querying so the example verifies durable storage,
    # not only an in-memory relational projection.
    db = duckdb.connect(str(db_path), read_only=True)
    persisted = db.execute("SELECT id, valid_from, valid_to, end_kind, supported_through FROM claims ORDER BY id").fetchall()
    assert persisted == [(c["id"], iso_date(c["valid_from"]),
                          iso_date(c["valid_to"]) if c["valid_to"] is not None else None,
                          c["end_kind"], iso_date(c["supported_through"]) if c["supported_through"] is not None else None)
                         for c in data["claims"]]

    # Every query is bounded by specific entity/predicate inputs or a fixed hop count.
    direct = db.execute("""SELECT id, object, polarity FROM claims
        WHERE subject = ? AND predicate = ? ORDER BY id""", ["policy:travel-v1", "applies_to"]).fetchall()
    assert direct == [("c1", "project:atlas", True), ("c5", "project:atlas", False)]
    two_hop = db.execute("""SELECT a.id, b.id, b.object FROM claims a JOIN claims b ON a.object = b.subject
        WHERE a.subject = ? AND a.predicate = ? AND b.predicate = ? AND a.polarity AND b.polarity
        ORDER BY a.id, b.id""", ["policy:travel-v1", "applies_to", "belongs_to"]).fetchall()
    assert two_hop == [("c1", "c3", "org:northbridge")]

    def evidence_on(day, subject="policy:travel-v1", predicate="applies_to", obj="project:atlas", source=None, connection=None):
        connection = db if connection is None else connection
        rows = connection.execute(f"""WITH requested AS (SELECT CAST(? AS DATE) AS day)
            SELECT c.id, c.polarity, {CLASSIFICATION} AS temporal_status,
              c.valid_from, c.valid_to, c.end_kind, c.supported_through, c.source, s.locator, c.mention
            FROM claims c JOIN sources s ON c.source = s.id CROSS JOIN requested
            WHERE c.subject = ? AND c.predicate = ? AND c.object = ? AND (? IS NULL OR c.source = ?)
            ORDER BY c.id""", [day, subject, predicate, obj, source, source]).fetchall()
        if any(row[2] == "invalid" for row in rows):
            raise ValueError("invalid temporal classification")
        return rows
    provenance = db.execute("""SELECT c.id, s.title, s.locator, m.text, e.span_start, e.span_end, e.span_text, e.method FROM claims c
        JOIN sources s ON c.source = s.id LEFT JOIN mentions m ON c.mention = m.id
        LEFT JOIN extraction_evidence e ON c.id = e.claim_id
        WHERE c.subject = ? AND c.predicate = ? AND c.object = ? ORDER BY c.id""",
        ["policy:travel-v1", "applies_to", "project:atlas"]).fetchall()
    assert [row[0] for row in provenance] == ["c1", "c5"]
    for claim_id, _, locator, _, start, end, span, method in provenance:
        claim = constructed[claim_id]
        assert claim["evidence"] == {"locator": locator, "start": start, "end": end,
                                     "text": span, "method": method}
        assert source_texts[claim["source"]]["text"][start:end] == span


    def answer_rows(rows):
        polarities = {row[1] for row in rows if row[2] == "applicable"}
        if len(polarities) > 1:
            return "abstain: conflicting evidence"
        if any(row[2] == "indeterminate" for row in rows):
            return "abstain: indeterminate temporal scope"
        if not polarities:
            return "abstain: no evidence"
        return "supported" if True in polarities else "refuted"

    def answer(day):
        return answer_rows(evidence_on(day))

    assert answer_rows([("x", False, "applicable")]) == "refuted"
    assert answer_rows([("x", True, "applicable"), ("y", True, "indeterminate")]) == "abstain: indeterminate temporal scope"
    assert answer_rows([("x", True, "applicable"), ("y", False, "applicable"),
                        ("z", True, "indeterminate")]) == "abstain: conflicting evidence"

    if not fixture_differences:
        cases = {
            "2023-12-31": (("outside", "outside"), "abstain: no evidence"),
            "2024-03-01": (("applicable", "outside"), "supported"),
            "2024-03-15": (("applicable", "applicable"), "abstain: conflicting evidence"),
            "2024-03-16": (("applicable", "indeterminate"), "abstain: indeterminate temporal scope"),
            "2024-04-01": (("outside", "indeterminate"), "abstain: indeterminate temporal scope"),
            "2024-04-15": (("outside", "indeterminate"), "abstain: indeterminate temporal scope"),
            "2099-01-01": (("outside", "indeterminate"), "abstain: indeterminate temporal scope"),
        }
        for day, (statuses, result) in cases.items():
            rows = evidence_on(day)
            assert [row[0] for row in rows] == ["c1", "c5"]
            assert tuple(row[2] for row in rows) == statuses and answer(day) == result
        assert evidence_on("2024-01-01")[0][2] == "applicable"
        assert evidence_on("2024-03-15", source="s-minutes")[0][2] == "applicable"
        assert evidence_on("2024-03-16", source="s-minutes")[0][2] == "indeterminate"
    else:
        print("Current-fixture temporal assertions skipped; query the rebuilt source-derived graph explicitly.")

    def path_status(day):
        first = evidence_on(day, source="s-register")[0][2]
        second = evidence_on(day, "project:atlas", "belongs_to", "org:northbridge")[0][2]
        return "outside" if "outside" in (first, second) else "indeterminate" if "indeterminate" in (first, second) else "applicable"

    if not fixture_differences:
        assert path_status("2024-01-01") == "applicable"
        assert path_status("2024-03-01") == "indeterminate"
        assert path_status("2024-04-01") == "outside"
    unbounded = [c for c in candidates if c["source"] == "synthetic-continuation"]
    assert len(unbounded) == 1 and unbounded[0]["end_kind"] == "unbounded"
    # Evaluate a deliberately defective positive-only extraction against the
    # same held-in source and question, then rerun from the original inputs.
    demo_records = json.loads(SOURCE_RECORDS.read_text(encoding="utf-8"))
    demo_candidates, _, _, _ = construct(SOURCE_RECORDS)
    demo_claims = build_claims(demo_candidates)
    minutes = next(r for r in demo_records["records"] if r["source"] == "s-minutes")
    negative = demo_claims["c5"]
    span = negative["evidence"]
    assert minutes["text"][span["start"]:span["end"]] == span["text"]
    assert negative["polarity"] is False
    incomplete_claims = {key: claim for key, claim in demo_claims.items() if claim["polarity"]}
    assert set(demo_claims) - set(incomplete_claims) == {"c5"}
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def graph_for(claims, missing=()):
        graph = deepcopy(fixture)
        graph["claims"] = [claims.get(c["id"], c) for c in graph["claims"] if c["id"] not in missing]
        validate(graph)
        return graph

    question_day = "2024-03-15"
    with TemporaryDirectory(prefix="knowledge-graph-repair-") as temporary_dir:
        def query_release(name, graph, claims):
            path = Path(temporary_dir) / (name + ".duckdb")
            populate_database(path, graph, claims)
            connection = duckdb.connect(str(path), read_only=True)
            try:
                rows = evidence_on(question_day, connection=connection)
                return [(row[0], row[1], row[2]) for row in rows], answer_rows(rows)
            finally:
                connection.close()

        failed_rows, failed_answer = query_release(
            "incomplete", graph_for(incomplete_claims, missing={"c5"}), incomplete_claims)
        # Repair the extraction policy by retaining negative candidates, then
        # construct again and build a fresh database, never patching the old one.
        repaired_candidates, _, _, _ = construct(SOURCE_RECORDS)
        repaired_claims = build_claims(repaired_candidates)
        repaired_rows, repaired_answer = query_release(
            "repaired", graph_for(repaired_claims), repaired_claims)
        assert (failed_rows, failed_answer) == ([("c1", True, "applicable")], "supported")
        assert (repaired_rows, repaired_answer) == (
            [("c1", True, "applicable"), ("c5", False, "applicable")],
            "abstain: conflicting evidence")
        print(f"Repair trace question: does travel v1 apply to Atlas on {question_day}?")
        print("Failure: positive-only extraction; evidence and answer:", failed_rows, failed_answer)
        print("Diagnosis: retrieved minutes contain a missing negative assertion:", span["locator"], repr(span["text"]))
        print("Repair: retain negative candidates; fresh rebuild and rerun:", repaired_rows, repaired_answer)

        # A separate hypothetical source correction changes only c1's end date.
        changed_records = deepcopy(demo_records)
        register = next(r for r in changed_records["records"] if r["source"] == "s-register")
        old_sentence = "Travel Policy v1 applies to Atlas from 2024-01-01 until 2024-04-01."
        new_sentence = "Travel Policy v1 applies to Atlas from 2024-01-01 until 2024-03-01."
        assert register["text"].count(old_sentence) == 1
        register["text"] = register["text"].replace(old_sentence, new_sentence, 1)
        assert "Travel Policy v2 applies to Atlas on 2024-04-01." in register["text"]
        corrected_input = Path(temporary_dir) / "corrected-source.json"
        corrected_input.write_text(json.dumps(changed_records), encoding="utf-8")
        changed_candidates, _, _, _ = construct(corrected_input)
        changed_claims = build_claims(changed_candidates)
        assert changed_claims["c1"]["valid_to"] == "2024-03-01"
        assert all(changed_claims[key] == repaired_claims[key] for key in ("c4", "c5"))
        corrected_rows, corrected_answer = query_release(
            "corrected", graph_for(changed_claims), changed_claims)
        assert (corrected_rows, corrected_answer) == (
            [("c1", True, "outside"), ("c5", False, "applicable")], "refuted")
        print("Separate hypothetical source correction: c1 end 2024-04-01 -> 2024-03-01")
        print("Fresh correction rebuild and same question:", corrected_rows, corrected_answer)
    synthetic = deepcopy(data)
    synthetic["claims"][0].update({k: unbounded[0][k] for k in ("valid_from", "valid_to", "end_kind", "supported_through")})
    validate(synthetic)
    # The same SQL classifier is exercised against a separate explicit assertion.
    check = db.execute(f"""WITH assertion AS (SELECT CAST(? AS DATE) AS day, CAST(? AS DATE) AS valid_from,
        CAST(? AS DATE) AS valid_to, ? AS end_kind, CAST(? AS DATE) AS supported_through)
        SELECT {CLASSIFICATION} FROM assertion""", ["2099-01-01", unbounded[0]["valid_from"],
        unbounded[0]["valid_to"], unbounded[0]["end_kind"], unbounded[0]["supported_through"]]).fetchone()[0]
    assert check == "applicable"
    print("Constructed claims:", sorted(constructed), "curated claims:", curated_ids)
    print("Fixture comparison (diagnostic):", "matched" if not fixture_differences else fixture_differences)
    print("Extraction refusals:", refusals)
    print("Fixture resolution decisions (generated and checked):", decisions)
    print("Test-only rejection (not a fixture decision):", test_rejection)
    print("Undated direct topology:", direct)
    print("Undated two-hop topology:", two_hop)
    print("Provenance:", provenance)
    print("2024-03-15 answer:", answer("2024-03-15"))
    print("2024-04-15 answer:", answer("2024-04-15"))
    print("Validation and query assertions passed.")
    db.close()


if __name__ == "__main__":
    main()
