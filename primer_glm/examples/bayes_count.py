"""Conjugate Poisson–Gamma posterior and future-count interval."""
from scipy.stats import gamma, nbinom
counts = [0,0,0,0,0,0,0,3,4,5,7,9]
assert len(counts) == 12 and sum(counts) == 28
shape = 2 + sum(counts); rate = 1 + len(counts)
mean = shape / rate
credible = gamma.ppf([.025,.975], a=shape, scale=1/rate)
predictive = nbinom.ppf([.025,.975], n=shape, p=rate/(rate+1))
assert abs(mean-30/13)<1e-12
assert abs(credible[0]-1.55699)<1e-4 and abs(credible[1]-3.20376)<1e-4
assert tuple(predictive) == (0,6)
print('posterior shape/rate',shape,rate,'mean',mean,'credible interval',credible,'predictive interval',predictive)
