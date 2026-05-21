import matplotlib.pyplot as plt

def plot_titration_histogram(volumes):
    plt.hist(volumes, bins=10,color='skyblue',edgecolor='black')
    plt.xlabel("Titration Volume (mL)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Titration Volumes")
    plt.show()
    

# Sample calls
cleaned_volumes = [24.3, 24.7, 24.5, 24.6, 24.8, 24.4, 24.7, 24.6, 24.9, 24.5, 24.7, 24.8, 24.6]
plot_titration_histogram(cleaned_volumes)
