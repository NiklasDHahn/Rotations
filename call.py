import numpy as np
from cartesian.transformations import Transformations
from test.test_2d_func import test_2d_rot

test_vector = np.array([7,7])
rotation_angle = 90.

tr = Transformations(test_vector)

rotated = tr.rotation_2d(angle=rotation_angle)

test_2d_rotation = test_2d_rot(rotated)