import numpy as np

def calculate_moles(masses, molar_mass):

    moles = masses / molar_mass
    return moles
    

# Sample calls
sample_masses = np.array([18.0, 36.0, 54.0])
sample_molar_mass = 18.0
result = calculate_moles(sample_masses, sample_molar_mass)
print(result)

empty_masses = np.array([])
result_empty = calculate_moles(empty_masses, sample_molar_mass)
print(result_empty)
