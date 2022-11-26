import numpy as np
import math

class Rotations():
    def __init__(self, vec):
        self.vec = vec
        
    
    def rotation_2d_origin(self, angle: float) -> np.ndarray:
        assert len(self.vec) == 2, f"Array of length {len(self.vec)} was provided for 2d roation."
        # Convert from degrees to radians
        angle = angle * math.pi / 180.
        
        # Setup rotation matrix
        mat = np.array([[np.cos(angle), np.sin(angle)],
                         [- np.sin(angle), np.cos(angle)]])
        
        return np.matmul(mat, self.vec)