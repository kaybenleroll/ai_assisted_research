# Validate R-fitted held-out predictions, without refitting the model.
using Printf
lines=readlines("examples/combined-fixture.csv")
@assert length(lines)==5
rows=[parse.(Float64,split(line,',')) for line in lines[2:end]]
y=Int.([r[1] for r in rows]); eta=[r[2] for r in rows]
theta,sigma,b=rows[1][3:5]
@assert y==[0,0,1,2] && theta>0 && sigma>0
@assert all(r[3:5]==rows[1][3:5] && r[8]==rows[1][8] for r in rows)
conditional=exp.(eta .+ b); integrated=exp.(eta .+ sigma^2/2)
@assert maximum(abs.(conditional.-[r[6] for r in rows]))<1e-10
@assert maximum(abs.(integrated.-[r[7] for r in rows]))<1e-10
function score(n)
 vals=Float64[]
 for i in 1:n
  z=-9+(i-.5)*18/n
  total=-z*z/2-log(2*pi)/2
  for j in eachindex(y)
   mu=exp(eta[j]+sigma*z)
   # Rising factorial avoids any external special-functions package.
   comb=sum((log(theta+k) for k in 0:y[j]-1);init=0.0)-sum((log(k) for k in 1:y[j]);init=0.0)
   total+=comb+theta*log(theta/(theta+mu))+y[j]*log(mu/(theta+mu))
  end
  push!(vals,total)
 end
 a=maximum(vals); a+log(sum(exp.(vals.-a))*18/n)
end
lo,hi=score(1600),score(3200)
@assert abs(lo-hi)<1e-7 && abs(hi-rows[1][8])<1e-9
@printf("Conditional means %s; integrated means %s; joint log density %.10f\n",conditional,integrated,hi)
# Integrate conditional NB probabilities over one new site's normal effect.
function future_cdf(n, limit)
 out=zeros(81)
 for j in 1:n
  z=-limit+(j-.5)*2*limit/n
  w=exp(-z*z/2)/sqrt(2*pi)*2*limit/n
  mu=exp(eta[1]+sigma*z); p=theta/(theta+mu); mass=p^theta; cumulative=0.0
  for k in 0:80
   if k>0; mass*=((theta+k-1)/k)*(1-p); end
   cumulative+=mass; out[k+1]+=w*cumulative
  end
 end
 out
end
f=future_cdf(3200,9); coarse=future_cdf(1600,9); wide=future_cdf(3200,10)
@assert maximum(abs.(f.-coarse))<1e-7 && maximum(abs.(f.-wide))<1e-7
@assert abs(1-f[end])<1e-10 && all(diff(f).>=0)
quantiles=[findfirst(x->x>=p,f)-1 for p in (.025,.975)]
@assert quantiles==Int.(rows[1][9:10]) && abs(f[quantiles[2]+1]-rows[1][11])<1e-10
@printf("Future count interval %s; F(upper) %.10f; remaining tail %.3g\n",quantiles,f[quantiles[2]+1],1-f[end])
