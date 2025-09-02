import numpy as np

from pysphinv.spherical_harmonic_inversion import SphericalHarmonicInversion, SphericalHarmonicsUtils, InversionData

data = InversionData(data_file='/space/ij264/earth-tunya/data/2024/global_holdt.xyz')
inversion = SphericalHarmonicInversion(data)

lambda_norms = np.logspace(1.5, 3.5, 5)
lambda_grads = np.logspace(-1, 1, 5)

# inversion.solve(lambda_norm=400, lambda_grad=1. )
# inversion.plot_grid(fname='/space/ij264/earth-tunya/pysphinv/tests/holdt.png')
# print(inversion.misfit)
inversion.calculate_spectrum_family(lambda_norms, lambda_grads)
inversion.plot_power_spectrum(fname='/space/ij264/earth-tunya/pysphinv/tests/holdt_ps_new.png')

