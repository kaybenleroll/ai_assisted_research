# Base R solve() computes the solution without additional packages.
matrix <- matrix(c(3, 1, 1, 2), nrow = 2, byrow = TRUE)
expected <- c(2, -1)
rhs <- drop(matrix %*% expected)
solution <- drop(solve(matrix, rhs))

# The system is well-conditioned; this tolerance allows double-precision
# rounding while remaining far below the scale of an incorrect solution.
stopifnot(max(abs(solution - expected)) < 1e-12)
stopifnot(max(abs(drop(matrix %*% solution) - rhs)) < 1e-12)
