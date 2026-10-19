"""Solve a small, well-conditioned system with the shared NumPy runtime."""

import numpy as np


matrix = np.array([[3.0, 1.0], [1.0, 2.0]])
expected = np.array([2.0, -1.0])
rhs = matrix @ expected
solution = np.linalg.solve(matrix, rhs)

# The system is well-conditioned; 1e-12 allows accumulated double-precision
# rounding while remaining far below the scale of an incorrect solution.
assert np.allclose(solution, expected, rtol=1e-12, atol=1e-12)
assert np.linalg.norm(matrix @ solution - rhs, ord=np.inf) < 1e-12
