"""Poisson fit with fixed-penalty truncated-power cubic spline; compare gam.R and mgcv."""
import numpy as np
from scipy.optimize import minimize
x=np.linspace(-1.5,1.5,24); y=np.array([1,2,1,3,0,2,2,1,3,2,4,1,2,4,3,3,5,2,4,5,3,6,4,7]); X=np.column_stack([np.ones(24),x,x*x,x**3,np.maximum(x,0)**3]); S=np.diag([0,0,4,4,4])
def f(b): return np.sum(np.exp(X@b)-y*(X@b))+b@S@b/2
def grad(b): return X.T@(np.exp(X@b)-y)+S@b
res=minimize(f,np.zeros(5),jac=grad,method='BFGS',tol=1e-10)
assert max(abs(grad(res.x)))<1e-7
assert np.allclose(res.x,[.9567229578,.4313560726,-.0098296418,.0106001189,.0523179112],atol=1e-5)
p=np.array([[1,-.7,.49,-.343,0],[1,.8,.64,.512,.512]]); print('penalised coefficients',res.x,'prediction',np.exp(p@res.x),'max score',max(abs(grad(res.x))))
