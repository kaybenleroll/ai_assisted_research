from pathlib import Path
import os

output = Path(os.environ["EXAMPLE_OUT"])
assert output == Path("/out")
assert 2 + 2 == 4
(output / "python.txt").write_text("checked\n", encoding="utf-8")
