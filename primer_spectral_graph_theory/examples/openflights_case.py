"""Run a deterministic spectral analysis of a synthetic route-table fixture.

The fixture has the historical shape of an OpenFlights route table, but all
values are synthetic. This script never downloads data and treats route rows as
observations whose undirected interpretation is chosen explicitly below.
"""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np


DATA_PATH = Path(__file__).with_name("data") / "openflights_synthetic_routes.dat"
PROVENANCE_PATH = DATA_PATH.with_suffix(".provenance.txt")
REQUIRED_COLUMNS = {
    "source_airport",
    "destination_airport",
    "source_airport_id",
    "destination_airport_id",
}


def load_routes() -> tuple[list[dict[str, str]], list[str]]:
    """Load and validate the local fixture without changing its row order."""

    provenance = PROVENANCE_PATH.read_text(encoding="utf-8")
    required_phrases = ("synthetic", "historical OpenFlights", "not real current aviation data")
    assert all(phrase in provenance for phrase in required_phrases), (
        "the provenance note must identify the fixture as synthetic historical-shape data"
    )

    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        assert reader.fieldnames is not None
        assert REQUIRED_COLUMNS <= set(reader.fieldnames)
        routes = list(reader)

    assert routes, "the fixture must contain at least one route"
    nodes = sorted(
        {
            endpoint
            for route in routes
            for endpoint in (
                route["source_airport"],
                route["destination_airport"],
            )
        }
    )
    assert all(route["source_airport"] != route["destination_airport"] for route in routes)
    assert all(route["source_airport_id"] != route["destination_airport_id"] for route in routes)
    return routes, nodes


def graph_variants(routes: list[dict[str, str]], nodes: list[str]) -> dict[str, np.ndarray]:
    """Build binary and multiplicity-weighted undirected adjacency matrices."""

    index = {node: position for position, node in enumerate(nodes)}
    counts = np.zeros((len(nodes), len(nodes)), dtype=float)
    for route in routes:
        source = index[route["source_airport"]]
        destination = index[route["destination_airport"]]
        counts[source, destination] += 1
        counts[destination, source] += 1
    binary = (counts > 0).astype(float)
    return {"binary": binary, "count": counts}


def components(adjacency: np.ndarray) -> list[list[int]]:
    """Return connected components in deterministic vertex-index order."""

    unseen = set(range(adjacency.shape[0]))
    result = []
    while unseen:
        start = min(unseen)
        stack = [start]
        unseen.remove(start)
        component = []
        while stack:
            vertex = stack.pop()
            component.append(vertex)
            neighbours = np.flatnonzero(adjacency[vertex] > 0)
            for neighbour in reversed(neighbours.tolist()):
                if neighbour in unseen:
                    unseen.remove(neighbour)
                    stack.append(neighbour)
        result.append(sorted(component))
    return sorted(result, key=lambda component: (component[0], len(component)))


def spectral_diagnostics(adjacency: np.ndarray) -> dict[str, np.ndarray | float | int]:
    """Compute dense Laplacian diagnostics for this deliberately small graph."""

    degrees = adjacency.sum(axis=1)
    laplacian = np.diag(degrees) - adjacency
    eigenvalues, eigenvectors = np.linalg.eigh(laplacian)
    inverse_sqrt_degree = np.zeros_like(degrees)
    positive = degrees > 0
    inverse_sqrt_degree[positive] = 1 / np.sqrt(degrees[positive])
    normalised = np.eye(adjacency.shape[0]) - (
        inverse_sqrt_degree[:, None] * adjacency * inverse_sqrt_degree[None, :]
    )
    normalised_eigenvalues = np.linalg.eigvalsh(normalised)
    zero_tolerance = 1e-10
    component_count = len(components(adjacency))
    assert np.allclose(adjacency, adjacency.T)
    assert np.allclose(np.diag(adjacency), 0)
    assert np.allclose(laplacian, laplacian.T)
    assert np.allclose(laplacian @ np.ones(adjacency.shape[0]), 0, atol=zero_tolerance)
    assert np.all(eigenvalues >= -zero_tolerance)
    assert np.count_nonzero(np.abs(eigenvalues) < zero_tolerance) == component_count
    assert np.all(normalised_eigenvalues >= -zero_tolerance)
    assert np.all(normalised_eigenvalues <= 2 + zero_tolerance)
    assert np.count_nonzero(np.abs(normalised_eigenvalues) < zero_tolerance) == component_count
    assert np.allclose(
        laplacian @ eigenvectors[:, 1],
        eigenvalues[1] * eigenvectors[:, 1],
        atol=1e-10,
    )
    return {
        "degrees": degrees,
        "laplacian_eigenvalues": eigenvalues,
        "normalised_eigenvalues": normalised_eigenvalues,
        "fiedler": eigenvectors[:, 1],
        "component_count": component_count,
    }


def sweep_cut(adjacency: np.ndarray, vector: np.ndarray) -> tuple[list[int], float]:
    """Find the minimum conductance among Fiedler-vector prefix cuts."""

    order = np.argsort(vector, kind="stable")
    degrees = adjacency.sum(axis=1)
    total_volume = degrees.sum()
    candidates: list[tuple[float, tuple[int, ...]]] = []
    for size in range(1, adjacency.shape[0]):
        selected = np.zeros(adjacency.shape[0], dtype=bool)
        selected[order[:size]] = True
        boundary = adjacency[np.ix_(selected, ~selected)].sum()
        volume = degrees[selected].sum()
        complement_volume = total_volume - volume
        conductance = boundary / min(volume, complement_volume)
        candidates.append((float(conductance), tuple(np.flatnonzero(selected).tolist())))
    conductance, selected = min(candidates, key=lambda candidate: (candidate[0], candidate[1]))
    chosen = list(selected)
    assert 0 < len(chosen) < adjacency.shape[0]
    assert conductance > 0
    assert conductance <= 1 + 1e-12
    return chosen, conductance


def format_nodes(indices: list[int], nodes: list[str]) -> str:
    return ",".join(nodes[index] for index in indices)


def main() -> None:
    routes, nodes = load_routes()
    variants = graph_variants(routes, nodes)
    assert len(routes) == 27
    assert nodes == [f"A{number:02d}" for number in range(1, 11)]
    assert int(np.count_nonzero(variants["binary"]) / 2) == 17
    assert np.count_nonzero(variants["count"] - variants["binary"]) == 16
    assert np.isclose(variants["count"].sum(), 2 * len(routes))

    print("Synthetic/historical-shape OpenFlights case study (offline fixture)")
    print(f"Fixture: {DATA_PATH.name}; rows={len(routes)}; vertices={len(nodes)}")
    for name, adjacency in variants.items():
        info = spectral_diagnostics(adjacency)
        component_list = components(adjacency)
        component_sizes = [len(component) for component in component_list]
        degrees = info["degrees"]
        cut, conductance = sweep_cut(adjacency, info["fiedler"])
        edges = int(np.count_nonzero(adjacency) / 2)
        eigenvalues = info["laplacian_eigenvalues"]
        normalised_eigenvalues = info["normalised_eigenvalues"]
        print(
            f"{name}: edges={edges}; components={info['component_count']} "
            f"(sizes={component_sizes}); degrees="
            f"{','.join(f'{node}:{degree:g}' for node, degree in zip(nodes, degrees))}"
        )
        print(
            f"  spectrum: lambda2={eigenvalues[1]:.6f}; "
            f"lambda_max={eigenvalues[-1]:.6f}; "
            f"normalised_lambda2={normalised_eigenvalues[1]:.6f}"
        )
        print(
            f"  sweep cut: conductance={conductance:.6f}; "
            f"side={format_nodes(cut, nodes)}"
        )

    assert [len(component) for component in components(variants["binary"])] == [len(nodes)]
    print("Validation: passed (symmetry, components, spectra, and sweep cuts)")


if __name__ == "__main__":
    main()
