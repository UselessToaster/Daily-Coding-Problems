# This problem was asked by Google.
# Difficuly: Medium

# Given an array of integers, return a new array where each element in the new array 
# is the number of smaller elements to the right of that element in the original input array.

#example array: [3, 4, 9, 6, 1]

listA = [3, 4, 9, 6, 1]
listB = []

for num in listA:
    count = 0
    for i in range(listA.index(num), len(listA)):
        #print(n, a[i], c) #---DEBUG
        if i < len(listA) - 1 and listA[i + 1] < num:
            count += 1
    listB.append(count)
print(listB)

#Note: After doing DCP 547, I realized this code could be optimized a little better:
listB = []
for j in range(len(listA)):
    count = 0
    for i in range(j + 1, len(listA)):
        # print(listA[j], listA[i], i, count) #---DEBUG
        if listA[i] < listA[j]:
            count += 1
    listB.append(count)
print(listB)

# Changes:
# - Removed unecessary compount if clause by referring to list values by index instead of element
