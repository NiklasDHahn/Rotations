import numpy as np
import math

class Rotations():
    def __init__(self, vec):
        self.vec = vec
        
    
    def axes_rotation_2d(self, angle: float) -> np.ndarray:
        assert self.vec.shape == (2,), f"Expected array of shape (2,) but was given {self.vec.shape} instead."
        # Convert from degrees to radians
        angle = angle * math.pi / 180.
        
        # Setup rotation matrix
        mat = np.array([[np.cos(angle), np.sin(angle)],
                         [- np.sin(angle), np.cos(angle)]])
        
        return np.matmul(mat, self.vec)