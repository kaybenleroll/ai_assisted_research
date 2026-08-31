#!/usr/bin/env Rscript
# Generate all figures for the numerical analysis primer.
# Run via: Rscript generate_plots.R  (inside the rocker/tidyverse container)

dir.create("figures", showWarnings = FALSE, recursive = TRUE)

FIGDPI <- 150
BLUE   <- "#2271B2"
ORANGE <- "#E69F00"
GREEN  <- "#009E73"
RED    <- "#D55E00"

# Vandermonde polynomial interpolation (degree n = length(x_nodes) - 1)
poly_interp <- function(x_nodes, y_nodes, x_eval) {
  n <- length(x_nodes) - 1
  V <- outer(x_nodes, 0:n, `^`)
  coefs <- solve(V, y_nodes)
  sapply(x_eval, function(xi) sum(coefs * xi^(0:n)))
}

cat("Generating figures...\n")

# --------------------------------------------------------------------------
# 1. Runge's phenomenon
# --------------------------------------------------------------------------
cat("  figures/runge_phenomenon.png\n")
local({
  f <- function(x) 1 / (1 + x^2)
  x_fine <- seq(-5, 5, length.out = 500)
  n <- 10

  x_unif <- seq(-5, 5, length.out = n + 1)
  y_unif  <- poly_interp(x_unif, f(x_unif), x_fine)

  k <- 0:n
  x_cheb <- -5 * cos(k * pi / n)
  y_cheb  <- poly_interp(x_cheb, f(x_cheb), x_fine)

  png("figures/runge_phenomenon.png", width = 800, height = 500, res = FIGDPI)
  par(mar = c(4, 4.2, 3, 1))
  plot(x_fine, f(x_fine), type = "l", lwd = 2.5, col = "black",
       ylim = c(-1.5, 2.0), xlab = expression(x), ylab = expression(f(x)),
       main = "Runge's Phenomenon: Uniform vs Chebyshev Nodes", cex.main = 1.1)
  lines(x_fine, y_unif, col = RED,  lwd = 1.8, lty = 2)
  lines(x_fine, y_cheb, col = BLUE, lwd = 1.8, lty = 4)
  points(x_unif, f(x_unif), col = RED,  pch = 19, cex = 0.9)
  points(x_cheb, f(x_cheb), col = BLUE, pch = 19, cex = 0.9)
  legend("topright", bty = "n", lty = c(1, 2, 4), lwd = c(2.5, 1.8, 1.8),
         col = c("black", RED, BLUE),
         legend = c(expression(f(x) == 1 / (1 + x^2)),
                    "Degree-10 (uniform nodes)",
                    "Degree-10 (Chebyshev nodes)"), cex = 0.88)
  dev.off()
})

# --------------------------------------------------------------------------
# 2. Finite-difference step-size vs error
# --------------------------------------------------------------------------
cat("  figures/finite_diff_stepsize.png\n")
local({
  f <- exp
  x0 <- 1.0
  true_deriv <- exp(1.0)
  h_vals <- 10^seq(-16, 0, length.out = 300)
  errors  <- abs((f(x0 + h_vals) - f(x0 - h_vals)) / (2 * h_vals) - true_deriv)
  errors[errors == 0] <- 1e-17

  eps_mach <- .Machine$double.eps
  h_opt    <- eps_mach^(1 / 3)

  png("figures/finite_diff_stepsize.png", width = 800, height = 500, res = FIGDPI)
  par(mar = c(4, 4.8, 3, 1))
  plot(h_vals, errors, type = "l", lwd = 2, col = BLUE, log = "xy",
       xlab = "Step size h",
       ylab = expression("Absolute error in " * f * "'(1)"),
       main = "Central Differences: Truncation vs Cancellation Error",
       cex.main = 1.1)
  abline(v = h_opt, col = RED, lty = 2, lwd = 1.8)
  legend("topleft", bty = "n", lty = c(1, 2), lwd = c(2, 1.8),
         col = c(BLUE, RED),
         legend = c("Absolute error",
                    bquote("Optimal" ~ h %~~% epsilon^{1/3} %~~% .(sprintf("%.1e", h_opt)))),
         cex = 0.88)
  text(5e-14, 0.03, "Cancellation\n(roundoff\ndominates)", col = RED,  cex = 0.78)
  text(0.1,   1e-13, "Truncation\n(discretisation\ndominates)", col = BLUE, cex = 0.78)
  dev.off()
})

# --------------------------------------------------------------------------
# 3. Stability regions: Forward Euler vs Backward Euler
# --------------------------------------------------------------------------
cat("  figures/stability_regions.png\n")
local({
  re_g <- seq(-3.5, 1.5, length.out = 400)
  im_g <- seq(-2.5, 2.5, length.out = 400)
  Z <- outer(re_g, im_g, function(r, i) complex(real = r, imaginary = i))

  fe_stable <- Mod(1 + Z) <= 1.0     # disk at -1, radius 1
  be_stable  <- Mod(Z - 1) >= 1.0    # exterior of disk at +1, radius 1

  # Encode: 0=neither, 1=FE only, 2=BE only, 3=both
  code_mat <- fe_stable * 1L + be_stable * 2L

  cols <- c("white",
            adjustcolor(BLUE,   alpha.f = 0.55),   # FE only
            adjustcolor(ORANGE, alpha.f = 0.40),   # BE only
            adjustcolor(GREEN,  alpha.f = 0.45))   # both

  theta <- seq(0, 2 * pi, length.out = 360)

  png("figures/stability_regions.png", width = 800, height = 650, res = FIGDPI)
  par(mar = c(4, 4.2, 3, 1))
  image(re_g, im_g, code_mat, col = cols,
        xlab = expression("Re(" * h * lambda * ")"),
        ylab = expression("Im(" * h * lambda * ")"),
        main = "Stability Regions: Forward Euler vs Backward Euler",
        cex.main = 1.1)
  # Boundary circles
  lines(-1 + cos(theta), sin(theta), col = BLUE,   lwd = 2)
  lines( 1 + cos(theta), sin(theta), col = ORANGE, lwd = 2)
  abline(h = 0, col = "grey30", lwd = 0.8)
  abline(v = 0, col = "grey30", lwd = 0.8)
  legend("topleft", bty = "n",
         fill   = c(adjustcolor(BLUE, 0.6), adjustcolor(ORANGE, 0.5)),
         border = c(BLUE, ORANGE),
         legend = c("Forward Euler (shaded = stable)",
                    "Backward Euler (shaded = stable)"), cex = 0.88)
  dev.off()
})

# --------------------------------------------------------------------------
# 4. Eigenvalue convergence (power iteration)
# --------------------------------------------------------------------------
cat("  figures/eigenvalue_convergence.png\n")
local({
  set.seed(42)
  n <- 20
  A_raw <- matrix(rnorm(n * n), n, n)
  A <- A_raw %*% t(A_raw)   # symmetric positive definite

  v <- rnorm(n)
  v <- v / sqrt(sum(v^2))

  max_iters <- 60
  residuals  <- numeric(max_iters)
  for (i in seq_len(max_iters)) {
    w   <- as.numeric(A %*% v)
    lam <- sum(v * w)
    residuals[i] <- sqrt(sum((w - lam * v)^2))
    v <- w / sqrt(sum(w^2))
  }

  png("figures/eigenvalue_convergence.png", width = 800, height = 500, res = FIGDPI)
  par(mar = c(4, 5.5, 3, 1))
  plot(seq_len(max_iters), residuals, type = "l", lwd = 2, col = BLUE, log = "y",
       xlab = "Iteration",
       ylab = expression(group("||", bold(A)*bold(v)[k] - hat(lambda)[k]*bold(v)[k], "||")[2]),
       main = "Power Iteration Convergence (20×20 Symmetric Matrix)",
       cex.main = 1.1)
  points(seq(1, max_iters, by = 5), residuals[seq(1, max_iters, by = 5)],
         col = BLUE, pch = 19, cex = 0.8)
  dev.off()
})

# --------------------------------------------------------------------------
# 5. Optimisation landscape: convex vs nonconvex
# --------------------------------------------------------------------------
cat("  figures/optimisation_landscape.png\n")
local({
  n_g  <- 200
  xv   <- seq(-3, 3, length.out = n_g)
  yv   <- seq(-3, 3, length.out = n_g)
  X    <- outer(xv, rep(1, n_g))
  Y    <- outer(rep(1, n_g), yv)

  Z_conv    <- X^2 + Y^2
  Z_nonconv <- sin(2*X) * cos(2*Y) + 0.1*(X^2 + Y^2)

  png("figures/optimisation_landscape.png", width = 1100, height = 520, res = FIGDPI)
  par(mfrow = c(1, 2), mar = c(4, 4, 3, 0.5))

  # Convex
  image(xv, yv, Z_conv, col = hcl.colors(20, "Blues", rev = TRUE),
        xlab = "x", ylab = "y",
        main = expression("Convex: " * f(x,y) == x^2 + y^2))
  contour(xv, yv, Z_conv, nlevels = 15, add = TRUE, col = "white", lwd = 0.5)
  points(0, 0, pch = 8, cex = 2, col = RED, lwd = 2)
  legend("topright", bty = "n", pch = 8, col = RED, pt.cex = 1.5,
         legend = "Global minimum", cex = 0.85)

  # Nonconvex
  image(xv, yv, Z_nonconv, col = hcl.colors(25, "Oranges", rev = TRUE),
        xlab = "x", ylab = "y",
        main = "Nonconvex: sin(2x)cos(2y) + 0.1(x²+y²)")
  contour(xv, yv, Z_nonconv, nlevels = 20, add = TRUE, col = "white", lwd = 0.5)
  local_min_x <- c(-pi/2, pi/2)
  local_min_y <- c(0, 0)
  points(local_min_x, local_min_y, pch = 8, cex = 2, col = RED, lwd = 2)
  legend("topright", bty = "n", pch = 8, col = RED, pt.cex = 1.5,
         legend = "Local minima", cex = 0.85)

  dev.off()
  par(mfrow = c(1, 1))
})

# --------------------------------------------------------------------------
# 6. L-curve (Tikhonov regularisation on Hilbert matrix)
# --------------------------------------------------------------------------
cat("  figures/lcurve.png\n")
local({
  hilbert_mat <- function(n) {
    i <- seq_len(n)
    1 / outer(i, i, function(a, b) a + b - 1)
  }

  n <- 10
  A <- hilbert_mat(n)
  set.seed(7)
  x_true <- rnorm(n)
  b <- A %*% x_true

  mu_vals <- 10^seq(-6, 2, length.out = 80)
  norms_x <- numeric(length(mu_vals))
  norms_r <- numeric(length(mu_vals))

  AtA <- t(A) %*% A
  Atb <- t(A) %*% b
  In  <- diag(n)

  for (j in seq_along(mu_vals)) {
    x_mu      <- solve(AtA + mu_vals[j] * In, Atb)
    norms_x[j] <- sqrt(sum(x_mu^2))
    norms_r[j] <- sqrt(sum((A %*% x_mu - b)^2))
  }

  # Corner: maximum discrete curvature in log-log space
  lx  <- log(norms_x)
  lr  <- log(norms_r)
  dx  <- diff(lx);  dy  <- diff(lr)
  ddx <- diff(dx);  ddy <- diff(dy)
  m   <- length(ddx)
  curvature <- abs(dx[1:m] * ddy - dy[1:m] * ddx) /
               (dx[1:m]^2 + dy[1:m]^2 + 1e-12)^1.5
  corner_idx <- which.max(curvature) + 1L

  png("figures/lcurve.png", width = 700, height = 600, res = FIGDPI)
  par(mar = c(5, 5.5, 3.5, 1))
  plot(norms_x, norms_r, type = "l", lwd = 2, col = BLUE, log = "xy",
       xlab = expression(log * " " * group("||", bold(x)[mu], "||")),
       ylab = expression(log * " " * group("||", bold(A)*bold(x)[mu] - bold(b), "||")),
       main = "L-Curve: Regularisation Parameter Selection\n(Hilbert matrix, Tikhonov)",
       cex.main = 1.0)
  points(norms_x[corner_idx], norms_r[corner_idx],
         pch = 8, cex = 2.5, col = RED, lwd = 2.5)
  legend("topleft", bty = "n", pch = 8, col = RED, pt.cex = 1.5,
         legend = sprintf("Corner (μ ≈ %.2e)", mu_vals[corner_idx]),
         cex = 0.88)
  dev.off()
})

cat("Done.\n")
