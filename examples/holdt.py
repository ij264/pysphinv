import numpy as np

from spherical_harmonic_inversion import SphericalHarmonicInversion, InversionData, SphericalHarmonicsUtils

data = InversionData(data_file='/space/ij264/earth-tunya/data/2024/global_holdt.xyz')
inversion = SphericalHarmonicInversion(data, l_max=40)
solution = inversion.solve()

coeffs = SphericalHarmonicsUtils.clm_to_vector(solution)
np.savetxt('holdt_coeffs.txt', coeffs)

