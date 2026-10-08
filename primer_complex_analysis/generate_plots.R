#!/usr/bin/env Rscript
# Reproducible figures for the complex-analysis primer.
# Run inside the rocker/tidyverse container through Justfile: plots.

suppressPackageStartupMessages({
  library(ggplot2)
  library(dplyr)
  library(tidyr)
})

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

theme_primer <- function(base_size = 12) {
  theme_minimal(base_size = base_size) +
    theme(
      plot.title = element_text(face = "bold", size = rel(1.12), margin = margin(b = 8)),
      plot.subtitle = element_text(color = "#4d4d4d", margin = margin(b = 10)),
      axis.title = element_text(face = "bold"),
      panel.grid.minor = element_blank(),
      legend.position = "top",
      legend.title = element_blank(),
      plot.margin = margin(12, 16, 10, 12)
    )
}

save_gg <- function(plot, name, width = 8.5, height = 5.6) {
  ggsave(file.path("figures", name), plot, width = width, height = height,
         dpi = FIGDPI, bg = "white")
}

# 1. The complex plane: modulus, argument, and polar geometry.
save_png("complex_plane_geometry.png")
par(mar = c(4.2, 4.2, 3, 1), pty = "s")
plot(NA, xlim = c(-2.2, 2.2), ylim = c(-2.2, 2.2), asp = 1,
     xlab = "Re z", ylab = "Im z", main = "The complex plane is a geometric object")
abline(h = 0, v = 0, col = GRID)
for (r in c(0.5, 1, 1.5, 2)) circle(r = r, col = adjustcolor(BLUE, .45), lty = 2)
for (th in seq(0, 2 * pi - pi / 6, by = pi / 6))
  lines(c(0, 2.05 * cos(th)), c(0, 2.05 * sin(th)), col = adjustcolor(GRID, .8))
z <- c(1.35, .9)
lines(c(0, z[1]), c(0, z[2]), col = RED, lwd = 2)
points(z[1], z[2], pch = 19, col = RED)
text(z[1] + .08, z[2] + .1, "z", col = RED, adj = 0)
text(1.52, -.12, "|z| = r", col = BLUE)
text(.72, .27, "arg(z)", col = RED)
dev.off()

# 2. Multiplication by a complex number: rotation plus scaling.
save_png("complex_multiplication.png")
par(mfrow = c(1, 2), mar = c(4.2, 4.2, 3, 1))
z0 <- 1.2 + .5i
multiplier <- 2 * exp(1i * pi / 3)
z1 <- multiplier * z0
for (which in 1:2) {
  plot(NA, xlim = c(-2.2, 2.2), ylim = c(-2.2, 2.2), asp = 1,
       xlab = "real", ylab = "imaginary",
       main = if (which == 1) "Before: z" else "After: (2 exp(i pi/3)) z")
  abline(h = 0, v = 0, col = GRID)
  a <- if (which == 1) z0 else z1
  circle(r = Mod(a), col = adjustcolor(BLUE, .5), lty = 2)
  arrow_line(c(0, Re(a)), c(0, Im(a)), BLUE, 2)
  points(Re(a), Im(a), pch = 19, col = BLUE)
  text(Re(a) + .08, Im(a) + .1, if (which == 1) "z" else "wz", col = BLUE, adj = 0)
  if (which == 1) {
    arc <- seq(0, Arg(multiplier), length.out = 100)
    lines(.55 * cos(arc), .55 * sin(arc), col = ORANGE, lwd = 2)
    text(.55, .38, "60 deg", col = ORANGE, adj = 0)
  } else text(-2.05, -1.95, "|wz| = 2|z|", col = BLUE, adj = 0)
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

# 4. Domain colouring: phase is hue and magnitude is brightness.
grid <- expand.grid(x = seq(-1.55, 1.55, length.out = 360),
                    y = seq(-1.55, 1.55, length.out = 360))
grid$z <- with(grid, x + 1i * y)
grid$w <- grid$z^2
grid$phase <- (Arg(grid$w) %% (2 * pi)) / (2 * pi)
grid$brightness <- scales::rescale(log1p(Mod(grid$w)), to = c(.28, 1))
grid$colour <- hsv(grid$phase, .82, grid$brightness)
grid$colour[abs(grid$z) < .025] <- "#3d3d3d"
domain_colouring <- ggplot(grid, aes(x, y, fill = colour)) +
  geom_raster() +
  scale_fill_identity() +
  coord_fixed(xlim = c(-1.55, 1.55), ylim = c(-1.55, 1.55), expand = FALSE) +
  labs(title = "Domain colouring makes phase winding visible",
       subtitle = "For f(z) = z², one turn around the origin becomes two turns in phase") +
  theme_void(base_size = 12) +
  theme(plot.title = element_text(face = "bold", size = 14, margin = margin(b = 5)),
        plot.subtitle = element_text(color = "#4d4d4d", size = 10, margin = margin(b = 8)),
        plot.margin = margin(12, 16, 10, 16))
save_gg(domain_colouring, "domain_colouring_z2.png", 8, 6)

# 5. Directional difference quotients reveal complex differentiability.
theta <- seq(0, 2 * pi, length.out = 500)
z0 <- .8 + .4i
quotients <- expand.grid(theta = theta, rho = c(.8, .4, .15),
                         function_name = c("f(z) = z²", "f(z) = conjugate(z)")) |>
  mutate(h = rho * exp(1i * theta),
         q = ifelse(function_name == "f(z) = z²",
                    (z0 + h)^2 - z0^2,
                    Conj(z0 + h) - Conj(z0)) / h,
         radius = paste0("ρ = ", rho))
quotient_plot <- ggplot(quotients, aes(Re(q), Im(q), colour = radius)) +
  geom_path(linewidth = .8, alpha = .9) +
  geom_point(data = tibble(x = Re(2 * z0), y = Im(2 * z0)),
             aes(x, y), inherit.aes = FALSE, colour = "#2166ac", size = 2) +
  facet_wrap(~ function_name, nrow = 1) +
  coord_fixed() +
  scale_colour_manual(values = c("ρ = 0.8" = "#f28e2b", "ρ = 0.4" = "#1b9e77", "ρ = 0.15" = "#2166ac")) +
  labs(title = "The complex difference quotient must forget direction",
       subtitle = "For z² the curves collapse to 2z₀; for conjugate(z) they remain a unit circle",
       x = "Re Qρ", y = "Im Qρ") +
  theme_primer() + theme(legend.position = "top", strip.text = element_text(face = "bold"))
save_gg(quotient_plot, "difference_quotients.png", 9, 5.4)

# 6. A directed contour and its winding numbers.
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

# 6. Cauchy's formula: the interior value is controlled by a boundary circle.
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

# 7. Laurent annuli and the singularities at radii 1 and 2.
save_png("laurent_annuli.png")
par(mar = c(4.2, 4.2, 3, 1), pty = "s")
plot(NA, xlim = c(-2.7, 2.7), ylim = c(-2.7, 2.7), asp = 1,
     xlab = "Re z", ylab = "Im z", main = "Laurent expansions stop at the nearest singularity")
abline(h = 0, v = 0, col = GRID)
circle(r = 1, col = ORANGE, lty = 2, lwd = 2)
circle(r = 2, col = BLUE, lty = 2, lwd = 2)
points(c(1, 2), c(0, 0), pch = 4, col = RED, lwd = 2, cex = 1.5)
text(1.08, .2, "pole 1", col = RED, adj = 0)
text(2.05, -.22, "pole 2", col = RED, adj = 0)
text(0, .42, "|z| < 1", col = ORANGE, font = 2)
text(0, 1.45, "1 < |z| < 2", col = BLUE, font = 2)
text(-2.3, -2.25, "|z| > 2", col = "#555555", font = 2, adj = 0)
dev.off()

# 8. Semicircle contour selected by exponential decay.
save_png("semicircle_contour.png")
par(mar = c(4.2, 4.2, 3, 1))
plot(NA, xlim = c(-2.3, 2.3), ylim = c(-.35, 2.3), asp = 1,
     xlab = "Re z", ylab = "Im z", main = "The sign of the phase selects the half-plane")
th <- seq(pi, 0, length.out = 200)
lines(2 * cos(th), 2 * sin(th), col = BLUE, lwd = 2)
lines(seq(-2, 2, length.out = 200), rep(0, 200), col = BLUE, lwd = 2)
arrows(-1.5, 0, -1.1, 0, col = BLUE, length = .1)
arrows(1.1, 0, 1.5, 0, col = BLUE, length = .1)
arrows(2 * cos(.8), 2 * sin(.8), 2 * cos(.68), 2 * sin(.68), col = BLUE, length = .1)
points(0, 1, pch = 4, col = RED, lwd = 2, cex = 1.5)
text(.15, 1, "pole", col = RED, adj = 0)
text(-2.1, 2.15, "upper semicircle", col = BLUE, adj = 0)
dev.off()

# 9. Keyhole contour around a branch cut.
save_png("keyhole_contour.png")
par(mar = c(4.2, 4.2, 3, 1))
plot(NA, xlim = c(-2.4, 2.4), ylim = c(-2.3, 2.3), asp = 1,
     xlab = "Re z", ylab = "Im z", main = "A keyhole contour has two banks of the cut")
eps <- .35; R <- 2
lines(seq(eps, R, length.out = 200), rep(.12, 200), col = BLUE, lwd = 2)
lines(seq(R, eps, length.out = 200), rep(-.12, 200), col = BLUE, lwd = 2)
th_outer <- seq(0, 2 * pi, length.out = 250)
th_inner <- seq(2 * pi, 0, length.out = 120)
lines(R * cos(th_outer), R * sin(th_outer), col = BLUE, lwd = 2)
lines(eps * cos(th_inner), eps * sin(th_inner), col = BLUE, lwd = 2)
arrows(1.1, .12, 1.45, .12, col = ORANGE, length = .1)
arrows(1.45, -.12, 1.1, -.12, col = ORANGE, length = .1)
arrows(R * cos(.7), R * sin(.7), R * cos(.82), R * sin(.82), col = ORANGE, length = .1)
points(-.8, 0, pch = 4, col = RED, lwd = 2, cex = 1.4)
text(-1.8, .35, "pole -1", col = RED, adj = 0)
text(1.15, 1.25, "outer arc", col = BLUE)
text(.55, -.55, "inner arc", col = BLUE)
text(.85, .34, "upper bank", col = ORANGE)
text(.85, -.34, "lower bank", col = ORANGE)
dev.off()

# 10. Argument principle: a boundary image winds around the origin.
save_png("argument_principle_winding.png")
par(mfrow = c(1, 2), mar = c(4.2, 4.2, 3, 1))
th <- seq(0, 2 * pi, length.out = 600)
z <- 1.5 * exp(1i * th)
fz <- (z - 1)^2 / (z * (z - 2))
plot(Re(z), Im(z), type = "l", asp = 1, col = BLUE, lwd = 2,
     xlab = "Re z", ylab = "Im z", main = "Contour |z| = 3/2")
abline(h = 0, v = 0, col = GRID)
for (j in c(80, 280, 480)) arrow_line(c(Re(z[j]), Re(z[j + 4])),
                                         c(Im(z[j]), Im(z[j + 4])), BLUE, 1.5)
points(0, 0, pch = 4, col = RED, lwd = 2)
points(1, 0, pch = 1, col = RED, lwd = 2)
plot(Re(fz), Im(fz), type = "l", asp = 1, col = RED, lwd = 2,
     xlab = "Re f(z)", ylab = "Im f(z)", main = "Image winds once")
abline(h = 0, v = 0, col = GRID)
for (j in c(80, 280, 480)) arrow_line(c(Re(fz[j]), Re(fz[j + 4])),
                                         c(Im(fz[j]), Im(fz[j + 4])), RED, 1.5)
points(0, 0, pch = 4, col = "black", lwd = 2)
dev.off()

# 11. A Mobius map from the upper half-plane to the unit disk.
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

# 12. Wedge straightening by a power map.
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

# 13. The Poisson kernel concentrates near the boundary point.
x <- seq(-pi, pi, length.out = 1000)
poisson <- expand.grid(theta = x, r = c(.25, .60, .90)) |>
  mutate(P = (1 - r^2) / (1 - 2 * r * cos(theta) + r^2),
         radius = sprintf("r = %.2f", r))
poisson_plot <- ggplot(poisson, aes(theta, P, colour = radius)) +
  geom_line(linewidth = 1.05) +
  geom_vline(xintercept = 0, linetype = "dashed", colour = "#777777") +
  scale_colour_manual(values = c("#2166ac", "#f28e2b", "#d73027")) +
  scale_x_continuous(breaks = c(-pi, -pi/2, 0, pi/2, pi),
                     labels = c("−π", "−π/2", "0", "π/2", "π")) +
  labs(title = "Poisson kernels concentrate at the boundary point",
       subtitle = "As r approaches 1, the kernel becomes a sharper averaging window",
       x = "boundary angle θ", y = "Pᵣ(θ)") +
  theme_primer()
save_gg(poisson_plot, "poisson_kernel.png")

# 14. A complex potential and its streamlines.
save_png("complex_potential_flow.png")
par(mar = c(4.2, 4.2, 3, 1))
xx <- seq(-2.2, 2.2, length.out = 350)
yy <- seq(-2.2, 2.2, length.out = 350)
zz <- outer(xx, yy, FUN = function(x, y) x + 1i * y)
F <- zz + .7 / zz
F[Mod(zz) <= sqrt(.7)] <- NA_complex_
lev <- seq(-3, 3, length.out = 13)
plot(NA, xlim = c(-2.2, 2.2), ylim = c(-2.2, 2.2), asp = 1,
     xlab = "Re z", ylab = "Im z", main = "Complex potential flow")
contour(xx, yy, Im(F), levels = lev, drawlabels = FALSE, add = TRUE, col = BLUE)
contour(xx, yy, Re(F), levels = lev, drawlabels = FALSE, add = TRUE, col = ORANGE, lty = 2)
circle(r = sqrt(.7), col = RED, lty = 2)
points(c(-sqrt(.7), sqrt(.7)), c(0, 0), pch = 19, col = RED)
legend("topleft", legend = c("Im F: streamlines", "Re F: equipotentials"),
       col = c(BLUE, ORANGE), lty = c(1, 2), bty = "n")
dev.off()

# 15. Periodic trapezoidal convergence for a contour integral.
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
quadrature <- tibble(
  N = rep(N, 2),
  error = c(err_inside, err_outside),
  case = c(rep("pole inside: exact value", length(err_inside)),
           rep("pole outside: zero", length(err_outside)))
)
quadrature_plot <- ggplot(quadrature, aes(N, error, colour = case, shape = case)) +
  geom_line(linewidth = .9) + geom_point(size = 2.3) +
  scale_x_continuous(trans = "log2", breaks = N, labels = N) + scale_y_log10() +
  scale_colour_manual(values = c("#2166ac", "#d73027")) +
  labs(title = "Contour quadrature: check the contour before trusting the limit",
       subtitle = "Both valid contours converge rapidly, but they compute different residue-theorem values",
       x = "number of nodes N", y = "absolute error") +
  theme_primer() + theme(legend.position = "top")
save_gg(quadrature_plot, "contour_quadrature_convergence.png")

# 16. Laplace's method: separate the landscape from the concentration.
x <- seq(-2.5, 2.5, length.out = 800)
f <- x^2 / 2 + .08 * x^4
laplace <- expand.grid(x = x, lambda = c(1, 4, 12)) |>
  mutate(f = x^2 / 2 + .08 * x^4,
         weight = exp(-lambda * f),
         lambda_label = paste0("λ = ", lambda))
landscape <- tibble(x = x, value = f, panel = "landscape f(x)",
                    lambda_label = "landscape")
weights <- laplace |>
  transmute(x, value = weight, panel = "normalised weight exp(−λf(x))",
            lambda_label)
laplace_data <- bind_rows(landscape, weights)
laplace_plot <- ggplot(laplace_data, aes(x, value, colour = lambda_label)) +
  geom_line(linewidth = 1.05) +
  facet_grid(. ~ panel, scales = "free_y") +
  scale_colour_manual(values = c("landscape" = "#2166ac", "λ = 1" = "#f28e2b", "λ = 4" = "#1b9e77", "λ = 12" = "#d73027")) +
  labs(title = "Laplace's method is local near the minimiser",
       subtitle = "The left panel shows the landscape; the right panel shows how increasing λ concentrates the weight",
       x = "x", y = NULL) +
  theme_primer() + theme(legend.position = "top", strip.text = element_text(face = "bold"))
save_gg(laplace_plot, "laplace_method.png", 9, 5.8)

cat("Generated 16 complex-analysis figures in figures/.\n")
