import csv
from pathlib import Path

EXPECTED = {"east": "4", "north": "7", "west": "3"}
# The check reads the delivered artefact.
inventory = Path("published") / "inventory.csv"
with inventory.open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))
actual = {row["sensor"]: row["count"] for row in rows}
if len(rows) != len(EXPECTED) or actual != EXPECTED:
    raise SystemExit("FAIL: inventory differs from approved readings")
print("PASS: inventory matches approved readings")
