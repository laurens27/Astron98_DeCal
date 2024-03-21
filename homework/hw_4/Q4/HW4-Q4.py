# HW 4: Lists, Debugging
# Question 4 - More list practice 
# 4 

# Write a function that takes in a list and returns a copy of that list with duplicate values removed.
# >>> lis = [1, 1, 2, 3, 4, 4] 
# >>> removeDuplicates(lis)
# [1,2,3,4]

# TEST CASE 1
listA = [1, 1, 2, 3, 4, 4] # og list
listB = [] # list without duplicates 

[listB.append(x) for x in listA if x not in listB]

print(listB)



# TEST CASE 2
listC = [2, 2, 2, 6, 28, 28, 32, 32] # og list
listD = [] # list without duplicates 

[listD.append(x) for x in listC if x not in listD]

print(listD)