"""Analytical plane-channel baseline used by the primer."""
import numpy as np

h = 1.0e-3
w = 20.0e-3
length = 0.20
mu = 1.0e-3
rho = 1000.0
mean_speed = 0.020

re = rho * mean_speed * h / mu
pressure_drop = 12.0 * mu * length * mean_speed / h**2
flow_rate = mean_speed * w * h
y = np.linspace(-h / 2.0, h / 2.0, 101)
profile = 1.5 * mean_speed * (1.0 - (2.0 * y / h) ** 2)

assert np.isclose(re, 20.0, rtol=1e-12)
assert np.isclose(pressure_drop, 48.0, rtol=1e-12)
assert np.isclose(flow_rate, 4.0e-7, rtol=1e-12)
assert np.isclose(profile[0], 0.0, atol=1e-14)
assert np.isclose(profile[-1], 0.0, atol=1e-14)
assert np.isclose(np.trapezoid(profile, y) / h, mean_speed, rtol=2e-4)
print(f"Re_h={re:.12g} pressure_drop_pa={pressure_drop:.12g} flow_rate_m3_s={flow_rate:.12g}")
