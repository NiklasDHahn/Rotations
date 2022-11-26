import numpy as np

def test_2d_rot(test_input):
    tester = [7, -7]
    
    assert np.array_equal(test_input,tester)
    print("Test Successfull")
