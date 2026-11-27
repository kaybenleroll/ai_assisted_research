"""Reproduce the six-vertex weak-bridge ledger and verify its invariants."""

import numpy as np


for epsilon in (0.0, 0.01, 0.1, 1.0):
    adjacency = np.zeros((6, 6))
    for u, v, weight in (
        (0, 1, 1.0), (0, 2, 1.0), (1, 2, 1.0),
        (3, 4, 1.0), (3, 5, 1.0), (4, 5, 1.0), (0, 3, epsilon),
    ):
        adjacency[u, v] = adjacency[v, u] = weight
    degrees = adjacency.sum(axis=1)
    laplacian = np.diag(degrees) - adjacency
    normalised = np.eye(6) - adjacency / np.sqrt(np.outer(degrees, degrees))
    values, vectors = np.linalg.eigh(laplacian)
    normalised_values = np.linalg.eigvalsh(normalised)
    expected = 4 * epsilon / (3 + 2 * epsilon + np.sqrt(9 + 4 * epsilon + 4 * epsilon**2))
    normalised_root = 4 * epsilon / (
        6 + 5 * epsilon + np.sqrt((6 + 5 * epsilon)**2 - 16 * epsilon * (2 + epsilon))
    )
    assert np.isclose(values[1], expected, atol=1e-12, rtol=1e-12)
    assert np.isclose(normalised_values[1], normalised_root, atol=1e-12, rtol=1e-12)
    assert values[1] <= 2 * epsilon / 3 + 1e-12
    assert normalised_values[1] <= 2 * epsilon / (6 + epsilon) + 1e-12
    zeros = int(np.count_nonzero(np.abs(values) < 1e-12))
    assert zeros == (2 if epsilon == 0 else 1)
    if epsilon == 0:
        print(f"{epsilon:g}: components=2, lambda2=0, nu2=0; mode not unique")
        continue
    vector = vectors[:, 1]
    if vector[:3].mean() < 0:
        vector = -vector
    mean = vector[:3].mean()
    deviation = np.max(np.abs(vector[:3] - mean)) / abs(mean)
    residual = np.linalg.norm(laplacian @ vector - values[1] * vector)
    assert residual < 1e-12
    assert np.allclose(vector[:3], -vector[3:], atol=1e-12)
    print(f"{epsilon:g}: components=1, lambda2={values[1]:.6f}, "
          f"nu2={normalised_values[1]:.6f}, mean={mean:.6f}, "
          f"relative deviation={deviation:.6f}, residual={residual:.2e}")
