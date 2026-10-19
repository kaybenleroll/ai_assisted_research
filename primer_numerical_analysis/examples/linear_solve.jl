using LinearAlgebra

# LinearAlgebra is part of Julia's standard library.
A = [3.0 1.0; 1.0 2.0]
expected = [2.0, -1.0]
b = A * expected
solution = A \ b

# The system is well-conditioned; this tolerance allows double-precision
# rounding while remaining far below the scale of an incorrect solution.
@assert isapprox(solution, expected; rtol=1e-12, atol=1e-12)
@assert norm(A * solution - b, Inf) < 1e-12
