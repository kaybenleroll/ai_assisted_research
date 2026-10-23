#!/usr/bin/env Rscript
# Generate the reproducible figures used by the fluid-mechanics primer.
# Run via: just --justfile primer_fluid_mechanics/Justfile plots

dir.create("figures", showWarnings = FALSE, recursive = TRUE)

FIGDPI <- 150
BLUE <- "#2271B2"
ORANGE <- "#E69F00"
GREEN <- "#009E73"
RED <- "#D55E00"
PURPLE <- "#7B3294"

save_plot <- function(path, width = 800, height = 520, expr) {
  png(path, width = width, height = height, res = FIGDPI)
  on.exit(dev.off(), add = TRUE)
  par(mar = c(4.3, 4.5, 3.1, 1.2), mgp = c(2.5, 0.8, 0))
  force(expr)
}

cat("Generating fluid-mechanics figures...\n")

# 1. Couette and Poiseuille profiles.
cat("  figures/velocity_profiles.png\n")
y <- seq(0, 1, length.out = 300)
couette <- y
poiseuille <- 4 * y * (1 - y)
combined <- 0.35 * couette + 0.65 * poiseuille
save_plot("figures/velocity_profiles.png", expr = {
  plot(couette, y, type = "l", lwd = 2.5, col = BLUE,
       xlim = c(0, 1.15), ylim = c(0, 1),
       xlab = expression(u / U), ylab = expression(y / h),
       main = "Parallel-Plate Velocity Profiles")
  lines(poiseuille, y, lwd = 2.5, col = ORANGE, lty = 2)
  lines(combined, y, lwd = 2.2, col = GREEN, lty = 3)
  legend("bottomright", bty = "n", lwd = c(2.5, 2.5, 2.2), lty = c(1, 2, 3),
         col = c(BLUE, ORANGE, GREEN),
         legend = c("Couette: moving wall", "Poiseuille: pressure-driven",
                    "Combined profile"), cex = 0.88)
})

# 2. Hydrostatic pressure and Bernoulli baseline.
cat("  figures/hydrostatic_and_bernoulli.png\n")
depth <- seq(0, 5, length.out = 200)
gauge <- 1000 * 9.81 * depth / 1000
speed <- seq(0, 4, length.out = 200)
dynamic <- 0.5 * 1000 * (1.5^2 - speed^2) / 1000
save_plot("figures/hydrostatic_and_bernoulli.png", expr = {
  par(mfrow = c(1, 2), mar = c(4.3, 3.5, 3.1, 0.8))
  plot(depth, gauge, type = "l", lwd = 2.5, col = BLUE,
       xlab = "Depth (m)", ylab = "Pressure (kPa)",
       main = "Hydrostatic Column")
  plot(speed, dynamic, type = "l", lwd = 2.5, col = ORANGE,
       xlab = "Speed (m/s)", ylab = "p2 - p1 (kPa)",
       main = "Ideal Contraction")
  abline(h = 0, col = "grey40", lty = 3)
})

# 3. Boundary-layer profiles and integral thicknesses.
cat("  figures/boundary_layer_profiles.png\n")
eta <- seq(0, 4, length.out = 300)
laminar <- 1 - exp(-eta) * (1 + eta)
turbulent <- pmin(1, (eta / 1.6)^(1 / 7))
save_plot("figures/boundary_layer_profiles.png", expr = {
  plot(laminar, eta, type = "l", lwd = 2.5, col = BLUE,
       xlim = c(0, 1.05), ylim = c(0, 4),
       xlab = expression(u / U[e]), ylab = expression(y / delta),
       main = "Idealised Boundary-Layer Profiles")
  lines(turbulent, eta, lwd = 2.5, col = RED, lty = 2)
  abline(v = 0.99, col = "grey40", lty = 3)
  legend("bottomright", bty = "n", lwd = c(2.5, 2.5), lty = c(1, 2),
         col = c(BLUE, RED), legend = c("Smooth laminar-like profile",
         "Power-law turbulent-like profile"), cex = 0.83)
  text(0.72, 3.5, "99% reference", col = "grey30", cex = 0.78)
})

# 4. Isentropic pressure and density ratios.
cat("  figures/isentropic_ratios.png\n")
ma <- seq(0, 2, length.out = 300)
gamma <- 1.4
pressure_ratio <- (1 + (gamma - 1) * ma^2 / 2)^(-gamma / (gamma - 1))
density_ratio <- (1 + (gamma - 1) * ma^2 / 2)^(-1 / (gamma - 1))
save_plot("figures/isentropic_ratios.png", expr = {
  plot(ma, pressure_ratio, type = "l", lwd = 2.5, col = BLUE,
       ylim = c(0.2, 1.05), xlab = "Mach number", ylab = "Static / stagnation ratio",
       main = "Ideal-Gas Isentropic Ratios (gamma = 1.4)")
  lines(ma, density_ratio, lwd = 2.5, col = ORANGE, lty = 2)
  abline(v = 1, col = "grey40", lty = 3)
  legend("topright", bty = "n", lwd = c(2.5, 2.5), lty = c(1, 2),
         col = c(BLUE, ORANGE), legend = c("p / p0", "rho / rho0"), cex = 0.9)
})

# 5. Conservative advection: exact translation and diffusive upwind result.
cat("  figures/periodic_advection.png\n")
n <- 80
x <- (seq_len(n) - 0.5) / n
u <- 1
dt <- 0.8 / n
steps <- 40
q0 <- 0.5 + 0.5 * sin(2 * pi * x)
q <- q0
for (step in seq_len(steps)) q <- q - u * dt / (1 / n) * (q - c(q[n], q[-n]))
t_final <- steps * dt
exact <- 0.5 + 0.5 * sin(2 * pi * ((x - u * t_final) %% 1))
save_plot("figures/periodic_advection.png", expr = {
  plot(x, q0, type = "l", lwd = 2.2, col = "grey35",
       ylim = c(0, 1), xlab = "Periodic position x / L", ylab = "Scalar q",
       main = "Conservative Upwind Advection")
  lines(x, exact, lwd = 2.5, col = BLUE, lty = 2)
  lines(x, q, lwd = 2.2, col = ORANGE)
  legend("topright", bty = "n", lwd = c(2.2, 2.5, 2.2), lty = c(1, 2, 1),
         col = c("grey35", BLUE, ORANGE),
         legend = c("Initial", "Exact translation", "Upwind result"), cex = 0.87)
})

# 6. Grid refinement and observed first-order convergence.
cat("  figures/advection_convergence.png\n")
advection_run <- function(n, final_time = 0.5) {
  length <- 1.0
  velocity <- 0.4
  cfl_limit <- 0.4
  dx <- length / n
  steps <- ceiling(final_time / (cfl_limit * dx / velocity))
  dt <- final_time / steps
  cfl <- velocity * dt / dx
  x <- ((seq_len(n) - 0.5) * dx)
  factor <- sin(pi / n) / (pi / n)
  field <- 1.0 + 0.2 * factor * sin(2 * pi * x)
  for (step in seq_len(steps)) {
    outgoing <- velocity * field
    incoming <- c(outgoing[n], outgoing[-n])
    field <- field - dt / dx * (outgoing - incoming)
  }
  exact <- 1.0 + 0.2 * factor * sin(2 * pi * ((x - velocity * final_time) %% length))
  c(error = sqrt(mean((field - exact)^2)), cfl = cfl,
    mass_change = sum(field) * dx - sum(1.0 + 0.2 * factor * sin(2 * pi * x)) * dx)
}
grids <- c(32, 64, 128, 256)
results <- t(vapply(grids, advection_run, numeric(3)))
errors <- results[, "error"]
save_plot("figures/advection_convergence.png", expr = {
  plot(grids, errors, type = "b", log = "xy", pch = 19, lwd = 2,
       col = PURPLE, xlab = "Number of cells N", ylab = "L2 error",
       main = "Refinement Evidence for First-Order Advection")
  lines(grids, errors[1] * grids[1] / grids, col = RED, lty = 2, lwd = 1.8)
  legend("topright", bty = "n", lwd = c(2, 1.8), lty = c(1, 2),
         col = c(PURPLE, RED), legend = c("Measured error", "Reference slope -1"),
         cex = 0.88)
})

# 7. Control-volume flux accounting schematic.
cat("  figures/control_volume_fluxes.png\n")
save_plot("figures/control_volume_fluxes.png", width = 800, height = 500, expr = {
  plot.new()
  plot.window(xlim = c(0, 10), ylim = c(0, 6), asp = 1)
  rect(3, 1.2, 7, 4.8, border = BLUE, lwd = 3)
  arrows(0.8, 3, 3, 3, length = 0.12, lwd = 2, col = ORANGE)
  arrows(7, 3.8, 9.2, 3.8, length = 0.12, lwd = 2, col = GREEN)
  arrows(5, 5.8, 5, 4.8, length = 0.12, lwd = 2, col = RED)
  arrows(5, 1.2, 5, 0.2, length = 0.12, lwd = 2, col = PURPLE)
  text(5, 3, "control\nvolume", cex = 1.2)
  text(1.6, 3.35, "inlet flux", col = ORANGE, cex = 0.9)
  text(8.1, 4.15, "outlet flux", col = GREEN, cex = 0.9)
  text(5.45, 5.4, "surface force", col = RED, cex = 0.9)
  text(5.7, 0.55, "body/source term", col = PURPLE, cex = 0.9)
  title("Control-Volume Flux Accounting")
})

# 8. Kinematics: pathline, streamline, and streakline schematic.
cat("  figures/kinematics_paths.png\n")
save_plot("figures/kinematics_paths.png", width = 800, height = 520, expr = {
  plot(NA, xlim = c(0, 10), ylim = c(0, 7), axes = FALSE, xlab = "", ylab = "",
       main = "Three Ways to Describe Motion")
  axis(1, at = c(0, 5, 10), labels = c("upstream", "source", "downstream"))
  axis(2, at = c(0, 3.5, 7), labels = c("", "y", ""), las = 1)
  abline(h = 3.5, col = "grey85")
  curve(2.5 + 0.12 * (x - 5)^2, from = 0.4, to = 5, add = TRUE, col = BLUE, lwd = 2.5)
  curve(2.5 + 0.12 * (x - 5)^2, from = 5, to = 9.6, add = TRUE, col = BLUE, lwd = 2.5, lty = 2)
  lines(c(1, 2.5, 4, 5.5, 7.4, 9), c(1.0, 1.4, 2.0, 2.9, 4.3, 5.6), col = ORANGE, lwd = 2.5)
  lines(c(5, 5.4, 6.1, 7.1, 8.2, 9.3), c(1.0, 1.2, 1.7, 2.6, 3.9, 5.2), col = GREEN, lwd = 2.5)
  points(5, 1.0, pch = 19, col = RED, cex = 1.1)
  legend("topleft", bty = "n", lwd = c(2.5, 2.5, 2.5), lty = c(1, 1, 1),
         col = c(BLUE, ORANGE, GREEN),
         legend = c("streamline (instantaneous field)", "pathline (one particle)",
                    "streakline (continuous source)"), cex = 0.79)
  text(5.2, 0.55, "source location", col = RED, cex = 0.8)
})

# 9. Finite-volume cells and shared face fluxes.
cat("  figures/finite_volume_faces.png\n")
save_plot("figures/finite_volume_faces.png", width = 800, height = 500, expr = {
  plot.new()
  plot.window(xlim = c(0, 10), ylim = c(0, 5), asp = 1)
  for (x0 in c(1, 3, 5, 7)) rect(x0, 1.5, x0 + 2, 3.5, border = "grey35", lwd = 1.5)
  for (x0 in c(1, 3, 5, 7)) text(x0 + 1, 2.5, paste0("cell ", (x0 - 1) / 2 + 1), cex = 0.85)
  for (x0 in c(3, 5, 7)) arrows(x0 - 0.7, 4.35, x0 + 0.7, 4.35, length = 0.1, col = RED, lwd = 2)
  text(5, 4.7, "one shared face flux", col = RED, cex = 0.95)
  arrows(0.25, 2.5, 1, 2.5, length = 0.1, col = ORANGE, lwd = 2)
  arrows(9, 2.5, 9.75, 2.5, length = 0.1, col = GREEN, lwd = 2)
  text(0.65, 2.95, "in", col = ORANGE, cex = 0.9)
  text(9.35, 2.95, "out", col = GREEN, cex = 0.9)
  title("Finite-Volume Face Fluxes")
})

cat("Figures complete.\n")
