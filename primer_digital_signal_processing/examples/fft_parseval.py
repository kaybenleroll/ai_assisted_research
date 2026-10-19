"""Check NumPy's unnormalised DFT energy identity on a fixed real signal."""

import numpy as np


signal = np.array([1.0, -2.0, 0.5, 3.0, -1.5, 0.0, 2.0, -0.5])
spectrum = np.fft.fft(signal)

# NumPy's forward FFT is unnormalised, so Parseval gives
# sum(|X[k]|**2) = N * sum(|x[n]|**2). This tolerance is generous relative
# to round-off across eight samples and strict against a scaling/index error.
time_energy = np.sum(np.abs(signal) ** 2)
frequency_energy = np.sum(np.abs(spectrum) ** 2)
assert np.isclose(frequency_energy, signal.size * time_energy, rtol=1e-12, atol=1e-12)

# A real input has conjugate-symmetric DFT bins.
assert np.allclose(spectrum[1:], np.conjugate(spectrum[:0:-1]), rtol=1e-12, atol=1e-12)
