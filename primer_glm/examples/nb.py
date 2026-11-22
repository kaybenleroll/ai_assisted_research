import numpy as np
from scipy.optimize import minimize
x=np.linspace(-1.5,1.5,24);g=np.tile([0.,1.],12); y=np.array([1,2,1,3,0,2,2,1,3,2,4,1,2,4,3,3,5,2,4,5,3,6,4,7]); effort=np.tile([1.,2.,1.5],8); X=np.column_stack([np.ones(24),x,g]); theta=2.
def objective(b):
 eta=X@b+np.log(effort); return np.sum((y+theta)*np.logaddexp(np.log(theta),eta)-y*eta)
r=minimize(objective,np.zeros(3),method='BFGS',tol=1e-9)
# The optimizer can report precision loss near a stationary solution; test the analytical score.
mu=np.exp(X@r.x+np.log(effort)); score=X.T@((y-mu)/(1+mu/theta)); assert np.max(np.abs(score))<1e-5,(r.message,score)
print('optimizer',r.message,'max_abs_score',max(abs(score)))
print('coefficients',*[f'{v:.10f}' for v in r.x]); print('prediction',*[f'{v:.10f}' for v in np.exp(np.array([[1,-.7,0],[1,.8,1]])@r.x+np.log([1.3,2.1]))])
assert np.max(np.abs(np.exp(np.array([[1,-.7,0],[1,.8,1]])@r.x+np.log([1.3,2.1]))-np.array([1.6070231217,6.0269527481])))<1e-5
