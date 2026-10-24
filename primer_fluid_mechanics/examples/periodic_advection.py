"""Conservative first-order upwind advection with a fixed-time refinement check."""
import numpy as np

def run(n, final_time=0.5, cfl_target=0.4):
    length, velocity = 1.0, 0.4
    dx = length / n
    steps = int(np.ceil(final_time / (cfl_target * dx / velocity)))
    dt = final_time / steps
    cfl = velocity * dt / dx
    if not 0.0 < cfl <= 1.0:
        raise ValueError(f"invalid CFL={cfl}")
    x = (np.arange(n) + 0.5) * dx
    # The exact state is a cell average, not a point sample at the centre.
    cell_average_factor = np.sinc(1.0 / n)
    initial = 1.0 + 0.2 * cell_average_factor * np.sin(2.0 * np.pi * x)
    field = initial.copy()
    for _ in range(steps):
        # One periodic face flux is shared by its two neighbouring cells.
        outgoing = velocity * field
        incoming = np.roll(outgoing, 1)
        field -= dt / dx * (outgoing - incoming)
    exact = 1.0 + 0.2 * cell_average_factor * np.sin(
        2.0 * np.pi * ((x - velocity * final_time) % length)
    )
    mass_initial = np.sum(initial) * dx
    mass_final = np.sum(field) * dx
    error = np.linalg.norm(field - exact) / np.sqrt(n)
    return mass_initial, mass_final, error, cfl

mass0, final0, error_n, cfl_n = run(32)
mass1, final1, error_2n, cfl_2n = run(64)
mass2, final2, error_4n, cfl_4n = run(128)
assert abs(final0 - mass0) < 1e-12
assert abs(final1 - mass1) < 1e-12
assert abs(final2 - mass2) < 1e-12
assert error_2n < error_n and error_4n < error_2n
assert max(cfl_n, cfl_2n, cfl_4n) <= 0.4
try:
    run(32, cfl_target=2.0)
except ValueError as exc:
    assert "invalid CFL" in str(exc)
else:
    raise AssertionError("CFL above one was not rejected")
print(f"mass={mass2:.12g} errors={error_n:.6g},{error_2n:.6g},{error_4n:.6g}")
