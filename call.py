import numpy as np
from cartesian.rotations import Rotations
from test.test_2d_func import test_2d_rot

test_vector = np.array([7,7])
rotation_angle = 90.

tr = Rotations(test_vector)

rotated = tr.rotation_2d_origin(angle=rotation_angle)

test_2d_rotation = test_2d_rot(rotated)