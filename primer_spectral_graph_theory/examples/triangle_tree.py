"""Check the matrix-tree and edge-resistance identities on a unit triangle."""

import numpy as np
from scipy.linalg import solve


laplacian = np.array([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]], dtype=float)
# Ground vertex 3; the determinant is the number of unit-weight spanning trees.
grounded = laplacian[:2, :2]
tree_count = np.linalg.det(grounded)
potential = np.append(solve(grounded, [1, 0], assume_a="pos"), 0)
resistance = potential[0] - potential[2]

np.testing.assert_allclose(tree_count, 3, atol=1e-12)
np.testing.assert_allclose(laplacian @ potential, [1, 0, -1], atol=1e-12)
np.testing.assert_allclose(resistance, 2 / 3, atol=1e-12)
# Two of the three spanning trees contain edge {1, 3}; its conductance is 1.
np.testing.assert_allclose(resistance, 2 / tree_count, atol=1e-12)
print(f"Triangle spanning trees: {tree_count:.0f}; edge resistance: {resistance:.6f}")
