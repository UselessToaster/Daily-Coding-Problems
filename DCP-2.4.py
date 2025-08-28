"""
This problem was asked by Stripe.
Difficulty: Hard

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place."""

def main():
    missing_num = missing_int([3, 4, -1, 1])

    print(f"The smallest positive integer missing from this list is: {missing_num}")

def missing_int(input):
    #remove duplicates and order list
    refined_input = set(sorted(input))

    count = 1
    for num in refined_input:
        if num > 0:             #skips negative numbers
            if count == num:    
                count += 1      #continues loop if consecutive number exists
            else:
                return count    #ends loop if missing positive int is found
    
    return count                #returns consecutive number if all positive ints are accounted for
        
main()

