using ForwardDiff
using LinearAlgebra
using Statistics
using Zygote

const EXPECTED_FORWARD_DIFF = v"0.10.39"
const EXPECTED_ZYGOTE = v"0.7.10"

version = VERSION
forwarddiff_version = pkgversion(ForwardDiff)
zygote_version = pkgversion(Zygote)

@assert version == v"1.12.7" "Unexpected Julia version: $version"
@assert forwarddiff_version == EXPECTED_FORWARD_DIFF "Unexpected ForwardDiff version: $forwarddiff_version"
@assert zygote_version == EXPECTED_ZYGOTE "Unexpected Zygote version: $zygote_version"

f(x) = sin(x^2)
scalar_point = π / 4
expected_scalar_derivative = 2scalar_point * cos(scalar_point^2)
forwarddiff_derivative = ForwardDiff.derivative(f, scalar_point)
zygote_gradient = only(Zygote.gradient(f, scalar_point))

@assert isapprox(forwarddiff_derivative, expected_scalar_derivative; atol = 1e-12)
@assert isapprox(zygote_gradient, expected_scalar_derivative; atol = 1e-12)

F(x) = [sin(x[1]), x[1] * x[2], exp(x[2])]
x0 = [1.0, 2.0]
expected_jacobian = [cos(1.0) 0.0; 2.0 1.0; 0.0 exp(2.0)]
jacobian = ForwardDiff.jacobian(F, x0)
@assert isapprox(jacobian, expected_jacobian; atol = 1e-12)

# Four-point regularised logistic fixture from primer_ml_optimisation.
X = [1.0 0.0; 1.0 1.0; 1.0 2.0; 1.0 -1.0]
y = [0.0, 1.0, 1.0, 0.0]
λ = 0.1
θ = [0.2, -0.3]
v = [0.4, -0.2]

softplus(s) = max(s, 0) + log1p(exp(-abs(s)))
logits(t) = X * t
objective(t) = mean(softplus.(logits(t)) - y .* logits(t)) + λ / 2 * dot(t, t)

forward_gradient = ForwardDiff.gradient(objective, θ)
reverse_gradient = Zygote.gradient(objective, θ)[1]
jvp_logits = ForwardDiff.jacobian(a -> logits(θ .+ only(a) .* v), [0.0])[:, 1]
hvp = Zygote.hessian(objective, θ) * v
probabilities = 1.0 ./ (1.0 .+ exp.(-logits(θ)))
weights = probabilities .* (1.0 .- probabilities)
expected_hvp = X' * (weights .* (X * v)) / length(y) + λ * v

@assert isapprox(forward_gradient, reverse_gradient; atol = 1e-10, rtol = 1e-10)
@assert isapprox(jvp_logits, X * v; atol = 1e-10, rtol = 1e-10)
@assert isapprox(hvp, expected_hvp; atol = 1e-10, rtol = 1e-10)

println("primer-julia-probe: Julia=$version ForwardDiff=$forwarddiff_version Zygote=$zygote_version scalar_derivative=$forwarddiff_derivative jacobian=$jacobian")
println("logistic: gradient=$forward_gradient JVP=$jvp_logits HVP=$hvp")
