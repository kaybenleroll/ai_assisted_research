from pathlib import Path

readings = "sensor,count\neast,4\nnorth,7\nwest,3\n"
for directory in (Path("staging"), Path("published")):
    directory.mkdir(exist_ok=True)
Path("staging/inventory.csv").write_text(readings, encoding="utf-8")
Path("published/inventory.csv").write_text(readings, encoding="utf-8")
print("Build complete")
