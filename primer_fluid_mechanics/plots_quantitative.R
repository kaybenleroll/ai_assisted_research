#!/usr/bin/env Rscript
# Reproducible quantitative illustrations. Run from primer_fluid_mechanics/.
# Uses only base R, ggplot2, and grid in the pinned Rocker figure image.

library(ggplot2)

dir.create("figures", showWarnings = FALSE)
dpi <- 150
blue <- "#2271B2"
orange <- "#B86800"
green <- "#00845F"
red <- "#C34B18"
ink <- "#25313A"

figure_theme <- function() {
  theme_classic(base_family = "DejaVu Sans", base_size = 12) +
    theme(plot.title = element_text(size = 15, face = "bold", colour = ink),
          plot.subtitle = element_text(size = 10.5, colour = ink,
                                       margin = margin(b = 9)),
          axis.title = element_text(colour = ink),
          axis.text = element_text(colour = ink),
          legend.position = "bottom", legend.title = element_blank(),
          legend.text = element_text(size = 10),
          plot.margin = margin(17, 23, 17, 20))
}

save_figure <- function(name, plot, width, height) {
  ggsave(file.path("figures", name), plot, width = width, height = height,
         units = "in", dpi = dpi, bg = "white")
}

stack_panels <- function(plots, heights, width, height) {
  stopifnot(length(plots) == length(heights))
  # Build text metrics on the same PNG device family used for the final plot.
  metrics_file <- tempfile(fileext = ".png")
  grDevices::png(metrics_file, width = width, height = height,
                 units = "in", res = dpi)
  grobs <- lapply(plots, ggplotGrob)
  invisible(grDevices::dev.off())
  unlink(metrics_file)
  heights <- heights / sum(heights)
  starts <- 1 - cumsum(heights)
  grid::grobTree(children = do.call(grid::gList, lapply(seq_along(plots), function(i) {
    grid::grobTree(grobs[[i]],
                   vp = grid::viewport(y = starts[i] + heights[i] / 2,
                                       height = heights[i], width = 1))
  })))
}

# 1. The field and paths use the primer's T(x,t) = 300 + 2x + 0.5t K,
# x in metres, t in seconds, and particle velocity u = 3 m/s.
# D T / D t = 0.5 + 3(2) = 6.5 K/s.
field <- expand.grid(x = seq(0, 3, length.out = 121),
                     t = seq(0, 0.8, length.out = 81))
field$temperature <- 300 + 2 * field$x + 0.5 * field$t
paths <- data.frame(t = seq(0, 0.8, length.out = 161))
paths$x <- 0.2 + 3 * paths$t
arrowhead <- grid::arrow(length = grid::unit(0.18, "cm"), type = "closed")
material_plot <- ggplot(field, aes(x, t)) +
  geom_raster(aes(fill = temperature), interpolate = TRUE) +
  geom_contour(aes(z = temperature), breaks = seq(301, 306, 1),
               colour = "#617784", linewidth = 0.35, alpha = 0.7) +
  geom_vline(xintercept = 1.2, colour = orange, linewidth = 1.15,
             linetype = "dashed") +
  geom_path(data = paths, aes(x, t), inherit.aes = FALSE,
            colour = blue, linewidth = 1.4) +
  annotate("segment", x = 1.2, xend = 1.2, y = 0.38, yend = 0.54,
           colour = orange, linewidth = 1.8, arrow = arrowhead) +
  annotate("segment", x = 1.35, xend = 1.83, y = 0.28, yend = 0.28,
           colour = blue, linewidth = 1.8, arrow = arrowhead) +
  annotate("label", x = 0.62, y = 0.58,
           label = "Fixed probe\nlocal: +0.5 K/s", colour = orange,
           fill = "white", linewidth = 0, size = 3.7) +
  annotate("label", x = 2.25, y = 0.20,
           label = "Moving particle\nadvective: +6 K/s", colour = blue,
           fill = "white", linewidth = 0, size = 3.7) +
  scale_fill_gradient(low = "#F3F8FB", high = "#5B9BC8", name = "T (K)") +
  scale_x_continuous(breaks = 0:3, expand = c(0, 0)) +
  scale_y_continuous(breaks = seq(0, 0.8, 0.2), expand = c(0, 0)) +
  coord_cartesian(xlim = c(0, 3), ylim = c(0, 0.8), expand = FALSE) +
  labs(title = "Material Derivative in an x–t Field",
       subtitle = "T = 300 + 2x + 0.5t K; u = 3 m/s; total along particle = 6.5 K/s",
       x = "Position x (m)", y = "Time t (s)") +
  figure_theme() + theme(legend.position = "right")
save_figure("material_derivative_field.png", material_plot, 10.2, 6.1)

# 2. Quasi-one-dimensional ideal-gas area/Mach branches. The prescribed
# internal shock is one illustrative back-pressure-compatible solution.
gamma <- 1.4
area_mach <- function(m) {
  (1 / m) * ((2 / (gamma + 1)) *
    (1 + (gamma - 1) * m^2 / 2))^((gamma + 1) / (2 * (gamma - 1)))
}
mach_from_area <- function(ratio, branch) {
  if (abs(ratio - 1) < 1e-12) return(1)
  interval <- if (branch == "sub") c(1e-5, 1) else c(1, 10)
  uniroot(function(m) area_mach(m) - ratio, interval, tol = 1e-11)$root
}
static_ratio <- function(m) (1 + (gamma - 1) * m^2 / 2)^(-gamma / (gamma - 1))
x <- seq(0, 1, length.out = 401)
area <- function(x) 1 + 2 * (x - 0.5)^2
area_values <- area(x)
sub_throat_mach <- 0.65
sub_astar <- 1 / area_mach(sub_throat_mach)
sub_mach <- vapply(area_values / sub_astar, mach_from_area, numeric(1), branch = "sub")
choked_mach <- vapply(seq_along(x), function(i) {
  mach_from_area(area_values[i], if (x[i] <= 0.5) "sub" else "sup")
}, numeric(1))
shock_x <- 0.78
shock_i <- which.min(abs(x - shock_x))
m1 <- choked_mach[shock_i]
m2 <- sqrt((1 + (gamma - 1) * m1^2 / 2) /
           (gamma * m1^2 - (gamma - 1) / 2))
p1 <- static_ratio(m1)
p2 <- p1 * (1 + 2 * gamma / (gamma + 1) * (m1^2 - 1))
down_astar <- area(shock_x) / area_mach(m2)
down_x <- x[shock_i:length(x)]
down_mach <- vapply(area(down_x) / down_astar, mach_from_area,
                    numeric(1), branch = "sub")
down_p0 <- p2 / static_ratio(m2)
case_levels <- c("Unchoked subsonic", "Choked, isentropic",
                 "Choked, example shock")
make_lines <- function(sub, choked, down) {
  data.frame(x = c(x, x, x[seq_len(shock_i)], down_x),
             value = c(sub, choked, choked[seq_len(shock_i)], down),
             case = factor(rep(case_levels, c(length(x), length(x),
                                              shock_i + length(down_x))),
                           levels = case_levels))
}
mach_lines <- make_lines(sub_mach, choked_mach, down_mach)
pressure_lines <- make_lines(static_ratio(sub_mach), static_ratio(choked_mach),
                             down_p0 * static_ratio(down_mach))
back_pressure <- tail(pressure_lines$value, 1)
case_colours <- setNames(c(blue, orange, green), case_levels)
case_types <- setNames(c("dashed", "solid", "dotdash"), case_levels)
nozzle_theme <- figure_theme() +
  theme(plot.title = element_text(size = 12, face = "bold", colour = ink,
                                  margin = margin(b = 7)),
        legend.position = "none", plot.margin = margin(8, 23, 8, 20))
markers <- function() {
  list(geom_vline(xintercept = 0.5, colour = "grey45", linetype = "dotted"),
       geom_vline(xintercept = shock_x, colour = red, linetype = "dashed",
                  linewidth = 0.55))
}
area_plot <- ggplot(data.frame(x, value = area_values), aes(x, value)) +
  markers() + geom_line(colour = ink, linewidth = 1.1) +
  annotate("text", x = 0.5, y = 1.18, label = "throat", colour = ink,
           size = 3.4, hjust = -0.07) +
  annotate("text", x = shock_x, y = 1.43, label = "example shock position",
           colour = red, size = 3.2, hjust = 1.03) +
  scale_x_continuous(limits = c(0, 1), breaks = seq(0, 1, 0.2)) +
  coord_cartesian(ylim = c(0.95, 1.58)) +
  labs(title = "Area ratio", x = NULL, y = "A / A_t") + nozzle_theme
branch_plot <- ggplot(mach_lines, aes(x, value, colour = case, linetype = case,
                                     group = case)) +
  markers() + geom_path(linewidth = 1.05) +
  geom_hline(yintercept = 1, colour = "grey65", linetype = "dotted") +
  scale_colour_manual(values = case_colours) +
  scale_linetype_manual(values = case_types) +
  scale_x_continuous(limits = c(0, 1), breaks = seq(0, 1, 0.2)) +
  coord_cartesian(ylim = c(0, 2.1)) +
  labs(title = "Mach branches", x = NULL, y = "Mach number") + nozzle_theme
pressure_plot <- ggplot(pressure_lines, aes(x, value, colour = case,
                                            linetype = case, group = case)) +
  markers() + geom_path(linewidth = 1.05) +
  annotate("point", x = 1, y = back_pressure, colour = green, size = 3) +
  annotate("label", x = 0.94, y = back_pressure + 0.095,
           label = sprintf("example back pressure = %.3f p0", back_pressure),
           colour = green, fill = "white", linewidth = 0,
           size = 3.2, hjust = 1) +
  scale_colour_manual(values = case_colours) +
  scale_linetype_manual(values = case_types) +
  scale_x_continuous(limits = c(0, 1), breaks = seq(0, 1, 0.2)) +
  coord_cartesian(ylim = c(0, 1.02)) +
  labs(title = "Static pressure", x = "Axial position x / L", y = "p / p0") +
  nozzle_theme + theme(legend.position = "bottom",
                       legend.key.width = grid::unit(1.4, "cm"))
nozzle_panels <- stack_panels(list(area_plot, branch_plot, pressure_plot),
                              c(1, 1, 1.3), 11.6, 10.4)
save_figure("nozzle_branches.png", nozzle_panels, 11.6, 10.4)

# 3. Fixed offsets and assumed intervals are synthetic teaching data.
station <- seq(0.1, 0.9, 0.1)
model <- function(x) 1 - 0.30 * x
offset <- c(0.005, -0.008, 0.010, -0.004, 0.006,
            -0.009, 0.004, 0.008, -0.005)
observed <- model(station) + offset
interval <- 0.012
data <- data.frame(station, observed, residual = offset,
                   lower = observed - interval, upper = observed + interval)
prediction <- data.frame(station = seq(0, 1, length.out = 201))
prediction$value <- model(prediction$station)
measurement_theme <- figure_theme() +
  theme(plot.title = element_text(size = 12, face = "bold", colour = ink,
                                  margin = margin(b = 6)),
        legend.position = "none", plot.margin = margin(8, 23, 8, 20))
comparison_plot <- ggplot() +
  geom_line(data = prediction, aes(station, value), colour = blue,
            linewidth = 1.15) +
  geom_errorbar(data = data, aes(station, ymin = lower, ymax = upper),
                width = 0.012, colour = orange, linewidth = 0.65) +
  geom_point(data = data, aes(station, observed), colour = orange, size = 2.5) +
  annotate("label", x = 0.04, y = 1.005, hjust = 0,
           label = "Blue: model prediction   Orange: synthetic observations",
           fill = "white", linewidth = 0, size = 3.25, colour = ink) +
  scale_x_continuous(limits = c(0, 1), breaks = seq(0, 1, 0.2)) +
  coord_cartesian(ylim = c(0.69, 1.04)) +
  labs(title = "Pressure profile",
       subtitle = "Illustrative synthetic channel data — not validation data",
       x = NULL, y = "Pressure p / p_in") +
  measurement_theme
residual_plot <- ggplot(data, aes(station, residual)) +
  geom_hline(yintercept = 0, colour = "grey45", linetype = "dotted") +
  geom_errorbar(aes(ymin = residual - interval,
                    ymax = residual + interval),
                width = 0.012, colour = orange, linewidth = 0.65) +
  geom_point(colour = orange, size = 2.5) +
  scale_x_continuous(limits = c(0, 1), breaks = seq(0, 1, 0.2)) +
  coord_cartesian(ylim = c(-0.027, 0.027)) +
  labs(title = "Residual = synthetic observation − model",
       subtitle = "Vertical bars show assumed ±0.012 intervals in both panels",
       x = "Channel position x / L", y = "Residual in p / p_in") +
  measurement_theme
measurement_panels <- stack_panels(list(comparison_plot, residual_plot),
                                   c(1, 1), 10.5, 7.2)
save_figure("measurement_comparison.png", measurement_panels, 10.5, 7.2)

cat(sprintf("Wrote three figures; example shock exit p_b/p0 = %.4f\n",
            back_pressure))
