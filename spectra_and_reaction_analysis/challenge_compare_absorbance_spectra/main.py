import matplotlib.pyplot as plt

def plot_two_absorbance_spectra(wavelengths1, absorbance1, wavelengths2, absorbance2):
    plt.plot(wavelengths1, absorbance1, color='blue', label='Sample 1')
    plt.plot(wavelengths2, absorbance2, color='red', label='Sample 2')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Absorbance')
    plt.title('Absorbance Spectra Comparison')
    plt.legend()
    plt.show()

wavelengths1 = [400, 450, 500, 550, 600, 650, 700]
absorbance1 = [0.05, 0.15, 0.30, 0.25, 0.18, 0.10, 0.05]

wavelengths2 = [400, 450, 500, 550, 600, 650, 700]
absorbance2 = [0.08, 0.20, 0.28, 0.22, 0.16, 0.09, 0.04]

plot_two_absorbance_spectra(wavelengths1, absorbance1, wavelengths2, absorbance2)
