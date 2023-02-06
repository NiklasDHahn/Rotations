import math
import numpy as np

class Rotation:
    def from_euler(self, seq: str, angles: np.array, degrees=False) -> np.array: 

        if seq == 'xyz':
            if degrees:
                omega = angles[0] * math.pi / 180.
                phi = angles[1] * math.pi / 180.
                kappa = angles[2] * math.pi / 180.
            else:
                omega = angles[0]
                phi = angles[1]
                kappa = angles[2]

            r_x = np.array([[1, 0, 0],
                        [0, math.cos(omega), -math.sin(omega)],
                        [0, math.sin(omega), math.cos(omega)]])
            r_y = np.array([[math.cos(phi), 0, math.sin(phi)],
                        [0, 1, 0],
                        [-math.sin(phi), 0, math.cos(phi)]])
            r_z = np.array([[math.cos(kappa), -math.sin(kappa), 0],
                        [math.sin(kappa), math.cos(kappa), 0,],
                        [0, 0, 1]])

            return r_x @ r_y @ r_z
        else:
            print(f'{seq} not yet implemented.')
            