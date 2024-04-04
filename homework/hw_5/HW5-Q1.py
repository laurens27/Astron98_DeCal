# HW 5: Numpy Arrays
# Question 1 - Hey Twin

# Given an array, find the rows where all the values are equal.
# >>> arr = np.array([[1,1,1],[1,2,3],[2,2,2]])
# >>> findEqual(arr)
# array([[1,1,1],
#        [2,2,2]])

# Test Case 1
import numpy as np
def find_rows_with_equal_values(array):
    np_array = np.array(array)
    equal_rows = np_array[np.all(np_array == np_array[:,[0]], axis=1)]
    return equal_rows.tolist()

array = [[1,1,1],[1,2,3],[2,2,2]]

equal_rows = find_rows_with_equal_values(array)
print(equal_rows)


# Test Case 2
array = [[6,6,6],[8,9,10],[8,6,8]]

equal_rows = find_rows_with_equal_values(array)
print(equal_rows)