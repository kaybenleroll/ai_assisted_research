# Answer Key

Run each fixture from its own directory. Both `python3 build.py` commands print `Build complete`; both `python3 verify.py` commands print `PASS: inventory matches approved readings` and exit zero.

In `case-17`, the published inventory is `sensor,count | east,4 | north,7`: the build drops `west,3` but the verification reads the complete staging inventory. The passing result therefore cannot establish the claimed published state. Pointing the verifier at `published/inventory.csv` makes it exit nonzero with `FAIL: inventory differs from approved readings`; correcting the publishing rule and then verifying the published output makes the intended check pass. Both changes are needed for a correct delivery and an informative gate.

In `case-29`, the published inventory is `sensor,count | east,4 | north,7 | west,3`; verification reads that delivered file, checks exact row count and the complete expected mapping, and passes. The control is not a claim about atomic publication, concurrent modification, or operating-system durability; those are outside this fixture's promise.

`case-29-original` preserves the initial intended control. Its `csv.DictReader`
accepts duplicate column names and silently retains the final value: a file with
header `sensor,count,count` and rows `east,999,4`, `north,888,7`, `west,777,3`
incorrectly passed. An independent reviewer identified this real defect; it was
not a false positive. The corrected `case-29` validates the exact header and
rejects extra fields before comparing all readings. Both original and corrected
controls remain available so the initial trial and correction can be reproduced.
