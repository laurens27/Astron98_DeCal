# HW 5: Numpy Arrays
# Question 2 - Checkers

# Create an 8x8 array with a checkerboard pattern of zeros and ones using a
# slicing + striding approach.
# >>> checkerboard()
#     array([[1, 0,1,0,1,0,1,0],
#            [0 , 1 , 0 , 1 , 0 , 1 , 0 , 1 ],
#            [1 , 0 , 1 , 0 , 1 , 0 , 1 , 0 ],
#            [0 , 1 , 0 , 1 , 0 , 1 , 0 , 1 ],
#            [1 , 0 , 1 , 0 , 1 , 0 , 1 , 0 ],
#            [0 , 1 , 0 , 1 , 0 , 1 , 0 , 1 ],
#            [1 , 0 , 1 , 0 , 1 , 0 , 1 , 0 ],
#            [0 , 1 , 0 , 1 , 0 , 1 , 0 , 1 ]])

import numpy as numpy

checkerboard = np.zeros((8, 8), dtype=int)
checkerboard[::2, ::2] = 1
checkerboard[1::2, 1::2] = 1
print(checkerboard)