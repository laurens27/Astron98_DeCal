# HW 4: Lists, Debugging
# Question 3 - 2D Lists 
# 3.1 - Part 1

# Using nested for loops, create and print a 5x5 2D list with the numbers 1 to 25. 

# Expected output: [[1, 2, 3, 4, 5], 
#                  [6, 7, 8, 9, 10],
#                  [11, 12, 13, 14, 15],
#                  [16, 17, 18, 19, 20],
#                  [21, 22, 23, 24, 25]] 

final_list = []

counter = 1
for i in range(5):
    row = []
    for j in range(5):
        row.append(counter)
        counter += 1
    final_list.append(row)

for row in final_list:
    print(row)
