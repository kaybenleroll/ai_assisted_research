import numpy as np
x=np.linspace(-1.5,1.5,24); g=np.tile([0.,1.],12)
ybin=np.array([0,1,0,0,1,0,1,0,0,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1]); ycount=np.array([1,2,1,3,0,2,2,1,3,2,4,1,2,4,3,3,5,2,4,5,3,6,4,7]); effort=np.tile([1.,2.,1.5],8)
ygauss=4+.7*x+.4*g+np.tile([-.3,.2,.1,-.2],6); ygamma=np.exp(.5+.3*x+.2*g)*np.tile([.7,1.2,.9,1.3],6)
X=np.column_stack([np.ones(24),x,g]); P=np.array([[1,-.7,0],[1,.8,1]])
def fit(y,fam,offset):
 b=np.zeros(3)
 for i in range(200):
  eta=X@b+offset
  if fam=='gaussian': mu=eta; der=np.ones(24); variance=np.ones(24)
  elif fam=='binomial': mu=1/(1+np.exp(-eta)); der=mu*(1-mu); variance=der
  elif fam=='poisson': mu=np.exp(eta); der=mu; variance=mu
  else: mu=np.exp(eta); der=mu; variance=mu*mu
  w=der*der/variance; z=eta+(y-mu)/der-offset
  nb=np.linalg.solve(X.T@(w[:,None]*X),X.T@(w*z))
  if np.max(abs(nb-b))<1e-12: return nb
  b=nb
 raise RuntimeError(f'{fam} did not converge')
reference={'gaussian':[3.41,4.96], 'binomial':[.5602052091,.6537850817], 'poisson':[1.5197656922,5.8214687823], 'gamma':[1.0600187949,3.2313426836]}
for name,y,off in [('gaussian',ygauss,np.zeros(24)),('binomial',ybin,np.zeros(24)),('poisson',ycount,np.log(effort)),('gamma',ygamma,np.zeros(24))]:
 b=fit(y,name,off); eta=P@b+(np.log([1.3,2.1]) if name=='poisson' else 0)
 pred=eta if name=='gaussian' else 1/(1+np.exp(-eta)) if name=='binomial' else np.exp(eta)
 assert np.max(np.abs(pred-np.array(reference[name])))<1e-7
 print(name,*[f'{v:.10f}' for v in pred])
