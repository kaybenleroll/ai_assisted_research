"""Check the pinned interpreter and DuckDB with an offline graph query."""

import sys

import duckdb


def main():
    if sys.version_info[:3] != (3, 12, 15):
        raise RuntimeError(f"expected Python 3.12.15, got {sys.version.split()[0]}")
    if duckdb.__version__ != "1.4.3":
        raise RuntimeError(f"expected DuckDB 1.4.3, got {duckdb.__version__}")

    with duckdb.connect(":memory:") as db:
        result = db.execute(
            """
            WITH edges(source, target) AS (VALUES ('a', 'b'), ('b', 'c'))
            SELECT e1.source, e2.target
            FROM edges AS e1 JOIN edges AS e2 ON e1.target = e2.source
            ORDER BY e1.source, e2.target
            """
        ).fetchall()
    if result != [("a", "c")]:
        raise RuntimeError(f"unexpected graph query result: {result!r}")
    print(f"knowledge-graph-probe: Python={sys.version.split()[0]} DuckDB={duckdb.__version__}")


if __name__ == "__main__":
    main()
