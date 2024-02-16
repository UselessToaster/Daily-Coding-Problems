# This problem was asked by Google.

# Given an array of integers, return a new array where each element in the new array 
# is the number of smaller elements to the right of that element in the original input array.

#example array: [3, 4, 9, 6, 1]

listA = [3, 4, 9, 6, 1]
listB = []

i = 0

for num in listA:
    count = 0
    for i in range(listA.index(num), len(listA)):
        #print(n, a[i], c) #---DEBUG
        if i < len(listA) - 1 and listA[i + 1] < num:
            count += 1
    listB.append(count)
print(listB)