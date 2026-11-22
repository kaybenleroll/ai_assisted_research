#!/usr/bin/env python3
"""Generate deterministic GLM teaching figures from analytic examples/data."""

from __future__ import annotations

import csv
import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta, gamma, lognorm, nbinom, poisson


PRIMER_ROOT = Path(__file__).resolve().parents[1]
OUT = PRIMER_ROOT / "figures"
PENGUINS = PRIMER_ROOT / "data" / "penguins.csv"

COLORS = {
    "blue": "#0072B2",
    "orange": "#D55E00",
    "green": "#009E73",
    "purple": "#CC79A7",
    "sky": "#56B4E9",
    "yellow": "#E69F00",
    "dark": "#333333",
    "grey": "#777777",
}
SPECIES_STYLE = {
    "Adelie": (COLORS["blue"], "o"),
    "Chinstrap": (COLORS["orange"], "s"),
    "Gentoo": (COLORS["green"], "^"),
}

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.labelsize": 10,
        "legend.fontsize": 8.5,
        "figure.dpi": 120,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": "#D9DDE2",
        "grid.linewidth": 0.6,
        "grid.alpha": 0.8,
    }
)


def save(fig: plt.Figure, name: str) -> None:
    fig.savefig(OUT / name, dpi=300, facecolor="white")
    plt.close(fig)


def poisson_means() -> None:
    x = np.arange(0, 19)
    fig, ax = plt.subplots(figsize=(6.8, 4.3), constrained_layout=True)
    for mu, color, marker in [
        (0.5, COLORS["blue"], "o"),
        (2.0, COLORS["orange"], "s"),
        (6.0, COLORS["green"], "^"),
    ]:
        p = poisson.pmf(x, mu)
        assert np.all(p >= 0)
        assert np.isclose(p.sum() + poisson.sf(18, mu), 1.0, atol=1e-12)
        ax.vlines(x, 0, p, color=color, alpha=0.65, lw=1.3)
        ax.plot(x, p, marker=marker, linestyle="none", color=color, ms=4,
                label=fr"$\mu={mu:g}$")
    ax.set(title="Poisson probability mass changes with its mean",
           xlabel="Count, $y$ (events per observation)", ylabel="Probability, $P(Y=y)$",
           xlim=(-0.5, 18.5), ylim=(0, 0.68))
    ax.legend(title="Mean", frameon=True)
    save(fig, "01-poisson-means.png")


def inverse_links() -> None:
    eta = np.linspace(-6, 6, 601)
    p = 1 / (1 + np.exp(-eta))
    mu = np.exp(eta)
    assert np.all((p > 0) & (p < 1))
    assert np.all(mu > 0)
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.8), constrained_layout=True)
    axes[0].plot(eta, p, color=COLORS["blue"], lw=2.5)
    axes[0].axhline(0.5, color=COLORS["grey"], lw=0.9, ls="--")
    axes[0].set(title="Logit inverse link", xlabel="Linear predictor, $\\eta$",
                ylabel="Mean probability, $\\mu=1/(1+e^{-\\eta})$",
                xlim=(-6, 6), ylim=(-0.03, 1.03))
    axes[1].plot(eta, mu, color=COLORS["orange"], lw=2.5)
    axes[1].set(title="Log inverse link", xlabel="Linear predictor, $\\eta$",
                ylabel="Mean count/rate, $\\mu=e^\\eta$",
                xlim=(-6, 6), yscale="log", ylim=(1e-3, 1e3))
    fig.suptitle("The inverse link maps predictor values to valid means", fontsize=13)
    save(fig, "02-inverse-links.png")


def penguins() -> tuple[int, int, int]:
    rows: list[dict[str, str]] = []
    with PENGUINS.open(newline="", encoding="utf-8") as stream:
        rows.extend(csv.DictReader(stream))
    assert len(rows) == 344
    complete = [
        r for r in rows
        if r["body_mass_g"] not in ("", "NA") and r["flipper_length_mm"] not in ("", "NA")
    ]
    assert all(r["species"] in SPECIES_STYLE for r in complete)
    omitted = len(rows) - len(complete)
    fig, ax = plt.subplots(figsize=(7.2, 4.7), constrained_layout=True)
    for species, (color, marker) in SPECIES_STYLE.items():
        group = [r for r in complete if r["species"] == species]
        x = np.array([float(r["flipper_length_mm"]) for r in group])
        y = np.array([float(r["body_mass_g"]) for r in group])
        assert len(group) > 0 and np.all(np.isfinite(x)) and np.all(np.isfinite(y))
        ax.scatter(x, y, s=30, alpha=0.78, edgecolors="white", linewidths=0.35,
                   c=color, marker=marker, label=f"{species} (n={len(group)})")
    ax.set(title="Palmer penguins: body mass and flipper length",
           xlabel="Flipper length (mm)", ylabel="Body mass (g)")
    ax.legend(title="Species", frameon=True)
    ax.text(0.01, 0.99,
            f"Frozen package CSV: 344 rows; {omitted} omitted for missing plotted values; n={len(complete)} shown",
            transform=ax.transAxes, ha="left", va="top", fontsize=8.1,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.86, "pad": 3})
    save(fig, "03-penguins-mass-flipper.png")
    return len(rows), len(complete), omitted


def matched_positive_distributions() -> None:
    x = np.linspace(1e-4, 11, 1000)
    # Gamma: shape=3, scale=1 -> mean=3 and variance=3.
    k, theta = 3.0, 1.0
    # Lognormal matched on mean/variance, not on shape parameters.
    mean, variance = 3.0, 3.0
    sigma2 = np.log1p(variance / mean**2)
    sigma = np.sqrt(sigma2)
    log_mu = np.log(mean) - sigma2 / 2
    assert np.isclose(k * theta, mean)
    assert np.isclose(k * theta**2, variance)
    assert np.isclose(np.exp(log_mu + sigma2 / 2), mean)
    assert np.isclose((np.exp(sigma2) - 1) * np.exp(2 * log_mu + sigma2), variance)
    fig, ax = plt.subplots(figsize=(6.8, 4.3), constrained_layout=True)
    ax.plot(x, gamma.pdf(x, a=k, scale=theta), color=COLORS["blue"], lw=2.4,
            label=r"Gamma: shape $3$, scale $1$")
    ax.plot(x, lognorm.pdf(x, s=sigma, scale=np.exp(log_mu)), color=COLORS["orange"],
            lw=2.4, ls="--", label="Lognormal: matched moments")
    ax.set(title="Different positive distributions can share two moments",
           xlabel="Positive response, $y$", ylabel="Density, $f(y)$", xlim=(0, 11), ylim=(0, None))
    ax.text(0.98, 0.96, "Both: mean 3, variance 3; support $y>0$",
            transform=ax.transAxes, ha="right", va="top", fontsize=8.7)
    ax.legend(frameon=True)
    save(fig, "04-matched-positive-distributions.png")


def poisson_vs_nb() -> None:
    mu, shape = 2.0, 1.5
    x = np.arange(0, 15)
    pp = poisson.pmf(x, mu)
    # NB2 variance = mu + mu**2 / shape.
    p = shape / (shape + mu)
    pn = nbinom.pmf(x, shape, p)
    assert np.isclose(shape * (1 - p) / p, mu)
    assert np.isclose(shape * (1 - p) / p**2, mu + mu**2 / shape)
    assert np.all(pp >= 0) and np.all(pn >= 0)
    fig, ax = plt.subplots(figsize=(6.8, 4.3), constrained_layout=True)
    for probs, color, marker, label in [
        (pp, COLORS["blue"], "o", "Poisson, mean 2"),
        (pn, COLORS["orange"], "s", "Negative binomial NB2, mean 2, shape 1.5"),
    ]:
        ax.vlines(x, 0, probs, color=color, alpha=0.55, lw=1.1)
        ax.plot(x, probs, marker=marker, linestyle="none", color=color, ms=4, label=label)
    ax.set(title="NB2 allows greater count variation at the same mean",
           xlabel="Count, $y$", ylabel="Probability, $P(Y=y)$", xlim=(-0.5, 14.5))
    ax.legend(frameon=True)
    save(fig, "05-poisson-nb2.png")


def truncated_power_basis() -> None:
    x = np.linspace(-2, 2, 401)
    curves = [
        (x, r"$x$", COLORS["blue"], "-"),
        (x**2, r"$x^2$", COLORS["orange"], "--"),
        (x**3, r"$x^3$", COLORS["green"], "-.") ,
        (np.maximum(x, 0) ** 3, r"$\max(x,0)^3$", COLORS["purple"], ":"),
    ]
    assert np.allclose(curves[3][0][x <= 0], 0)
    fig, ax = plt.subplots(figsize=(6.8, 4.3), constrained_layout=True)
    for y, label, color, linestyle in curves:
        ax.plot(x, y, color=color, ls=linestyle, lw=2.2, label=label)
    ax.axvline(0, color=COLORS["grey"], lw=0.9, ls="--")
    ax.set(title="Illustrative cubic and truncated-power basis functions",
           xlabel="Input, $x$", ylabel="Basis value", xlim=(-2, 2), ylim=(-8.5, 8.5))
    ax.legend(title="Basis term", ncol=2, frameon=True)
    fig.text(0.5, -0.02, "Illustration only: these are basis functions, not a fitted GAM or REML result.",
             ha="center", fontsize=8.4)
    save(fig, "06-truncated-power-basis.png")


def zip_vs_hurdle() -> float:
    lam, pi = 2.0, 0.3
    p_zero = pi + (1 - pi) * poisson.pmf(0, lam)
    x = np.arange(0, 13)
    zip_p = (1 - pi) * poisson.pmf(x, lam)
    zip_p[0] += pi
    hurdle_p = np.empty_like(zip_p)
    hurdle_p[0] = p_zero
    hurdle_p[1:] = (1 - p_zero) * poisson.pmf(x[1:], lam) / (1 - poisson.pmf(0, lam))
    diff = float(np.max(np.abs(zip_p - hurdle_p)))
    assert 0 < p_zero < 1 and diff < 1e-14
    assert np.isclose(zip_p.sum(), 1.0, atol=1e-12)
    assert np.isclose(hurdle_p.sum(), 1.0, atol=1e-12)
    fig, ax = plt.subplots(figsize=(6.8, 4.3), constrained_layout=True)
    for probs, color, marker, label in [
        (zip_p, COLORS["blue"], "o", r"ZIP: $\lambda=2,\;\pi=0.3$"),
        (hurdle_p, COLORS["orange"], "s", fr"Hurdle: Poisson positives, $p_0={p_zero:.3f}$"),
    ]:
        ax.vlines(x, 0, probs, color=color, alpha=0.55, lw=1.1)
        ax.plot(x, probs, marker=marker, linestyle="none", color=color, ms=4, label=label)
    ax.set(title="Different zero mechanisms can yield the same count law",
           xlabel="Count, $y$", ylabel="Probability, $P(Y=y)$", xlim=(-0.5, 12.5))
    ax.legend(frameon=True)
    ax.text(0.98, 0.96, fr"Equivalent hurdle zero probability: $p_0={p_zero:.4f}$",
            transform=ax.transAxes, ha="right", va="top", fontsize=8.7)
    save(fig, "07-zip-hurdle-equivalence.png")
    return diff


def hierarchical_shrinkage() -> None:
    labels = ["Group 1", "Group 2", "Group 3", "Group 4"]
    raw = np.array([0.1, 0.4, 0.7, 0.9])
    posterior = np.array([0.25752, 0.44502, 0.63252, 0.75752])
    assert np.all((raw >= 0) & (raw <= 1) & (posterior >= 0) & (posterior <= 1))
    assert np.all(np.abs(posterior - raw) < 0.2)
    ix = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(7.0, 4.4), constrained_layout=True)
    width = 0.34
    ax.bar(ix - width / 2, raw, width, color=COLORS["sky"], edgecolor=COLORS["blue"],
           label="Observed proportion")
    ax.bar(ix + width / 2, posterior, width, color=COLORS["orange"], alpha=0.86,
           label="Executed posterior mean")
    ax.set(title="Partial pooling shrinks group estimates toward a shared mean",
           xlabel="Group", ylabel="Success proportion / probability", xticks=ix,
           xticklabels=labels, ylim=(0, 1))
    ax.legend(frameon=True, loc="upper left")
    ax.text(0.99, 0.97,
            "Beta-binomial hierarchy; concentration fixed at 6;\ncommon hypermean uncertain (integrated over its posterior).",
            transform=ax.transAxes, ha="right", va="top", fontsize=8.4,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.88, "pad": 3})
    save(fig, "08-hierarchical-shrinkage.png")


def beta_prior_posterior() -> None:
    x = np.linspace(0, 1, 501)
    prior = beta.pdf(x, 2, 2)
    posterior = beta.pdf(x, 4, 10)
    prior_mean = 2 / 4
    post_mean = 4 / 14
    assert np.isclose(4, 2 + 2) and np.isclose(10, 2 + 8)
    assert np.all(prior >= 0) and np.all(posterior >= 0)
    fig, ax = plt.subplots(figsize=(6.8, 4.3), constrained_layout=True)
    ax.plot(x, prior, color=COLORS["blue"], lw=2.4, label=r"Prior: Beta$(2,2)$")
    ax.plot(x, posterior, color=COLORS["orange"], lw=2.4,
            label=r"Posterior: Beta$(4,10)$ after 2 successes, 8 failures")
    ax.axvline(prior_mean, color=COLORS["blue"], ls=":", lw=1.2)
    ax.axvline(post_mean, color=COLORS["orange"], ls=":", lw=1.2)
    ax.set(title="A binomial observation updates a beta prior",
           xlabel="Success probability, $\\theta$", ylabel="Density",
           xlim=(0, 1), ylim=(0, None))
    ax.legend(frameon=True)
    save(fig, "09-beta-prior-posterior.png")


def main() -> None:
    global OUT, PENGUINS
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=PRIMER_ROOT / "figures")
    parser.add_argument("--data-dir", type=Path, default=PRIMER_ROOT / "data")
    args = parser.parse_args()
    OUT = args.output_dir.resolve()
    PENGUINS = args.data_dir.resolve() / "penguins.csv"
    OUT.mkdir(parents=True, exist_ok=True)
    poisson_means()
    inverse_links()
    penguin_n, penguin_complete, penguin_omitted = penguins()
    matched_positive_distributions()
    poisson_vs_nb()
    truncated_power_basis()
    zip_difference = zip_vs_hurdle()
    hierarchical_shrinkage()
    beta_prior_posterior()
    print("ASSERTIONS PASSED")
    print(f"penguins rows={penguin_n} plotted_complete={penguin_complete} omitted={penguin_omitted}")
    print(f"ZIP/hurdle max probability difference={zip_difference:.3g}")
    print(f"figures={len(list(OUT.glob('*.png')))} output_dir={OUT}")


if __name__ == "__main__":
    main()
