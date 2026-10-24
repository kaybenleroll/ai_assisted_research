#!/usr/bin/env Rscript
# Reproducible conceptual schematics for the fluid-mechanics primer.
# Run from primer_fluid_mechanics in the pinned Rocker tidyverse image.
library(ggplot2)

dir.create("figures", showWarnings = FALSE, recursive = TRUE)
BLUE <- "#2271B2"
ORANGE <- "#B86800"
GREEN <- "#00845F"
RED <- "#C34B18"
PURPLE <- "#7B3294"
INK <- "#25313A"
PALE_BLUE <- "#EFF6FA"
PALE_ORANGE <- "#FFF5E8"
HEAD <- grid::arrow(length = grid::unit(0.22, "cm"), type = "closed")

canvas <- function(title, subtitle = NULL) {
  ggplot() +
    coord_cartesian(xlim = c(0, 12), ylim = c(0, 6), expand = FALSE, clip = "off") +
    labs(title = title, subtitle = subtitle) +
    theme_void(base_family = "DejaVu Sans", base_size = 12) +
    theme(plot.title = element_text(size = 15, face = "bold", colour = INK,
                                    margin = margin(b = 8)),
          plot.subtitle = element_text(size = 10.5, colour = INK,
                                       margin = margin(b = 13)),
          plot.margin = margin(22, 32, 25, 32))
}
box <- function(p, x1, x2, y1, y2, fill = PALE_BLUE, edge = BLUE, width = 0.8) {
  p + annotate("rect", xmin = x1, xmax = x2, ymin = y1, ymax = y2,
               fill = fill, colour = edge, linewidth = width)
}
line <- function(p, x1, y1, x2, y2, colour = INK, width = 0.8,
                 arrow = FALSE, linetype = "solid") {
  if (arrow) {
    p + annotate("segment", x = x1, y = y1, xend = x2, yend = y2,
                 colour = colour, linewidth = width, linetype = linetype,
                 arrow = HEAD)
  } else {
    p + annotate("segment", x = x1, y = y1, xend = x2, yend = y2,
                 colour = colour, linewidth = width, linetype = linetype)
  }
}
label <- function(p, x, y, value, size = 4, colour = INK, hjust = 0.5,
                  face = "plain") {
  p + annotate("text", x = x, y = y, label = value, family = "DejaVu Sans",
               size = size, colour = colour, hjust = hjust, fontface = face,
               lineheight = 1.12)
}
save <- function(name, p, width = 11.2, height = 6.4) {
  path <- file.path("figures", paste0(name, ".png"))
  ggsave(path, p, width = width, height = height, units = "in",
         dpi = 150, bg = "white")
  cat(path, "\n")
}

# 1. A moving boundary uses relative velocity; the same flow crosses both CVs.
p <- canvas("Fixed and moving control volumes",
            "The flux through a moving boundary uses fluid velocity relative to that boundary.")
for (cx in c(2.75, 8.75)) {
  p <- line(p, cx - 2.5, 1.85, cx + 2.5, 1.85)
  p <- line(p, cx - 2.5, 4.05, cx + 2.5, 4.05)
  p <- box(p, cx - 1.55, cx + 1.55, 2.18, 3.72)
  p <- label(p, cx, 2.95, "control volume", 4.0)
  p <- line(p, cx - 2.35, 2.95, cx - 1.63, 2.95, ORANGE, arrow = TRUE)
  p <- line(p, cx + 1.63, 2.95, cx + 2.35, 2.95, ORANGE, arrow = TRUE)
}
p <- label(p, 2.75, 5.25, "FIXED", 4.5, BLUE, face = "bold")
p <- label(p, 8.75, 5.25, "MOVING RIGHT", 4.5, BLUE, face = "bold")
p <- line(p, 7.9, 4.45, 9.1, 4.45, GREEN, 1, TRUE)
p <- label(p, 9.42, 4.45, "w", 4, GREEN, hjust = 0)
p <- label(p, 2.75, 1.15, "w = 0; outward flux = rho u · n", 3.7)
p <- label(p, 8.75, 1.15, "outward flux = rho (u - w) · n", 3.7)
p <- label(p, 6, 0.43, "Signs shown assume (u - w)·n < 0 at inlet and > 0 at outlet; reversed flow reverses the signs.", 3.4)
save("moving_control_volume", p)

# 2. One duct and one sign convention for three extensive balances.
p <- canvas("Three balances through the same duct",
            "Stationary duct with one inlet and outlet; positive port flux points out of the control volume.")
p <- box(p, 2.45, 9.55, 3.55, 4.75)
p <- label(p, 6, 4.15, "stored mass, x-momentum and total energy", 4.1)
p <- line(p, 0.85, 4.15, 2.35, 4.15, ORANGE, 1.1, TRUE)
p <- line(p, 9.65, 4.15, 11.15, 4.15, ORANGE, 1.1, TRUE)
p <- label(p, 1.6, 4.62, "inlet", 3.7)
p <- label(p, 10.4, 4.62, "outlet", 3.7)
p <- label(p, 0.7, 2.9, "MASS", 3.8, BLUE, hjust = 0, face = "bold")
p <- label(p, 3.05, 2.9, "dM/dt = m_in - m_out", 4.1, hjust = 0)
p <- label(p, 0.7, 2.1, "MOMENTUM", 3.8, BLUE, hjust = 0, face = "bold")
p <- label(p, 3.05, 2.1, "dP_x/dt = (m u)_in - (m u)_out + F_pressure + F_wall + F_body", 3.45, hjust = 0)
p <- label(p, 0.7, 1.3, "ENERGY", 3.8, BLUE, hjust = 0, face = "bold")
p <- label(p, 3.05, 1.3, "dE_CV/dt = (m H)_in - (m H)_out + Q_in - W_shaft + W_body", 3.25, hjust = 0)
p <- label(p, 6, 0.52, "E_CV = ∫rho E dV; E = e + u²/2; H = h + u²/2; W_body = ∫rho b·u dV.\nm is mass rate; ports are flux averages. Heat in and shaft work out are positive.", 3.0)
save("conservation_balances", p)

# 3. Escalation is driven by evidence and a decision-specific error tolerance.
p <- canvas("Choose a model, test it, then escalate if needed",
            "Candidate classes are examples; no single Reynolds-number threshold selects a model.")
p <- box(p, 0.55, 3.5, 2.72, 4.65)
p <- label(p, 2.02, 3.68, "Question, scales,\nboundaries and\nerror tolerance", 4)
p <- box(p, 4.45, 7.55, 2.72, 4.65, PALE_ORANGE, ORANGE)
p <- label(p, 6, 3.68, "Least complex\ndefensible candidate\n(1D, inviscid, viscous…)", 3.8)
p <- box(p, 8.5, 11.45, 2.72, 4.65, PALE_BLUE, BLUE)
p <- label(p, 9.98, 3.68, "Evidence gate:\nbalances, refinement,\ncomparison, uncertainty", 3.75)
p <- line(p, 3.55, 3.7, 4.36, 3.7, INK, arrow = TRUE)
p <- line(p, 7.6, 3.7, 8.41, 3.7, INK, arrow = TRUE)
p <- line(p, 9.98, 2.68, 9.98, 2.18, INK, arrow = TRUE)
p <- box(p, 6.65, 11.45, 1.1, 2.13, "#EEF8F2", GREEN)
p <- label(p, 9.15, 1.61, "Within tolerance:\nreport range of use", 3.7, GREEN)
p <- box(p, 0.85, 5.55, 1.1, 2.13, "#FFF3EF", RED)
p <- label(p, 3.2, 1.61, "Outside tolerance: add missing physics\nor resolution; repeat the gate", 3.5, RED)
p <- line(p, 8.8, 2.68, 5.1, 2.16, RED, arrow = TRUE)
p <- label(p, 6, 0.43, "Failure may reflect data, boundary conditions, discretisation or model form: diagnose before adding complexity.", 3.35)
save("model_escalation", p)

# 4. Cell-centred pressure correction and face-centred velocities (2D, constant density).
p <- canvas("Pressure projection on a staggered grid",
            "Cell-centred pressure correction; normal velocities live on cell faces.")
for (x in c(1.15, 3.1, 5.05)) p <- line(p, x, 1.1, x, 5.0, "grey50", 0.65)
for (y in c(1.1, 3.05, 5.0)) p <- line(p, 1.15, y, 5.05, y, "grey50", 0.65)
for (x in c(2.125, 4.075)) for (y in c(2.075, 4.025)) {
  p <- label(p, x, y, "phi", 4.1, BLUE, face = "bold")
}
for (y in c(2.075, 4.025)) {
  p <- line(p, 2.79, y, 3.4, y, ORANGE, 1.1, TRUE)
  p <- label(p, 3.1, y + 0.34, "u", 3.8, ORANGE)
}
for (x in c(2.125, 4.075)) {
  p <- line(p, x, 2.75, x, 3.36, GREEN, 1.1, TRUE)
  p <- label(p, x + 0.28, 3.06, "v", 3.8, GREEN, hjust = 0)
}
p <- label(p, 3.1, 0.55, "2 × 2 cells; arrows show positive face directions", 3.35)
p <- label(p, 6.05, 4.9, "1   Predict face velocities u*, v*", 4.0, hjust = 0, face = "bold")
p <- label(p, 6.05, 3.9, "2   Solve for phi from cell divergence", 4.0, hjust = 0, face = "bold")
p <- label(p, 6.35, 3.35, "Laplacian(phi) = (rho / dt) div(u*)", 3.6, hjust = 0)
p <- label(p, 6.05, 2.45, "3   Correct normal face velocities", 4.0, hjust = 0, face = "bold")
p <- label(p, 6.35, 1.9, "u_new = u* - (dt / rho) grad(phi)", 3.65, hjust = 0)
p <- label(p, 6.05, 0.92, "Then each corrected cell has zero discrete divergence.", 3.4, hjust = 0)
p <- label(p, 6, 0.22, "Constant density; use compatible discrete gradient/divergence and boundary conditions.", 3.25)
save("pressure_projection", p)

# 5. The coarse face is the union of two fine faces, not two copies of its flux.
p <- canvas("Conservative coarse-to-fine face coupling",
            "One coarse face meets two fine faces; flux is integrated over each face area.")
p <- box(p, 1.4, 5.3, 1.55, 5.0)
p <- box(p, 5.3, 9.5, 1.55, 3.275, PALE_ORANGE, ORANGE)
p <- box(p, 5.3, 9.5, 3.275, 5.0, PALE_ORANGE, ORANGE)
p <- label(p, 3.0, 3.3, "coarse cell C", 4.1, BLUE)
p <- label(p, 7.65, 4.12, "fine cell 2", 4.0, ORANGE)
p <- label(p, 7.65, 2.42, "fine cell 1", 4.0, ORANGE)
p <- line(p, 4.55, 2.42, 6.15, 2.42, GREEN, 1.15, TRUE)
p <- line(p, 4.55, 4.12, 6.15, 4.12, GREEN, 1.15, TRUE)
p <- label(p, 5.6, 2.75, "F_f1", 3.75, GREEN)
p <- label(p, 5.6, 4.45, "F_f2", 3.75, GREEN)
p <- label(p, 10.05, 4.62, "Shared geometry:", 3.4, INK, hjust = 0)
p <- label(p, 10.05, 4.07, "A_C = A_f1 + A_f2", 3.2, INK, hjust = 0)
p <- label(p, 6, 0.97, "F_C = F_f1 + F_f2", 4.6, GREEN, face = "bold")
p <- label(p, 6, 0.38, "Positive C to fine: subtract F_C from C, add each F_f to its fine cell; fine fluxes need not be equal.", 3.35)
save("coarse_fine_interface", p)

# 6. Distinct evidence routes and conclusions.
p <- canvas("Verification and validation ask different questions",
            "A checked numerical solution can still represent the wrong physical model.")
p <- box(p, 0.55, 5.7, 1.18, 4.75)
p <- box(p, 6.3, 11.45, 1.18, 4.75, PALE_ORANGE, ORANGE)
p <- label(p, 3.12, 5.22, "VERIFICATION", 4.5, BLUE, face = "bold")
p <- label(p, 8.88, 5.22, "VALIDATION", 4.5, ORANGE, face = "bold")
p <- label(p, 3.12, 4.15, "Equations + boundary conditions", 3.9)
p <- line(p, 3.12, 3.92, 3.12, 3.5, BLUE, arrow = TRUE)
p <- label(p, 3.12, 3.22, "Discrete solution", 4.0)
p <- line(p, 3.12, 2.96, 3.12, 2.55, BLUE, arrow = TRUE)
p <- label(p, 3.12, 2.22, "Reference solution; grid/time refinement;\nbalance and residual checks", 3.55)
p <- label(p, 3.12, 1.52, "Evidence of numerical error", 3.7, BLUE, face = "bold")
p <- label(p, 8.88, 4.15, "Model prediction for a stated use", 3.9)
p <- line(p, 8.88, 3.92, 8.88, 3.5, ORANGE, arrow = TRUE)
p <- label(p, 8.88, 3.22, "Independent physical measurements", 3.8)
p <- line(p, 8.88, 2.96, 8.88, 2.55, ORANGE, arrow = TRUE)
p <- label(p, 8.88, 2.22, "Compare with measurement uncertainty\nand operating range", 3.55)
p <- label(p, 8.88, 1.52, "Evidence of model adequacy", 3.7, ORANGE, face = "bold")
p <- label(p, 6, 0.5, "State numerical, measurement and model-form uncertainty; validation applies only to the tested use and range.", 3.3)
save("verification_validation", p)

# 7. Compare laminar attached layers at equal U and x, changing nu only.
p <- canvas("Near-wall layers over a flat plate",
            "Illustrative attached laminar flow at equal free-stream U and plate length; viscosity differs.")
for (bounds in list(c(0.8, 5.65), c(6.35, 11.2))) {
  p <- box(p, bounds[1], bounds[2], 1.65, 1.87, "grey75", "grey45", 0.4)
  p <- line(p, bounds[1] + 0.3, 4.55, bounds[1] + 1.45, 4.55, BLUE, 1.0, TRUE)
  p <- label(p, bounds[1] + 1.8, 4.55, "U", 3.9, BLUE)
  p <- line(p, bounds[1], 1.2, bounds[2], 1.2, INK, 0.7, TRUE)
  p <- label(p, bounds[2] - 0.3, 0.93, "x", 3.7)
}
low_x <- seq(0.9, 5.45, length.out = 150)
high_x <- seq(6.45, 11.0, length.out = 150)
low <- data.frame(x = low_x, y = 1.87 + 1.9 * sqrt((low_x - 0.9) / 4.55))
high <- data.frame(x = high_x, y = 1.87 + 1.03 * sqrt((high_x - 6.45) / 4.55))
p <- p + geom_line(data = low, aes(x, y), colour = ORANGE,
                   linewidth = 1.1, linetype = "dashed") +
  geom_line(data = high, aes(x, y), colour = GREEN,
            linewidth = 1.1, linetype = "dashed")
p <- label(p, 3.2, 5.23, "RELATIVELY LOWER Re_x", 4.2, ORANGE, face = "bold")
p <- label(p, 8.78, 5.23, "RELATIVELY HIGHER Re_x", 4.2, GREEN, face = "bold")
p <- label(p, 3.2, 4.18, "larger nu; thicker layer", 3.8, ORANGE)
p <- label(p, 8.78, 3.52, "smaller nu; thinner layer", 3.8, GREEN)
p <- label(p, 6, 0.49, "Re_x = Ux/nu; dashed edge denotes approximate delta_99. Both Re_x >> 1; transition or separation changes the picture.", 3.25)
save("reynolds_boundary_layer", p)
