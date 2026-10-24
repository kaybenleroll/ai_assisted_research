"""Isentropic ideal-gas ratios at a prescribed Mach number."""
import numpy as np

gamma = 1.4
mach = 0.5
factor = 1.0 + 0.5 * (gamma - 1.0) * mach**2
pressure_ratio = factor ** (-gamma / (gamma - 1.0))
density_ratio = factor ** (-1.0 / (gamma - 1.0))

assert np.isclose(pressure_ratio, 0.8430191754, rtol=1e-9)
assert np.isclose(density_ratio, 0.8851701342, rtol=1e-9)
assert 0.0 < density_ratio < 1.0
print(f"p_over_p0={pressure_ratio:.12g} rho_over_rho0={density_ratio:.12g}")
