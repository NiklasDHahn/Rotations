import numpy as np
from cartesian.rotations import Rotations
import random
from plots.plot_2d import plot_2d_rotated_coords


tr = Rotations()
x_list, y_list = [], []
x_list_rotated, y_list_rotated = [], []
rotations = []
for i in range(10):
    test_vector = np.random.rand(2,) * 10
    rotation_angle = random.uniform(0,360)
    rotations.append(rotation_angle)
    x_list.append(test_vector[0])
    y_list.append(test_vector[1])
    
    rotated = tr.uniform_rotation_2d(test_vector, rotation_angle)
    x_list_rotated.append(rotated[0])
    y_list_rotated.append(rotated[1])
    
x_before, y_before = np.array(x_list), np.array(y_list)
x_after, y_after = np.array(x_list_rotated), np.array(y_list_rotated)

plot_2d_rotated_coords(x_before, y_before, x_after, y_after)
print(rotations)