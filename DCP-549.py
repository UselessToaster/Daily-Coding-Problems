# This problem was asked by Google.

# Given an array of integers where every integer occurs 
# three times except for one integer, which only occurs once, 
# find and return the non-duplicated integer.

# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. 
# Given [13, 19, 13, 13], return 19.

# Do this in O(N) time and O(1) space.

exampleArr = [13, 19, 13, 13]

for num in exampleArr:
    frequency = exampleArr.count(num)
    if frequency == 1:
        print(f"The non-duplicated integer is {num}")


# NOTES #
# At first I didnt know what O(N) time or O(1) space was 
# and im starting to see that the knowledge of machine code 
# concepts and how to implement them is what makes the hard questions hard.


