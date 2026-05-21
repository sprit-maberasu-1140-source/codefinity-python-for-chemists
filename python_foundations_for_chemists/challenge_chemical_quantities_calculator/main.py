def calculate_moles(mass, molar_mass):
    moles = mass / molar_mass
    return moles
    
sample_mass = 18.0
sample_molar_mass = 18.015
sample_moles = calculate_moles(sample_mass, sample_molar_mass)
print(sample_moles)
