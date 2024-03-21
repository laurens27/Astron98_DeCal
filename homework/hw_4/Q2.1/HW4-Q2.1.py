# HW 4: Lists, Debugging
# Question 2 - List slicing and striding
# 2.1 - Part 1

# Create a variable (name it anything you want but make it descriptive!) 
# that is assigned to a list with the numbers 0 to 50. 
# You should not have to write each number manually.

list_through_50 = [i for i in range(0, 51)]
print(list_through_50)

# ERRORS
# At first, it only printed numbers up to 49
# I realized it should be range(0,51) rather than range(0,50)