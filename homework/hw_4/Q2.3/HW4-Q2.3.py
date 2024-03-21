# HW 4: Lists, Debugging
# Question 2 - List slicing and striding
# 2.3 - Part 3

# You are given two lists: listA and listB. 
# listA contains the integers 1 through 10 while listB contains the integers 20 through 30. 
# Return a single, new list containing only the odd integers of both lists in sorted order.
# Expected output: [1, 3, 5, 7, 9, 21, 23, 25, 27, 29]

listA = [i for i in range(1, 11)]
listB = [i for i in range(20,31)]

odd_listA = []
odd_listB = []

for num in listA:
    if num % 2 != 0:
        odd_listA.append(num)

for num in listB:
    if num % 2 != 0:
        odd_listB.append(num)

odd_integers = odd_listA + odd_listB
print(odd_integers)
