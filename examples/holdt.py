from pysphinv.spherical_harmonic_inversion import SphericalHarmonicInversion, SphericalHarmonicsUtils, InversionData

data = InversionData(data_file='/space/ij264/earth-tunya/data/2024/global_holdt.xyz')
inversion = SphericalHarmonicInversion(data)
inversion.solve(lambda_norm=400, lambda_grad=1. )
inversion.plot_grid(fname='/space/ij264/earth-tunya/pysphinv/tests/holdt.png')
print(inversion.misfit)
inversion.calculate_power_spectrum()
inversion.plot_power_spectrum(fname='/space/ij264/earth-tunya/pysphinv/tests/holdt_ps.png')

