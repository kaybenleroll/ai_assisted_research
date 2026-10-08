#!/usr/bin/env Rscript
# Reproducible figures for the complex-analysis primer.
# Run inside the rocker/tidyverse container through Justfile: plots.

dir.create("figures", showWarnings = FALSE, recursive = TRUE)

FIGDPI <- 150
BLUE <- "#1f77b4"
ORANGE <- "#d95f02"
GREEN <- "#1b9e77"
RED <- "#d62728"
PURPLE <- "#7570b3"
GRID <- "#bdbdbd"

arrow_line <- function(x, y, col = "black", lwd = 1.5, len = 0.08) {
  arrows(x[1], y[1], x[2], y[2], col = col, lwd = lwd,
         length = len, angle = 20)
}

circle <- function(cx = 0, cy = 0, r = 1, col = "black", lwd = 1, lty = 1) {
  th <- seq(0, 2 * pi, length.out = 400)
  lines(cx + r * cos(th), cy + r * sin(th), col = col, lwd = lwd, lty = lty)
}

save_png <- function(name, width = 900, height = 600) {
  png(file.path("figures", name), width = width, height = height, res = FIGDPI)
}

# 1. The complex plane: modulus, argument, and polar geometry.
save_png("complex_plane_geometry.png")
par(mar = c(4.2, 4.2, 3, 1))
plot(NA, xlim = c(-2.2, 2.2), ylim = c(-2.2, 2.2), asp = 1,
     xlab = "Re z", ylab = "Im z", main = "The complex plane is a geometric object")
abline(h = 0, v = 0, col = GRID)
for (r in c(0.5, 1, 1.5, 2)) circle(r = r, col = adjustcolor(BLUE, .45), lty = 2)
for (th in seq(0, 2 * pi - pi / 6, by = pi / 6))
  lines(c(0, 2.05 * cos(th)), c(0, 2.05 * sin(th)), col = adjustcolor(GRID, .8))
z <- c(1.35, .9)
lines(c(0, z[1]), c(0, z[2]), col = RED, lwd = 2)
points(z[1], z[2], pch = 19, col = RED)
text(z[1] + .1, z[2] + .1, "z = r exp(i theta)", col = RED, adj = 0)
text(1.52, -.12, "|z| = r", col = BLUE)
text(.72, .27, "arg(z)", col = RED)
dev.off()

# 2. Multiplication by a complex number: rotation plus scaling.
save_png("complex_multiplication.png")
par(mfrow = c(1, 2), mar = c(4.2, 4.2, 3, 1))
for (which in 1:2) {
  plot(NA, xlim = c(-2.2, 2.2), ylim = c(-2.2, 2.2), asp = 1,
       xlab = "real", ylab = "imaginary",
       main = if (which == 1) "Before multiplication" else "After multiplication")
  abline(h = 0, v = 0, col = GRID)
  a <- if (which == 1) c(1.2, .5) else c(.7, 1.2)
  b <- if (which == 1) c(1.1, -.2) else c(1.1, .8)
  circle(r = sqrt(sum(a^2)), col = adjustcolor(BLUE, .5), lty = 2)
  arrow_line(c(0, a[1]), c(0, a[2]), BLUE, 2)
  arrow_line(c(0, b[1]), c(0, b[2]), ORANGE, 2)
  points(a[1], a[2], pch = 19, col = BLUE)
  points(b[1], b[2], pch = 19, col = ORANGE)
  text(a[1] + .08, a[2] + .1, if (which == 1) "z" else "z w", col = BLUE, adj = 0)
  text(b[1] + .08, b[2] + .1, if (which == 1) "w" else "reference", col = ORANGE, adj = 0)
}
dev.off()

# 3. A conformal grid under z -> z^2.
save_png("conformal_grid_square.png")
par(mfrow = c(1, 2), mar = c(4.2, 4.2, 3, 1))
t <- seq(0, 1, length.out = 300)
for (which in 1:2) {
  plot(NA, xlim = c(-1.1, 1.1), ylim = c(-1.1, 1.1), asp = 1,
       xlab = "Re", ylab = "Im",
       main = if (which == 1) "Input grid" else "Image under z -> z^2")
  for (r in seq(.15, 1, length.out = 8)) {
    z <- r * exp(1i * 2 * pi * t)
    if (which == 2) z <- z^2
    lines(Re(z), Im(z), col = adjustcolor(BLUE, .7))
  }
  for (th in seq(0, 2 * pi - pi / 12, length.out = 24)) {
    z <- t * exp(1i * th)
    if (which == 2) z <- z^2
    lines(Re(z), Im(z), col = adjustcolor(ORANGE, .65))
  }
  abline(h = 0, v = 0, col = adjustcolor(GRID, .7))
}
dev.off()

# 4. A directed contour and its winding numbers.
save_png("contour_winding.png")
par(mar = c(4.2, 4.2, 3, 1))
plot(NA, xlim = c(-2.2, 2.2), ylim = c(-1.8, 1.8), asp = 1,
     xlab = "Re z", ylab = "Im z", main = "Winding is a directed count")
abline(h = 0, v = 0, col = GRID)
circle(r = 1.35, col = BLUE, lwd = 2)
th <- seq(0, 2 * pi, length.out = 100)
for (a in c(.25, 2.1, 4.1)) {
  p <- c(1.35 * cos(a), 1.35 * sin(a))
  q <- c(1.35 * cos(a + .18), 1.35 * sin(a + .18))
  arrow_line(c(p[1], q[1]), c(p[2], q[2]), BLUE, 1.8)
}
points(c(-.45, .5, 1.75), c(.25, -.35, .35), pch = 4, col = RED, lwd = 2, cex = 1.4)
text(c(-.45, .5, 1.75), c(.25, -.35, .35) + .16,
     c("inside: +1", "inside: +1", "outside: 0"), col = RED)
text(-1.9, 1.45, "counterclockwise", col = BLUE, adj = 0)
dev.off()

# 5. Cauchy's formula: the interior value is controlled by a boundary circle.
save_png("cauchy_integral_formula.png")
par(mar = c(4.2, 4.2, 3, 1))
plot(NA, xlim = c(-1.8, 1.8), ylim = c(-1.6, 1.6), asp = 1,
     xlab = "Re z", ylab = "Im z", main = "Cauchy's formula reads the boundary")
circle(r = 1.15, col = BLUE, lwd = 2)
circle(cx = .35, cy = .25, r = .14, col = RED, lwd = 2)
points(.35, .25, pch = 19, col = RED)
for (a in seq(0, 2 * pi - pi / 3, by = pi / 3)) {
  x <- c(1.15 * cos(a), .35)
  y <- c(1.15 * sin(a), .25)
  arrows(x[1], y[1], x[2], y[2], col = adjustcolor(ORANGE, .65), length = .08)
}
text(.35, .48, "a", col = RED)
text(0, -1.42, "f(a) = (1 / 2 pi i) integral_C f(z)/(z-a) dz", col = BLUE)
dev.off()

# 6. Laurent annuli and the singularity at the centre.
save_png("laurent_annuli.png")
par(mfrow = c(1, 3), mar = c(3.2, 3.2, 2.8, .5))
limits <- list(c(0, 1), c(1, 2), c(2, 3))
titles <- c("0 < |z| < 1", "1 < |z| < 2", "|z| > 2")
for (j in 1:3) {
  plot(NA, xlim = c(-3, 3), ylim = c(-3, 3), asp = 1, axes = FALSE,
       xlab = "", ylab = "", main = titles[j])
  axis(1, labels = FALSE); axis(2, labels = FALSE)
  circle(r = limits[[j]][1], col = if (j == 1) RED else GRID, lty = 2)
  circle(r = limits[[j]][2], col = if (j < 3) BLUE else GRID, lty = 2)
  points(0, 0, pch = 4, col = RED, lwd = 2, cex = 1.4)
  if (j == 3) points(2.5, 0, pch = 19, col = BLUE)
  text(0, -2.55, "series converges here", cex = .8)
}
dev.off()

# 7. Semicircle contour selected by exponential decay.
save_png("semicircle_contour.png")
par(mar = c(4.2, 4.2, 3, 1))
plot(NA, xlim = c(-2.3, 2.3), ylim = c(-.35, 2.3), asp = 1,
     xlab = "Re z", ylab = "Im z", main = "The sign of the phase selects the half-plane")
th <- seq(pi, 0, length.out = 200)
lines(2 * cos(th), 2 * sin(th), col = BLUE, lwd = 2)
lines(seq(-2, 2, length.out = 200), rep(0, 200), col = BLUE, lwd = 2)
arrows(-1.5, 0, -1.1, 0, col = BLUE, length = .1)
arrows(1.5, 0, 1.1, 0, col = BLUE, length = .1)
arrows(2 * cos(2.1), 2 * sin(2.1), 2 * cos(2.0), 2 * sin(2.0), col = BLUE, length = .1)
points(0, 1, pch = 4, col = RED, lwd = 2, cex = 1.5)
text(.15, 1, "pole", col = RED, adj = 0)
text(-2.1, 2.15, "upper semicircle", col = BLUE, adj = 0)
dev.off()

# 8. Keyhole contour around a branch cut.
save_png("keyhole_contour.png")
par(mar = c(4.2, 4.2, 3, 1))
plot(NA, xlim = c(-2.4, 2.4), ylim = c(-2.3, 2.3), asp = 1,
     xlab = "Re z", ylab = "Im z", main = "A keyhole contour has two banks of the cut")
lines(seq(-2, -.35, length.out = 200), rep(.12, 200), col = BLUE, lwd = 2)
lines(seq(-2, -.35, length.out = 200), rep(-.12, 200), col = BLUE, lwd = 2)
th <- seq(pi, 0, length.out = 100)
lines(.35 * cos(th), .35 * sin(th), col = BLUE, lwd = 2)
th2 <- seq(0, -pi, length.out = 100)
lines(2 * cos(th2), 2 * sin(th2), col = BLUE, lwd = 2)
arrows(-1.6, .12, -1.3, .12, col = ORANGE, length = .1)
arrows(-1.6, -.12, -1.9, -.12, col = ORANGE, length = .1)
points(-.8, 0, pch = 4, col = RED, lwd = 2, cex = 1.4)
text(-.65, .2, "branch cut", col = RED, adj = 0)
text(1.15, 1.25, "outer arc", col = BLUE)
text(.42, -.45, "inner arc", col = BLUE)
dev.off()

# 9. Argument principle: a boundary image winds around the origin.
save_png("argument_principle_winding.png")
par(mfrow = c(1, 2), mar = c(4.2, 4.2, 3, 1))
th <- seq(0, 2 * pi, length.out = 600)
z <- exp(1i * th)
fz <- z^3 - .35 * z
plot(Re(z), Im(z), type = "l", asp = 1, col = BLUE, lwd = 2,
     xlab = "Re z", ylab = "Im z", main = "Contour and image winding")
abline(h = 0, v = 0, col = GRID)
plot(Re(fz), Im(fz), type = "l", asp = 1, col = RED, lwd = 2,
     xlab = "Re f(z)", ylab = "Im f(z)", main = "Its image winds around zero")
abline(h = 0, v = 0, col = GRID)
points(0, 0, pch = 4, col = "black", lwd = 2)
dev.off()

# 10. A Mobius map from the upper half-plane to the unit disk.
save_png("mobius_half_plane_disk.png")
par(mfrow = c(1, 2), mar = c(4.2, 4.2, 3, 1))
xx <- seq(-3, 3, length.out = 300)
yy <- seq(.15, 3, length.out = 10)
for (which in 1:2) {
  plot(NA, xlim = if (which == 1) c(-3.2, 3.2) else c(-1.2, 1.2),
       ylim = if (which == 1) c(-.2, 3.2) else c(-1.2, 1.2), asp = 1,
       xlab = "real", ylab = "imaginary",
       main = if (which == 1) "Upper half-plane" else "Image under (z-i)/(z+i)")
  if (which == 1) {
    for (y in yy) lines(xx, rep(y, length(xx)), col = adjustcolor(BLUE, .45))
    for (x in seq(-3, 3, by = .5)) lines(rep(x, 300), seq(.15, 3, length.out = 300), col = adjustcolor(ORANGE, .45))
  } else {
    for (y in yy) { w <- (xx + 1i * y - 1i) / (xx + 1i * y + 1i); lines(Re(w), Im(w), col = adjustcolor(BLUE, .45)) }
    for (x in seq(-3, 3, by = .5)) { zz <- x + 1i * seq(.15, 3, length.out = 300); w <- (zz - 1i) / (zz + 1i); lines(Re(w), Im(w), col = adjustcolor(ORANGE, .45)) }
    circle(r = 1, col = "black", lwd = 1.5)
  }
}
dev.off()

# 11. Wedge straightening by a power map.
save_png("wedge_map.png")
par(mfrow = c(1, 2), mar = c(4.2, 4.2, 3, 1))
alpha <- pi / 3
for (which in 1:2) {
  plot(NA, xlim = c(0, 1.15), ylim = c(0, 1.15), asp = 1,
       xlab = "real", ylab = "imaginary",
       main = if (which == 1) "Wedge of angle pi/3" else "Image under z -> z^(pi/alpha)")
  for (r in seq(.15, 1, length.out = 8)) {
    zz <- r * exp(1i * seq(0, alpha, length.out = 300))
    if (which == 2) zz <- zz^(pi / alpha)
    lines(Re(zz), Im(zz), col = adjustcolor(BLUE, .65))
  }
  for (th in seq(0, alpha, length.out = 8)) {
    zz <- seq(0, 1, length.out = 300) * exp(1i * th)
    if (which == 2) zz <- zz^(pi / alpha)
    lines(Re(zz), Im(zz), col = adjustcolor(ORANGE, .65))
  }
}
dev.off()

# 12. The Poisson kernel concentrates near the boundary point.
save_png("poisson_kernel.png")
par(mar = c(4.2, 4.2, 3, 1))
x <- seq(-pi, pi, length.out = 1000)
for (r in c(.25, .6, .9)) {
  P <- (1 - r^2) / (1 - 2 * r * cos(x) + r^2)
  if (r == .25) plot(x, P, type = "l", lwd = 2, col = BLUE, ylim = c(0, 20),
                      xlab = "boundary angle theta", ylab = "P_r(theta)",
                      main = "Poisson kernels become concentrated")
  else lines(x, P, lwd = 2, col = if (r == .6) ORANGE else RED)
}
abline(v = 0, col = GRID, lty = 2)
legend("topright", legend = c("r = 0.25", "r = 0.60", "r = 0.90"),
       col = c(BLUE, ORANGE, RED), lwd = 2, bty = "n")
dev.off()

# 13. A complex potential and its streamlines.
save_png("complex_potential_flow.png")
par(mar = c(4.2, 4.2, 3, 1))
xx <- seq(-2.2, 2.2, length.out = 350)
yy <- seq(-2.2, 2.2, length.out = 350)
zz <- outer(xx, 1i * yy, )
F <- zz + .7 / zz
lev <- seq(-3, 3, length.out = 13)
plot(NA, xlim = c(-2.2, 2.2), ylim = c(-2.2, 2.2), asp = 1,
     xlab = "Re z", ylab = "Im z", main = "Complex potential flow")
contour(xx, yy, Im(F), levels = lev, drawlabels = FALSE, add = TRUE, col = BLUE)
contour(xx, yy, Re(F), levels = lev, drawlabels = FALSE, add = TRUE, col = ORANGE, lty = 2)
circle(r = sqrt(.7), col = RED, lty = 2)
legend("topleft", legend = c("Im F: streamlines", "Re F: equipotentials"),
       col = c(BLUE, ORANGE), lty = c(1, 2), bty = "n")
dev.off()

# 14. Periodic trapezoidal convergence for a contour integral.
save_png("contour_quadrature_convergence.png")
par(mar = c(4.2, 4.8, 3, 1))
N <- 2^(3:10)
err_inside <- sapply(N, function(n) {
  th <- 2 * pi * (0:(n - 1)) / n
  z <- 2 * exp(1i * th)
  val <- sum(exp(z) / (z - 1) * 1i * 2 * exp(1i * th)) * 2 * pi / n
  abs(val - 2 * pi * 1i * exp(1))
})
err_outside <- sapply(N, function(n) {
  th <- 2 * pi * (0:(n - 1)) / n
  z <- .5 * exp(1i * th)
  val <- sum(exp(z) / (z - 1) * 1i * .5 * exp(1i * th)) * 2 * pi / n
  abs(val)
})
plot(N, err_inside, log = "xy", type = "b", pch = 19, col = BLUE,
     xlab = "number of nodes N", ylab = "absolute error",
     main = "Contour quadrature: singularity location matters",
     ylim = range(c(err_inside, err_outside)))
lines(N, err_outside, type = "b", pch = 17, col = RED)
legend("bottomleft", legend = c("pole inside: exact value", "pole outside: zero"),
       col = c(BLUE, RED), pch = c(19, 17), lty = 1, bty = "n")
dev.off()

# 15. Laplace's method: the local quadratic region dominates.
save_png("laplace_method.png")
par(mar = c(4.2, 4.2, 3, 1))
x <- seq(-2.5, 2.5, length.out = 800)
f <- x^2 / 2 + .08 * x^4
plot(x, f, type = "l", lwd = 2, col = BLUE, xlab = "x", ylab = "f(x)",
     main = "Laplace's method focuses on the minimum")
for (lambda in c(1, 4, 12)) {
  y <- exp(-lambda * f)
  lines(x, y, lwd = 2, col = if (lambda == 1) ORANGE else if (lambda == 4) GREEN else RED, lty = 2)
}
abline(v = 0, col = GRID, lty = 2)
legend("topright", legend = c("f(x)", "exp(-f)", "exp(-4f)", "exp(-12f)"),
       col = c(BLUE, ORANGE, GREEN, RED), lty = c(1, 2, 2, 2), lwd = 2, bty = "n")
dev.off()

cat("Generated 15 complex-analysis figures in figures/.\n")
