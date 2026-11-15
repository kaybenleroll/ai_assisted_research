# Runner Fixture

This block is explicitly listed in the manifest.

```python {#runnable-python}
from pathlib import Path
import os

assert Path(os.environ["EXAMPLE_OUT"]) == Path("/out")
assert sum((1, 2, 3)) == 6
```

This block is illustrative and must never be executed.

```python {#illustrative-only}
raise RuntimeError("unlisted illustrative fence was executed")
```
