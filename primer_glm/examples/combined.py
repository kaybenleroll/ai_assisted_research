"""Validate the R-fitted, held-out site's predictions; this is not a refit."""
import csv, math
from pathlib import Path
import numpy as np
from scipy.special import gammaln, logsumexp
with Path('examples/combined-fixture.csv').open(newline='') as f:
    rows = list(csv.DictReader(f))
y = np.array([int(r['y']) for r in rows]); eta = np.array([float(r['eta']) for r in rows])
theta, sigma, b = (float(rows[0][k]) for k in ('theta', 'sigma', 'conditional_b'))
assert len(rows)==4 and theta>0 and sigma>0 and list(y)==[0,0,1,2]
for key in ('theta','sigma','conditional_b','joint_log_score'):
    assert all(float(r[key])==float(rows[0][key]) for r in rows)
conditional = np.exp(eta+b); integrated = np.exp(eta+sigma*sigma/2)
assert np.max(np.abs(conditional-np.array([float(r['conditional_mean']) for r in rows])))<1e-10
assert np.max(np.abs(integrated-np.array([float(r['integrated_mean']) for r in rows])))<1e-10
def score(n):
    z=-9+(np.arange(n)+.5)*18/n
    mu=np.exp(eta[:,None]+sigma*z[None,:])
    logp=gammaln(y[:,None]+theta)-gammaln(theta)-gammaln(y[:,None]+1)+theta*np.log(theta/(theta+mu))+y[:,None]*np.log(mu/(theta+mu))
    return logsumexp(logp.sum(axis=0)-z*z/2-.5*math.log(2*math.pi))+math.log(18/n)
a, c=score(1600),score(3200)
assert abs(a-c)<1e-7 and abs(c-float(rows[0]['joint_log_score']))<1e-9
print('Conditional means:',conditional,'integrated means:',integrated,'joint log density:',c)
# Recurrence builds the conditional NB mass; normal integration yields a discrete mixture.
def future_cdf(n, limit):
    z=-limit+(np.arange(n)+.5)*2*limit/n
    weights=np.exp(-z*z/2)/math.sqrt(2*math.pi)*2*limit/n
    mu=np.exp(eta[0]+sigma*z); p=theta/(theta+mu)
    mass=p**theta; cdf=[]; total=0.0
    for k in range(81):
        if k: mass=mass*((theta+k-1)/k)*(1-p)
        total+=float(np.dot(weights,mass)); cdf.append(total)
    return np.array(cdf)
f=future_cdf(3200,9); coarse=future_cdf(1600,9); wide=future_cdf(3200,10)
assert np.max(abs(f-coarse))<1e-7 and np.max(abs(f-wide))<1e-7
assert abs(1-f[-1])<1e-10 and np.all(np.diff(f)>=0)
quantiles=[int(np.searchsorted(f,p)) for p in (.025,.975)]
assert quantiles==[int(rows[0]['predictive_lower']),int(rows[0]['predictive_upper'])]
assert abs(f[quantiles[1]]-float(rows[0]['predictive_cdf_upper']))<1e-10
print('Future count interval:',quantiles,'F(upper):',f[quantiles[1]],'remaining tail:',1-f[-1])
