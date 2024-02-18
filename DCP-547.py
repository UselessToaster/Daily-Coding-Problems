# This problem was asked by Salesforce.
# Rating: Hard

# Given an array of integers, find the maximum XOR of any two elements.

# ***ORIGINAL SOLUTION***
smplList = [3, 10, 5, 25, 2, 8]
xorList = []
#print(len(smplList) - 1) #---DEBUG

for num in smplList:
    #print("Current num: ", num) #---DEBUG
    i = 1
    for i in range(i, len(smplList)):
        if i + smplList.index(num) < 6:
            nextVal = smplList[i + smplList.index(num)]
            #[print(i, num, nextVal, num ^ nextVal)] #---DEBUG
            xorList.append(num ^ nextVal)
        #Would an else statement with a break function improve processing speed?
print("Max XOR of given list: ", max(xorList))

# After consulting ChatGPT, I've discovered the secondary list was unnecessary and 
# inefficient as the only thing that matters is the max XOR. Thus, If i replace the
# XOR list with a simple integer value and compare the previously stored value with 
# the new XOR calculation, the result will be more accurate and efficient.abs

# ***REFINED SOLUTION W/NOTES***:
maxXOR = 0

for i in range(len(smplList)):                 #iterates over indecies rather than elements & range(x) == 0 to x - 1
    for j in range(i + 1, len(smplList)):      #starts from next value in less complicated way
        xorResult = smplList[i] ^ smplList[j]  
        maxXOR = max(maxXOR, xorResult)

print("Max XOR of given list: ", maxXOR)
# With this exercise I have relearned:
# - the difference in effectiveness between <for [element] in [list]:> vs <for [number] in range():>
# - the bounds of the range() function
# - to consider only the necessary information needed to solve the problem
