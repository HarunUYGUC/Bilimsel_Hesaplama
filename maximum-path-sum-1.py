""" https://projecteuler.net/problem=18 """
# I find 1064 but the answer is 1074. I still don't understand how it happens because I checked it one by one and it should be 1064.

rows = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34,], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], 
        [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], 
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], 
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,], 
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

sum = rows[0][0]
idOfLargest = 0
 
for i in range(1, len(rows)):

    if (idOfLargest == len(rows[i]) - 1):
        bigger = idOfLargest
        smaller = bigger - 1
    else:
        smaller = idOfLargest
        bigger = idOfLargest + 1
        
    if (rows[i][smaller] > rows[i][bigger]):
        idOfLargest = smaller
        sum += rows[i][smaller]
    else:
        idOfLargest = bigger
        sum += rows[i][bigger]

print(sum)
