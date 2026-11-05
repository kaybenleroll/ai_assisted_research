"""Generate deterministic figures for the spectral graph theory primer."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).parent
FIGURES = ROOT / "figures"


def laplacian(adjacency: np.ndarray) -> np.ndarray:
    return np.diag(adjacency.sum(axis=1)) - adjacency


def path(n: int) -> np.ndarray:
    adjacency = np.zeros((n, n))
    for i in range(n - 1):
        adjacency[i, i + 1] = adjacency[i + 1, i] = 1
    return adjacency


def cycle(n: int) -> np.ndarray:
    adjacency = path(n)
    adjacency[0, -1] = adjacency[-1, 0] = 1
    return adjacency


def star(n: int) -> np.ndarray:
    adjacency = np.zeros((n, n))
    adjacency[0, 1:] = adjacency[1:, 0] = 1
    return adjacency


def clique(n: int) -> np.ndarray:
    return np.ones((n, n)) - np.eye(n)


def bridge_graph(epsilon: float) -> np.ndarray:
    adjacency = np.zeros((6, 6))
    for offset in (0, 3):
        for i in range(offset, offset + 3):
            for j in range(i + 1, offset + 3):
                adjacency[i, j] = adjacency[j, i] = 1
    adjacency[2, 3] = adjacency[3, 2] = epsilon
    return adjacency


def save_spectra() -> None:
    graphs = {
        "Path $P_6$": path(6),
        "Cycle $C_6$": cycle(6),
        "Star $S_6$": star(6),
        "Clique $K_6$": clique(6),
    }
    fig, axes = plt.subplots(2, 2, figsize=(8.2, 5.8), sharex=True, sharey=True)
    for axis, (label, adjacency) in zip(axes.flat, graphs.items()):
        values = np.linalg.eigvalsh(laplacian(adjacency))
        axis.plot(np.arange(1, len(values) + 1), values, "o-")
        axis.set_title(label)
        axis.set_xlabel("eigenvalue index")
        axis.set_ylabel("$\\lambda_k$")
        axis.grid(alpha=0.25)
    fig.suptitle("Combinatorial Laplacian spectra of four small graphs")
    fig.tight_layout()
    fig.savefig(FIGURES / "small_graph_spectra.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def save_bridge() -> None:
    epsilons = np.logspace(-4, 0, 80)
    gaps = []
    normalised_gaps = []
    for epsilon in epsilons:
        adjacency = bridge_graph(float(epsilon))
        values = np.linalg.eigvalsh(laplacian(adjacency))
        degrees = adjacency.sum(axis=1)
        inv_sqrt = np.zeros_like(degrees)
        positive = degrees > 0
        inv_sqrt[positive] = 1 / np.sqrt(degrees[positive])
        normalised = np.eye(6) - inv_sqrt[:, None] * adjacency * inv_sqrt[None, :]
        normalised_values = np.linalg.eigvalsh(normalised)
        gaps.append(values[1])
        normalised_gaps.append(normalised_values[1])
    fig, axis = plt.subplots(figsize=(7.2, 4.2))
    axis.loglog(epsilons, gaps, label="$\\lambda_2(L)$")
    axis.loglog(epsilons, normalised_gaps, label="$\\nu_2(\\mathcal{L})$")
    axis.set_xlabel("bridge weight $\\varepsilon$")
    axis.set_ylabel("spectral gap")
    axis.set_title("Quantitative connectivity changes before disconnection")
    axis.grid(alpha=0.25, which="both")
    axis.legend()
    fig.tight_layout()
    fig.savefig(FIGURES / "weak_bridge_gaps.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def save_filters() -> None:
    eigenvalues = np.linspace(0, 2, 400)
    fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.6), sharey=True)
    for time in (0.25, 1, 4):
        axes[0].plot(eigenvalues, np.exp(-time * eigenvalues), label=f"$t={time:g}$")
    for tau in (0.25, 1, 4):
        axes[1].plot(eigenvalues, 1 / (1 + tau * eigenvalues), label=f"$\\tau={tau:g}$")
    axes[0].set_title("Heat response")
    axes[1].set_title("Tikhonov response")
    for axis in axes:
        axis.set_xlabel("normalised eigenvalue $\\lambda$")
        axis.grid(alpha=0.25)
        axis.legend()
    axes[0].set_ylabel("filter response $g(\\lambda)$")
    fig.suptitle("Low-pass responses preserve the constant mode")
    fig.tight_layout()
    fig.savefig(FIGURES / "spectral_filter_responses.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    save_spectra()
    save_bridge()
    save_filters()
    print("Generated three spectral graph figures")


if __name__ == "__main__":
    main()
