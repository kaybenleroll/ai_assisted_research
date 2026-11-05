"""Check the path on vertices 1--3 and the isolated vertex 4."""

import numpy as np


adjacency = np.array([[0, 1, 0, 0], [1, 0, 1, 0],
                      [0, 1, 0, 0], [0, 0, 0, 0]], dtype=float)
incidence = np.array([[1, 0], [-1, 1], [0, -1], [0, 0]], dtype=float)
laplacian = np.diag(adjacency.sum(axis=1)) - adjacency
signal = np.array([0, 1, 2, 7], dtype=float)
component_constant = np.array([5, 5, 5, -20], dtype=float)

np.testing.assert_allclose(adjacency, adjacency.T)
np.testing.assert_allclose(laplacian, laplacian.T)
np.testing.assert_allclose(laplacian @ np.ones(4), 0, atol=1e-12)
np.testing.assert_allclose(laplacian, incidence @ incidence.T)
np.testing.assert_allclose(np.trace(laplacian), adjacency.sum())
np.testing.assert_allclose(signal @ laplacian @ signal, 2)
np.testing.assert_allclose(component_constant @ laplacian @ component_constant, 0)
np.testing.assert_allclose(np.linalg.eigvalsh(laplacian), [0, 0, 1, 3], atol=1e-12)
print("Four-vertex spectrum: 0, 0, 1, 3; signal energy: 2")
