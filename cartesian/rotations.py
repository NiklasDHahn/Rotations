import numpy as np
import math

class Rotations():     
    
    def uniform_rotation_2d(self, array: np.array, angle: float) -> np.ndarray:
        assert array.shape == (2,), f"Expected array of shape (2,) but was given {array.shape} instead."
        # Convert from degrees to radians
        angle = angle * math.pi / 180.
        
        # Setup rotation matrix
        mat = np.array([[np.cos(angle), np.sin(angle)],
                         [- np.sin(angle), np.cos(angle)]])
        
        return np.matmul(mat, array)