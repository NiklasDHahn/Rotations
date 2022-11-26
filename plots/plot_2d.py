import matplotlib.pyplot as plt
import numpy as np


def plot_2d_rotated_coords(x_before: np.ndarray, y_before: np.ndarray, x_after: np.ndarray, y_after: np.ndarray):
    plt.scatter(x_before, y_before, label="original")
    plt.scatter(x_after, y_after, label="rotated")
    
    for i in range(len(x_before)):
        plt.annotate(str(i), (x_before[i], y_before[i]))
        plt.annotate(str(i), (x_after[i], y_after[i]))
    
    plt.legend()
    plt.savefig('.\\2d_rotations.png')