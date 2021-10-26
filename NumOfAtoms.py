#Constant

Avogadro = (6.02214076) * (10**23)

#function for finding number of atoms

def num_atoms(mass, molarmass = 196.97):
    mol = mass/molarmass
    atoms = mol * Avogadro
    print(atoms)


num_atoms(10)