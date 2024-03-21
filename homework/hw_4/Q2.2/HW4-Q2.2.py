# HW 4: Lists, Debugging
# Question 2 - List slicing and striding
# 2.2 - Part 2

# Create a function that takes in a list and squares each element in the list.
# >>> lis = [2, 3, 4] 
# >>> square(lis)
# [4, 9, 16]

lis = [2, 3, 4] 
square(lis)
# want to return: [4, 9, 16]
# returns NameError: name 'square' is not defined
# you have to define square as a function

og_list = [2, 3, 4] 
squared_list = []
def square(og_list):
    for number in og_list: 
        squared_list.append(number**2)
    print(squared_list)
