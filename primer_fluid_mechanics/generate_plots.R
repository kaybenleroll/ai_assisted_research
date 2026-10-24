#!/usr/bin/env Rscript
# Generate the reproducible figures used by the fluid-mechanics primer.
# Run via: just -f primer_fluid_mechanics/Justfile plots

library(ggplot2)

dir.create("figures", showWarnings = FALSE, recursive = TRUE)

FIGDPI <- 150
BLUE <- "#2271B2"
ORANGE <- "#B86800"
GREEN <- "#00845F"
RED <- "#C34B18"
PURPLE <- "#7B3294"
INK <- "#25313A"

plot_theme <- function() {
  theme_classic(base_family = "DejaVu Sans", base_size = 12) +
    theme(
      plot.title = element_text(size = 15, face = "bold", colour = INK,
                                margin = margin(b = 13)),
      axis.title = element_text(size = 12, colour = INK),
      axis.text = element_text(size = 10, colour = INK),
      axis.line = element_line(colour = INK, linewidth = 0.45),
      axis.ticks = element_line(colour = INK, linewidth = 0.45),
      legend.position = "bottom",
      legend.title = element_blank(),
      legend.text = element_text(size = 10),
      legend.key.width = grid::unit(1.5, "cm"),
      plot.margin = margin(22, 27, 22, 25)
    )
}

save_plot <- function(path, plot, width = 8.4, height = 5.5) {
  ggsave(path, plot = plot, width = width, height = height,
         units = "in", dpi = FIGDPI, bg = "white")
}

cat("Generating fluid-mechanics figures...\n")

# 1. Couette and Poiseuille profiles.
cat("  figures/velocity_profiles.png\n")
y <- seq(0, 1, length.out = 300)
couette <- y
poiseuille <- 4 * y * (1 - y)
combined <- 0.35 * couette + 0.65 * poiseuille
velocity_data <- data.frame(
  velocity = c(couette, poiseuille, combined),
  height = rep(y, 3),
  profile = factor(rep(c("Couette: moving wall", "Poiseuille: pressure-driven",
                         "Combined profile"), each = length(y)),
                   levels = c("Couette: moving wall", "Poiseuille: pressure-driven",
                              "Combined profile"))
)
velocity_plot <- ggplot(velocity_data, aes(velocity, height, colour = profile,
                                          linetype = profile)) +
  geom_path(linewidth = 1.05) +
  scale_colour_manual(values = c(BLUE, ORANGE, GREEN)) +
  scale_linetype_manual(values = c("solid", "dashed", "dotdash")) +
  scale_x_continuous(limits = c(0, 1.15), breaks = seq(0, 1, 0.25)) +
  scale_y_continuous(limits = c(0, 1), breaks = seq(0, 1, 0.25)) +
  labs(title = "Parallel-Plate Velocity Profiles", x = "u / U", y = "y / h") +
  guides(colour = guide_legend(nrow = 1)) + plot_theme()
save_plot("figures/velocity_profiles.png", velocity_plot, width = 9.8)

# 2. Hydrostatic pressure and Bernoulli baseline.
cat("  figures/hydrostatic_and_bernoulli.png\n")
depth <- seq(0, 5, length.out = 200)
gauge <- 1000 * 9.81 * depth / 1000
speed <- seq(0, 4, length.out = 200)
dynamic <- 0.5 * 1000 * (1.5^2 - speed^2) / 1000
hydro_plot <- ggplot(data.frame(depth, gauge), aes(depth, gauge)) +
  geom_line(colour = BLUE, linewidth = 1.1) +
  scale_x_continuous(breaks = 0:5) +
  labs(title = "Hydrostatic Column", x = "Depth (m)", y = "Pressure (kPa)") +
  plot_theme() + theme(plot.title = element_text(size = 13, face = "bold",
                                              margin = margin(b = 13)))
bernoulli_plot <- ggplot(data.frame(speed, dynamic), aes(speed, dynamic)) +
  geom_hline(yintercept = 0, colour = "grey55", linetype = "dotted") +
  geom_line(colour = ORANGE, linewidth = 1.1) +
  scale_x_continuous(breaks = 0:4) +
  labs(title = "Ideal Contraction", x = "Speed (m/s)", y = "p2 - p1 (kPa)") +
  plot_theme() + theme(plot.title = element_text(size = 13, face = "bold",
                                              margin = margin(b = 13)))
# Measure both panels on a PNG device, where the installed font is available.
# Base grid is part of R, so this layout needs no extra package.
metrics_device <- tempfile(fileext = ".png")
grDevices::png(metrics_device, width = 1680, height = 810, res = FIGDPI)
two_panels <- grid::grobTree(
  grid::grobTree(ggplotGrob(hydro_plot),
                 vp = grid::viewport(x = 0.25, width = 0.5, height = 1)),
  grid::grobTree(ggplotGrob(bernoulli_plot),
                 vp = grid::viewport(x = 0.75, width = 0.5, height = 1))
)
invisible(grDevices::dev.off())
unlink(metrics_device)
save_plot("figures/hydrostatic_and_bernoulli.png", two_panels,
          width = 11.2, height = 5.4)

# 3. Boundary-layer profiles and integral thicknesses.
cat("  figures/boundary_layer_profiles.png\n")
eta <- seq(0, 4, length.out = 300)
laminar <- 1 - exp(-eta) * (1 + eta)
turbulent <- pmin(1, (eta / 1.6)^(1 / 7))
boundary_data <- data.frame(
  velocity = c(laminar, turbulent), height = rep(eta, 2),
  profile = factor(rep(c("Smooth laminar-like profile",
                         "Power-law turbulent-like profile"), each = length(eta)),
                   levels = c("Smooth laminar-like profile",
                              "Power-law turbulent-like profile"))
)
boundary_plot <- ggplot(boundary_data, aes(velocity, height, colour = profile,
                                          linetype = profile)) +
  geom_vline(xintercept = 0.99, colour = "grey55", linetype = "dotted") +
  geom_line(linewidth = 1.05) +
  annotate("text", x = 0.78, y = 3.65, label = "u/Ue = 0.99",
           colour = "grey35", family = "DejaVu Sans", size = 3.5) +
  scale_colour_manual(values = c(BLUE, RED)) +
  scale_linetype_manual(values = c("solid", "dashed")) +
  scale_x_continuous(limits = c(0, 1.05), breaks = seq(0, 1, 0.25)) +
  scale_y_continuous(limits = c(0, 4), breaks = 0:4) +
  labs(title = "Idealised Boundary-Layer Profiles",
       subtitle = "delta_ref is a shared illustrative scale, not a 99% thickness",
       x = "u / Ue", y = "eta = y / delta_ref") +
  guides(colour = guide_legend(nrow = 1)) + plot_theme()
save_plot("figures/boundary_layer_profiles.png", boundary_plot, width = 9.6)

# 4. Isentropic pressure and density ratios.
cat("  figures/isentropic_ratios.png\n")
ma <- seq(0, 2, length.out = 300)
gamma <- 1.4
pressure_ratio <- (1 + (gamma - 1) * ma^2 / 2)^(-gamma / (gamma - 1))
density_ratio <- (1 + (gamma - 1) * ma^2 / 2)^(-1 / (gamma - 1))
ratio_data <- data.frame(
  mach = rep(ma, 2), ratio = c(pressure_ratio, density_ratio),
  quantity = factor(rep(c("p / p0", "rho / rho0"), each = length(ma)),
                    levels = c("p / p0", "rho / rho0"))
)
ratio_plot <- ggplot(ratio_data, aes(mach, ratio, colour = quantity,
                                    linetype = quantity)) +
  geom_vline(xintercept = 1, colour = "grey55", linetype = "dotted") +
  geom_line(linewidth = 1.05) +
  scale_colour_manual(values = c(BLUE, ORANGE)) +
  scale_linetype_manual(values = c("solid", "dashed")) +
  scale_x_continuous(breaks = seq(0, 2, 0.5)) +
  scale_y_continuous(breaks = seq(0.2, 1, 0.2)) +
  coord_cartesian(ylim = c(0.1, 1.05)) +
  labs(title = "Ideal-Gas Isentropic Ratios (gamma = 1.4)",
       x = "Mach number", y = "Static / stagnation ratio") + plot_theme()
save_plot("figures/isentropic_ratios.png", ratio_plot)

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
advection_data <- data.frame(
  position = rep(x, 3), scalar = c(q0, exact, q),
  series = factor(rep(c("Initial", "Exact translation", "Upwind result"),
                      each = length(x)),
                  levels = c("Initial", "Exact translation", "Upwind result"))
)
advection_plot <- ggplot(advection_data, aes(position, scalar, colour = series,
                                             linetype = series)) +
  geom_line(linewidth = 1.05) +
  scale_colour_manual(values = c("#555555", BLUE, ORANGE)) +
  scale_linetype_manual(values = c("solid", "dashed", "solid")) +
  scale_x_continuous(limits = c(0, 1), breaks = seq(0, 1, 0.2)) +
  scale_y_continuous(limits = c(0, 1), breaks = seq(0, 1, 0.25)) +
  labs(title = "Conservative Upwind Advection", x = "Periodic position x / L",
       y = "Scalar q") +
  guides(colour = guide_legend(nrow = 1)) + plot_theme()
save_plot("figures/periodic_advection.png", advection_plot)

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
convergence_data <- data.frame(
  cells = rep(grids, 2),
  error = c(errors, errors[1] * grids[1] / grids),
  series = factor(rep(c("Measured error", "Reference slope -1"), each = length(grids)),
                  levels = c("Measured error", "Reference slope -1"))
)
convergence_plot <- ggplot(convergence_data,
                           aes(cells, error, colour = series, linetype = series)) +
  geom_line(linewidth = 0.95) +
  geom_point(data = subset(convergence_data, series == "Measured error"),
             size = 2.7, show.legend = FALSE) +
  scale_colour_manual(values = c(PURPLE, RED)) +
  scale_linetype_manual(values = c("solid", "dashed")) +
  scale_x_log10(breaks = grids, labels = as.character(grids)) +
  scale_y_log10() +
  labs(title = "Refinement Evidence for First-Order Advection",
       x = "Number of cells N", y = "L2 error") + plot_theme()
save_plot("figures/advection_convergence.png", convergence_plot, width = 9)

# 7. Control-volume flux accounting schematic.
cat("  figures/control_volume_fluxes.png\n")
arrow_head <- grid::arrow(length = grid::unit(0.24, "cm"), type = "closed")
schematic_theme <- function() {
  theme_void(base_family = "DejaVu Sans", base_size = 12) +
    theme(plot.title = element_text(size = 15, face = "bold", colour = INK,
                                    hjust = 0.5, margin = margin(b = 14)),
          plot.margin = margin(24, 30, 24, 30))
}
control_plot <- ggplot() +
  annotate("rect", xmin = 3, xmax = 7, ymin = 1.2, ymax = 4.8,
           fill = "#F4F8FA", colour = BLUE, linewidth = 1.2) +
  annotate("segment", x = 0.8, xend = 3, y = 3, yend = 3,
           colour = ORANGE, linewidth = 1.1, arrow = arrow_head) +
  annotate("segment", x = 7, xend = 9.2, y = 3.8, yend = 3.8,
           colour = GREEN, linewidth = 1.1, arrow = arrow_head) +
  annotate("segment", x = 5, xend = 5, y = 5.8, yend = 4.8,
           colour = RED, linewidth = 1.1, arrow = arrow_head) +
  annotate("segment", x = 5, xend = 5, y = 1.2, yend = 0.2,
           colour = PURPLE, linewidth = 1.1, arrow = arrow_head) +
  annotate("text", x = 5, y = 3, label = "control\nvolume",
           family = "DejaVu Sans", colour = INK, size = 5) +
  annotate("text", x = 1.7, y = 3.48, label = "inlet flux",
           family = "DejaVu Sans", colour = ORANGE, size = 4) +
  annotate("text", x = 8.1, y = 4.3, label = "outlet flux",
           family = "DejaVu Sans", colour = GREEN, size = 4) +
  annotate("text", x = 5.9, y = 5.48, label = "surface force",
           family = "DejaVu Sans", colour = RED, size = 4) +
  annotate("text", x = 6.25, y = 0.55, label = "body/source term",
           family = "DejaVu Sans", colour = PURPLE, size = 4) +
  coord_fixed(xlim = c(0, 10), ylim = c(0, 6), expand = FALSE) +
  labs(title = "Control-Volume Flux Accounting") + schematic_theme()
save_plot("figures/control_volume_fluxes.png", control_plot, width = 9.2, height = 5.9)

# 8. Kinematics: pathline, streamline, and streakline schematic.
cat("  figures/kinematics_paths.png\n")
stream_x <- seq(0.4, 9.6, length.out = 250)
stream_y <- 2.5 + 0.12 * (stream_x - 5)^2
kinematics_plot <- ggplot() +
  geom_hline(yintercept = 3.5, colour = "grey88", linewidth = 0.5) +
  geom_line(data = data.frame(x = stream_x[stream_x <= 5],
                              y = stream_y[stream_x <= 5]),
            aes(x, y), colour = BLUE, linewidth = 1.1) +
  geom_line(data = data.frame(x = stream_x[stream_x >= 5],
                              y = stream_y[stream_x >= 5]),
            aes(x, y), colour = BLUE, linewidth = 1.1, linetype = "dashed") +
  geom_line(data = data.frame(x = c(1, 2.5, 4, 5.5, 7.4, 9),
                              y = c(1.0, 1.4, 2.0, 2.9, 4.3, 5.6)),
            aes(x, y), colour = ORANGE, linewidth = 1.1) +
  geom_line(data = data.frame(x = c(5, 5.4, 6.1, 7.1, 8.2, 9.3),
                              y = c(1.0, 1.2, 1.7, 2.6, 3.9, 5.2)),
            aes(x, y), colour = GREEN, linewidth = 1.1) +
  annotate("point", x = 5, y = 1, colour = RED, size = 3.5) +
  annotate("text", x = 2.45, y = 6.5, label = "streamline (instantaneous field)",
           colour = BLUE, family = "DejaVu Sans", size = 3.8) +
  annotate("text", x = 7.6, y = 6.25, label = "pathline (one particle)",
           colour = ORANGE, family = "DejaVu Sans", size = 3.8) +
  annotate("text", x = 7.65, y = 5.6, label = "streakline (continuous source)",
           colour = GREEN, family = "DejaVu Sans", size = 3.8) +
  annotate("text", x = 5.15, y = 0.55, label = "source location",
           colour = RED, family = "DejaVu Sans", hjust = 0, size = 3.7) +
  scale_x_continuous(breaks = c(0, 5, 10),
                     labels = c("upstream", "source", "downstream")) +
  scale_y_continuous(breaks = 3.5, labels = "y") +
  coord_cartesian(xlim = c(0, 10), ylim = c(0, 7), expand = FALSE) +
  labs(title = "Three Ways to Describe Motion", x = NULL, y = NULL) +
  plot_theme() + theme(plot.title = element_text(hjust = 0.5, size = 15,
                                                  face = "bold", margin = margin(b = 13)))
save_plot("figures/kinematics_paths.png", kinematics_plot, width = 9.2, height = 6)

# 9. Finite-volume cells and shared face fluxes.
cat("  figures/finite_volume_faces.png\n")
cells <- data.frame(xmin = c(1, 3, 5, 7), xmax = c(3, 5, 7, 9),
                    ymin = 1.5, ymax = 3.5, label = paste("cell", 1:4),
                    x = c(2, 4, 6, 8), y = 2.5)
faces <- data.frame(x = c(2.3, 4.3, 6.3), xend = c(3.7, 5.7, 7.7),
                    y = 4.15, yend = 4.15)
faces_plot <- ggplot() +
  geom_rect(data = cells, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax),
            fill = "#F4F8FA", colour = "#555555", linewidth = 0.7) +
  geom_text(data = cells, aes(x, y, label = label), family = "DejaVu Sans",
            colour = INK, size = 4.3) +
  geom_segment(data = faces, aes(x = x, xend = xend, y = y, yend = yend),
               colour = RED, linewidth = 1.05, arrow = arrow_head) +
  annotate("text", x = 5, y = 4.68, label = "one shared face flux",
           colour = RED, family = "DejaVu Sans", size = 4.3) +
  annotate("segment", x = 0.25, xend = 1, y = 2.5, yend = 2.5,
           colour = ORANGE, linewidth = 1.05, arrow = arrow_head) +
  annotate("segment", x = 9, xend = 9.75, y = 2.5, yend = 2.5,
           colour = GREEN, linewidth = 1.05, arrow = arrow_head) +
  annotate("text", x = 0.65, y = 3, label = "in",
           colour = ORANGE, family = "DejaVu Sans", size = 4) +
  annotate("text", x = 9.35, y = 3, label = "out",
           colour = GREEN, family = "DejaVu Sans", size = 4) +
  coord_fixed(xlim = c(0, 10), ylim = c(0, 5), expand = FALSE) +
  labs(title = "Finite-Volume Face Fluxes") + schematic_theme()
save_plot("figures/finite_volume_faces.png", faces_plot, width = 9.2, height = 5.6)

cat("Figures complete.\n")
