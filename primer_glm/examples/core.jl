using LinearAlgebra, Printf
x=collect(range(-1.5,1.5,length=24)); g=repeat([0.,1.],12)
ybin=[0,1,0,0,1,0,1,0,0,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1]; ycount=[1,2,1,3,0,2,2,1,3,2,4,1,2,4,3,3,5,2,4,5,3,6,4,7]; effort=repeat([1.,2.,1.5],8)
ygauss=4 .+ 0.7 .* x .+ 0.4 .* g .+ repeat([-.3,.2,.1,-.2],6); ygamma=exp.(.5 .+ 0.3 .* x .+ 0.2 .* g).*repeat([.7,1.2,.9,1.3],6)
X=hcat(ones(24),x,g); P=[1. -.7 0.; 1. .8 1.]
function fit(y,fam,offset)
 b=zeros(3)
 for i in 1:200
  eta=X*b+offset
  if fam=="gaussian"; mu=eta; der=ones(24); variance=ones(24)
  elseif fam=="binomial"; mu=1 ./ (1 .+ exp.(-eta)); der=mu.*(1 .- mu); variance=der
  elseif fam=="poisson"; mu=exp.(eta); der=mu; variance=mu
  else; mu=exp.(eta); der=mu; variance=mu.^2
  end
  w=der.^2 ./ variance; z=eta+(y-mu)./der-offset
  nb=(X'*(w.*X))\(X'*(w.*z))
  if maximum(abs.(nb-b))<1e-12; return nb; end
  b=nb
 end
 error("$fam did not converge")
end
reference=Dict("gaussian"=>[3.41,4.96], "binomial"=>[.5602052091,.6537850817], "poisson"=>[1.5197656922,5.8214687823], "gamma"=>[1.0600187949,3.2313426836])
for (name,y,off) in [("gaussian",ygauss,zeros(24)),("binomial",ybin,zeros(24)),("poisson",ycount,log.(effort)),("gamma",ygamma,zeros(24))]
 b=fit(y,name,off); eta=P*b+(name=="poisson" ? log.([1.3,2.1]) : zeros(2))
 pred=name=="gaussian" ? eta : name=="binomial" ? 1 ./ (1 .+ exp.(-eta)) : exp.(eta)
 @assert maximum(abs.(pred-reference[name]))<1e-7
 @printf("%s %.10f %.10f\n",name,pred[1],pred[2])
end
