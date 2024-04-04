# HW 5: Numpy Arrays
# Question 3 - I need some space

# Given an array of strings, return an array where each letter in each string is
# separated by a space.
# >>> myarr = np.array([’python’,’is’,’cool!’])
# >>> spaceBetween(myarr)
# array([’ p y t h o n ’,’ i s ’,’ c o o l ! ’], dtype=’<U11’)

import numpy as np

def separate_letters_with_space(string_array):
    character_array = np.array([list(string) for string in string_array])
    spaced_array = np.insert(character_array, np.arange(1, character_array.shape[1] * 2, 2), ' ')
   
    return np.array([''.join(row) for row in spaced_array])

string_array = np.array(['python', 'is', 'cool!'])
result = separate_letters_with_space(string_array)
print(result)