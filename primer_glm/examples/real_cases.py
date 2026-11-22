"""Matched descriptive GLMs on frozen penguins and package-derived salamanders."""
import csv
import hashlib
from pathlib import Path
import numpy as np


def rows(path, expected):
    raw = Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected
    return list(csv.DictReader(raw.decode().splitlines()))


def fit(X, y, family):
    """Fisher scoring for this full-rank, bounded example only."""
    beta = np.zeros(X.shape[1]); beta[0] = np.log(np.mean(y))
    for _ in range(300):
        eta = X @ beta
        mu = np.exp(eta)
        weight = mu if family == 'poisson' else np.ones(len(y))
        work = eta + (y - mu) / mu
        updated = np.linalg.solve(X.T @ (weight[:, None] * X), X.T @ (weight * work))
        if np.max(np.abs(updated - beta)) < 1e-11:
            return updated
        beta = updated
    raise RuntimeError(f'{family} did not converge')


penguins = rows('data/penguins.csv', 'f204db2c753b0937caac3cb35258562c14f073e4bbc76be24b4c51ce22767a93')
p = [r for r in penguins if r['body_mass_g'] not in ('NA', '') and r['species'] not in ('NA', '')]
assert len(penguins) == 344 and len(p) == 342
species = np.array([r['species'] for r in p]); island = np.array([r['island'] for r in p])
y = np.array([float(r['body_mass_g']) for r in p]); assert np.all(y > 0)
c = (species == 'Chinstrap').astype(float); g = (species == 'Gentoo').astype(float)
d = (island == 'Dream').astype(float); t = (island == 'Torgersen').astype(float)
X = np.column_stack([np.ones(len(p)), c, g]); additive = np.column_stack([X, d, t]); interaction = np.column_stack([additive, c*d, c*t, g*d, g*t])
assert np.linalg.matrix_rank(additive) == 5 and np.linalg.matrix_rank(interaction) == 5 and interaction.shape[1] == 9
beta = np.linalg.lstsq(X, y, rcond=None)[0]; P = np.array([[1,0,0],[1,1,0],[1,0,1]])
gaussian = P @ beta; gamma = np.exp(P @ fit(X, y, 'gamma'))
reference = np.array([3700.66225165563,3733.08823529412,5076.0162601626])
assert np.allclose(gaussian, reference, atol=1e-5, rtol=0) and np.allclose(gamma, reference, atol=1e-5, rtol=0)
print('penguins n',len(p),'additive rank',np.linalg.matrix_rank(additive),'interaction rank/columns',np.linalg.matrix_rank(interaction),interaction.shape[1])
print('gaussian means',gaussian,'gamma means',gamma,'Gentoo minus Adelie',gaussian[2]-gaussian[0],'Gamma mean ratio',gamma[2]/gamma[0])

sal = rows('data/salamanders-package.csv', '1dadca43a8c917da58cd341fb04f15c0ad22384a8487a33dc3f6b77516bf8874')
s = [r for r in sal if r['spp'] == 'GP']
assert len(sal) == 644 and len(s) == 92 and len({r['site'] for r in s}) == 23
assert all(sum(row['site'] == site for row in s) == 4 for site in {r['site'] for r in s})
X = np.array([[1.,float(r['mined'] == 'yes'),float(r['DOP'])] for r in s]); y = np.array([float(r['count']) for r in s])
assert np.linalg.matrix_rank(X) == 3 and np.all(y >= 0)
beta = fit(X, y, 'poisson'); predicted = np.exp(np.array([[1,0,0],[1,1,0]]) @ beta)
assert np.allclose(predicted,[2.20610650201214,0.045503366405712],atol=1e-6,rtol=0)
print('salamanders GP n',len(s),'sites',len({r['site'] for r in s}),'poisson coefficients',beta,'DOP 0 predicted counts',predicted)
