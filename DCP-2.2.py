'''
This problem was asked by Uber.
Difficulty: Hard

Given an array of integers, return a new array such that each element 
at index i of the new array is the product of all the numbers in the 
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output 
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the 
expected output would be [2, 3, 6].

Follow-up: what if you can't use division?'''

def main():
    given_arr = [1, 2, 3, 4, 5]

    base_result = base_solution(given_arr)
    print(f"base solution:\n {base_result}\n")

    sans_div_result = w_out_div(given_arr)
    print(f"solution w/out division:\n{sans_div_result}")


def base_solution(array1):
    product = 1
    for element in array1:      #Get product of entire array
        product *= element
    
    new_array = []
    for val in array1:          #divide product by given value and add to new array
        result = product/val
        new_array.append(result)
    return(new_array)

def w_out_div(array1):
    new_arr = []

    for elem in array1:                     #iterate through array
        product = 1

        for elem2 in array1:                #get product of all values not equal to outer loop iterator
            if elem2 != elem:           
                product *= elem2

        new_arr.append(product)             #add product to new array
    
    return(new_arr)


main()
