"""Check AD derivatives of the primer's four-point logistic loss."""

using ForwardDiff
using Zygote
using LinearAlgebra
using Statistics

X = [1.0 0.0; 1.0 1.0; 1.0 2.0; 1.0 -1.0]
y = [0.0, 1.0, 1.0, 0.0]
λ = 0.1
θ = [0.2, -0.3]
v = [0.4, -0.2]

softplus(s) = max(s, zero(s)) + log1p(exp(-abs(s)))
logits(t) = X * t
objective(t) = mean(softplus.(logits(t)) - y .* logits(t)) + λ / 2 * dot(t, t)

function check(actual, expected, label; tolerance=1e-10)
    @assert all(isfinite, actual isa Number ? (actual,) : actual) "$label is non-finite"
    @assert isapprox(actual, expected; atol=tolerance, rtol=tolerance) "$label mismatch"
end

forward_gradient = ForwardDiff.gradient(objective, θ)
reverse_gradient = Zygote.gradient(objective, θ)[1]
probabilities = 1.0 ./ (1.0 .+ exp.(-logits(θ)))
expected_gradient = X' * (probabilities - y) / length(y) + λ * θ
check(forward_gradient, expected_gradient, "forward logistic gradient")
check(reverse_gradient, expected_gradient, "reverse logistic gradient")

jvp_logits = ForwardDiff.derivative(a -> logits(θ .+ a .* v), 0.0)
check(jvp_logits, X * v, "logit JVP"; tolerance=1e-12)

actual_hvp = Zygote.hessian(objective, θ) * v
weights = probabilities .* (1 .- probabilities)
expected_hvp = X' * (weights .* (X * v)) / length(y) + λ * v
check(actual_hvp, expected_hvp, "logistic Hessian-vector product")

h = 1e-5
directional_difference = (objective(θ .+ h .* v) - objective(θ .- h .* v)) / (2h)
check(dot(reverse_gradient, v), directional_difference, "directional finite difference")
gradient_difference = (
    ForwardDiff.gradient(objective, θ .+ h .* v) -
    ForwardDiff.gradient(objective, θ .- h .* v)
) / (2h)
check(actual_hvp, gradient_difference, "HVP finite difference")
println("AD gradient: ", reverse_gradient, "; HVP: ", actual_hvp)
