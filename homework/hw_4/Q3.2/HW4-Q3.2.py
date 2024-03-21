# HW 4: Lists, Debugging
# Question 3 - 2D Lists 
# 3.2 - Part 2

# Now with your completed 2D list, replace all multiples of 3 with '?' character 
# and print the resulting list. 

# Expected output: [[1, 2, ?, 4, 5], 
#                  [?, 7, 8, ?, 10],
#                  [11, ?, 13, 14, ?],
#                  [16, 17, ?, 19, 20],
#                  [?, 22, 23, ?, 25]] 

final_list = []

counter = 1
for i in range(5):
    row = []
    for j in range(5):
        row.append(counter)
        counter += 1
    final_list.append(row)

for i in range(5):
    for j in range(5):
        if final_list[i][j] % 3 == 0:
            final_list[i][j] = '?'

for row in final_list:
    print(row)



# ERRORS
# NameError: name 'matrix' is not defined
# I accidentally used a different name for my final list, so I must remember to be consistent with my variable names. 

# IndentationError: unexpected indent
# I added an exxtra line that should not have been there. 
    
# IndexError: list index out of range
# I'm not sure what was out of range, but I seperated the new code for this question 
# onto its own lines which fixed the problem. 