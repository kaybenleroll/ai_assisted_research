"""Check the displayed joint law of two fair, dependent bits."""

from math import isclose, isfinite, log2


joint = [[0.4, 0.1], [0.1, 0.4]]
assert all(isfinite(p) and p >= 0 for row in joint for p in row)
rows = [sum(row) for row in joint]
columns = [sum(column) for column in zip(*joint)]
# Absolute tolerance covers floating-point round-off for this small table.
tol = 1e-12
assert isclose(sum(rows), 1.0, rel_tol=0, abs_tol=tol)
assert all(isclose(p, 0.5, rel_tol=0, abs_tol=tol) for p in rows + columns)

# All four probabilities and marginals are positive, so no zero-log case arises.
information = sum(
    joint[x][y] * log2(joint[x][y] / (rows[x] * columns[y]))
    for x in range(2)
    for y in range(2)
)
# Independently, this is 1 - binary entropy of crossover probability 0.2.
expected = 1 + 0.2 * log2(0.2) + 0.8 * log2(0.8)
assert isclose(information, expected, rel_tol=0, abs_tol=tol)
assert isclose(information, 0.2780719051126377, rel_tol=0, abs_tol=tol)
print(f"marginals: {rows}, {columns}; mutual information: {information:.12f} bits")
