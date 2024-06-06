#Given an array of integers, return a new array such that each element 
# at index i of the new array is the product of all the numbers in the 
# original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected 
#output would be [120, 60, 40, 30, 24]. If our input was 
# [3, 2, 1], the expected output would be [2, 3, 6].

#Follow-up: what if you can't use division?

#Initial Thoughs:
'''I can find the total product of the list and then divide by each element 
in the list and subsequently add that value to another list.

I can do this without division by using a nested loop to skip the current 
iteration value and then add the resulting product to the new list in the initial loop'''

def exclusionary_product(input):
    total_product = 1
    product_list = []
    for i in input:         #Gets total product
        total_product *= i

    for j in input:         #adds exclusionary product to a list
        product_list.append(total_product/j)
    return(product_list)

print(exclusionary_product([1, 2, 3, 4, 5]))

def sans_division(input):
    product_list = []
    for i in input: 
        iter_product = 1   
        for j in input:
            if i != j:
                iter_product *= j
            print(i, j, iter_product,)
        print()
        product_list.append(iter_product)
    return(product_list)

print(sans_division([3, 2, 1]))

#Final Thoughts:
'''This exercise went exactly as i thought it would. I got turned around with some 
syntax and arithmetic errors but overall pretty easy breezy. I do wonder if this
solution is the most efficient way however...'''