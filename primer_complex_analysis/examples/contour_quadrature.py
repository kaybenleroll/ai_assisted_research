"""Check contour quadrature against the residue theorem for a smooth circle."""

import cmath
import math


RADIUS = 0.4
RESOLUTIONS = (8, 16, 32, 64)
ABSOLUTE_TOLERANCE = 1e-12

# Counterclockwise C: |z - 1| = RADIUS encloses the simple pole at z = 1
# and no singularity lies on C. By Cauchy's integral formula, the exact
# integral of exp(z)/(z - 1) is 2*pi*i*exp(1).
exact = 2j * math.pi * math.e
estimates = []
errors = []

for n in RESOLUTIONS:
    total = 0j
    for k in range(n):
        theta = 2 * math.pi * k / n
        z = 1 + RADIUS * cmath.exp(1j * theta)
        dz_dtheta = 1j * RADIUS * cmath.exp(1j * theta)
        total += cmath.exp(z) / (z - 1) * dz_dtheta
    estimate = total * (2 * math.pi / n)
    estimates.append(estimate)
    errors.append(abs(estimate - exact))

# The first refinement must reduce error; later values are near the
# double-precision floor, so require agreement with the stated absolute
# tolerance rather than strict monotonicity at every resolution.
assert errors[1] < errors[0]
assert all(error <= ABSOLUTE_TOLERANCE for error in errors[1:])
