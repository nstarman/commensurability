

from commensurability.analysis.coordinates import Cylindrical
from commensurability.analysis.backends import GalpyBackend, GalaBackend

import galpy.potential as gp

# print(vars(GalpyBackend))
# print(vars(GalpyBackend()))

# print(GalaBackend)
# print(GalaBackend())

# from commensurability.analysis import backends

# print(vars(backends))


c = Cylindrical(R=[1, 2, 3], vR=0, vT=[1, 2], z=0, vz=0, phi=90)
g = GalpyBackend()

print('=== ITER_EXAMPLE ===')

for p in g.iter_compute_orbits(gp.MWPotential2014, c, 0.01, 5):
    print(p)

print()
print()
print('=== ITER_SLICE_EXAMPLE ===')

for iter_p in g.iter_compute_orbit_slices(gp.MWPotential2014, c, 0.01, 5, 10):
    print('== SLICE ==')
    for p in iter_p:
        print(p)