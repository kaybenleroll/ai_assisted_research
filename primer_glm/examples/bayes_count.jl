# Integer-shape Gamma and NB CDFs; no non-standard package is needed.
using Printf
counts=[0,0,0,0,0,0,0,3,4,5,7,9]; @assert length(counts)==12 && sum(counts)==28
shape=2+sum(counts); rate=1+length(counts)
# Gamma(integer shape, rate) CDF is the survival probability of Poisson(rate*x).
function gamma_cdf(x,shape,rate)
    z=rate*x; term=1.0; acc=term
    for k in 1:shape-1
        term*=z/k; acc+=term
    end
    1-exp(-z)*acc
end
function gamma_quantile(p)
    lo=0.; hi=10.
    @assert gamma_cdf(hi,shape,rate)>p
    for _ in 1:100
        mid=(lo+hi)/2
        if gamma_cdf(mid,shape,rate)<p; lo=mid; else; hi=mid; end
    end
    (lo+hi)/2
end
# NB(size, success probability) recursion for integer counts.
function nb_quantile(p,size,success)
    mass=success^size; cumulative=mass; k=0
    while cumulative<p
        mass*=(k+size)/(k+1)*(1-success); k+=1; cumulative+=mass
        @assert k<10000
    end
    k
end
ci=[gamma_quantile(.025),gamma_quantile(.975)]; prediction=[nb_quantile(.025,shape,rate/(rate+1)),nb_quantile(.975,shape,rate/(rate+1))]
@assert abs(ci[1]-1.55699)<1e-4 && abs(ci[2]-3.20376)<1e-4 && prediction==[0,6]
@printf("posterior shape/rate %d %d mean %.8f credible interval %.8f %.8f predictive interval %d %d\n",shape,rate,shape/rate,ci...,prediction...)
