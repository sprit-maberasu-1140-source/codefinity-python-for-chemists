import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def first_order_decay(t, A0, k):
    return A0 * np.exp(-k * t)

def fit_and_plot_kinetics(time, concentration):
    popt, pcov = curve_fit(first_order_decay, time, concentration, p0=(concentration[0], 0.1))
    fitted = first_order_decay(time, *popt)
    plt.scatter(time, concentration, label="Experimental Data")
    plt.plot(time, fitted, color="red", label="Fitted First-Order Decay")
    plt.xlabel("Time (s)")
    plt.ylabel("Concentration (mol/L)")
    plt.legend()
    plt.title("First-Order Kinetics Fit")
    plt.show()
    params = popt
    print(', '.join(map(str, params)))

# Example data
time_points = np.array([0, 1, 2, 3, 4, 5])
concentration_points = np.array([1.0, 0.82, 0.67, 0.55, 0.45, 0.37])

fit_and_plot_kinetics(time_points, concentration_points)
