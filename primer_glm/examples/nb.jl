using LinearAlgebra, ForwardDiff, Printf
x=collect(range(-1.5,1.5,length=24)); g=repeat([0.,1.],12); y=[1,2,1,3,0,2,2,1,3,2,4,1,2,4,3,3,5,2,4,5,3,6,4,7]; effort=repeat([1.,2.,1.5],8); X=hcat(ones(24),x,g); theta=2.
function objective(b)
 eta=X*b+log.(effort); sum((y .+ theta).*log.(theta .+ exp.(eta)) - y.*eta)
end
b=zeros(3)
for i in 1:30
 grad=ForwardDiff.gradient(objective,b); H=ForwardDiff.hessian(objective,b); delta=H\grad
 global b=b-delta
 maximum(abs.(grad))<1e-9 && break
end
score=ForwardDiff.gradient(objective,b); @assert maximum(abs.(score))<1e-7
@printf("max_abs_score %.3g\n",maximum(abs.(score)))
@printf("coefficients %.10f %.10f %.10f\n",b...)
pred=exp.([1. -.7 0.; 1. .8 1.]*b+log.([1.3,2.1])); @printf("prediction %.10f %.10f\n",pred...)
@assert maximum(abs.(pred-[1.6070231217,6.0269527481]))<1e-5
