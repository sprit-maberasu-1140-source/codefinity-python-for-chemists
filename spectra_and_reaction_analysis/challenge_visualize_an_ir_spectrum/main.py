import matplotlib.pyplot as plt

def plot_ir_spectrum(wavenumbers, absorbance):
    plt.figure(figsize=(8, 5))
    plt.plot(wavenumbers, absorbance, color='blue')
    plt.xlabel("Wavenumber (cm$^{-1}$)")
    plt.ylabel("Absorbance")
    plt.title("IR Spectrum")
    plt.gca().invert_xaxis()
    plt.tight_layout()
    plt.show()

# Sample data
wavenumbers = [4000, 3500, 3000, 2500, 2000, 1500, 1000, 500]
absorbance = [0.05, 0.15, 0.40, 0.25, 0.10, 0.20, 0.18, 0.09]

plot_ir_spectrum(wavenumbers, absorbance)