# Fixed-penalty truncated-power cubic spline; reference fit is gam.R (mgcv).
using LinearAlgebra, ForwardDiff, Printf
x=collect(range(-1.5,1.5,length=24)); y=[1,2,1,3,0,2,2,1,3,2,4,1,2,4,3,3,5,2,4,5,3,6,4,7]; X=hcat(ones(24),x,x.^2,x.^3,max.(x,0).^3); S=Diagonal([0.,0.,4.,4.,4.])
f(b)=sum(exp.(X*b)-y.*(X*b))+dot(b,S*b)/2
b=zeros(5)
for i in 1:30
 grad=ForwardDiff.gradient(f,b); H=ForwardDiff.hessian(f,b); global b=b-H\grad
 maximum(abs.(grad))<1e-9 && break
end
score=maximum(abs.(ForwardDiff.gradient(f,b)))
@assert score<1e-7 && maximum(abs.(b-[.9567229578,.4313560726,-.0098296418,.0106001189,.0523179112]))<1e-5
p=exp.([1. -.7 .49 -.343 0.; 1. .8 .64 .512 .512]*b)
println("penalised coefficients ", b, "; prediction ", p, "; max score ", score)
