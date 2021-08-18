import pymatgen.core as pg

'''
The Element class is located in the core subpakage inside the periodic_table module. The link to the API documentation is below.

https://pymatgen.org/pymatgen.core.periodic_table.html#pymatgen.core.periodic_table.Element
'''

# Fetch details of an Element
fe = pg.Element("Fe")

# Atomic mass
print('atomic mass: ', fe.atomic_mass)
print('atomic mass: ', fe.Z)
print('atomic radius: ', fe.atomic_radius_calculated)

from pymatgen.ext.matproj import MPRester
m = MPRester('fmdc9tZK1xE74JOq')
for s in m.get_structures("mp-2894"):
    print(s.lattice.abc)
