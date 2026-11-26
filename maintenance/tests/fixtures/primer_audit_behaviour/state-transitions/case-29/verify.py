import csv
from pathlib import Path

EXPECTED = {"east": "4", "north": "7", "west": "3"}
# The check reads the delivered artefact.
inventory = Path("published") / "inventory.csv"
with inventory.open(newline="", encoding="utf-8") as handle:
    reader = csv.DictReader(handle)
    if reader.fieldnames != ["sensor", "count"]:
        raise SystemExit("FAIL: inventory has the wrong header")
    rows = list(reader)
if any(set(row) != {"sensor", "count"} for row in rows):
    raise SystemExit("FAIL: inventory has extra fields")
actual = {row["sensor"]: row["count"] for row in rows}
if len(rows) != len(EXPECTED) or actual != EXPECTED:
    raise SystemExit("FAIL: inventory differs from approved readings")
print("PASS: inventory matches approved readings")
