"""Ground vertex 3 of a unit path and solve for effective resistance."""

import numpy as np
from scipy.linalg import solve


laplacian = np.array([[1, -1, 0], [-1, 2, -1], [0, -1, 1]], dtype=float)
injection = np.array([1, 0, -1], dtype=float)
# Vertex 3 is the grounded sink; the remaining principal minor is nonsingular.
potential = np.append(solve(laplacian[:2, :2], injection[:2], assume_a="pos"), 0)
resistance = potential[0] - potential[2]

np.testing.assert_allclose(laplacian @ potential, injection, atol=1e-12)
np.testing.assert_allclose(resistance, 2, atol=1e-12)
np.testing.assert_allclose(potential @ laplacian @ potential, resistance, atol=1e-12)
print(f"Path resistance between vertices 1 and 3: {resistance:.1f}")
