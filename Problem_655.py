#Given a 32 bit integer, return the number with its bits reversed

#Initial Thoughts:
'''My thought process starts with converting the integer into a list 
and then inverting the list either with a loop or a potential built in function'''

def blind():
    num = 123456789
    inverted_num = []

    while num != 0:
        pv_dim = num//10 #removes a place value from the 1's place
        val = num - 10*(pv_dim)
        inverted_num.append(val)
        num = pv_dim

    print(inverted_num)

#improved function after research:
def informed():
    num = 1234
    inverted_num = []
    while num != 0:
        ones_plc = num % 10
        inverted_num.append(ones_plc)
        num = num//10 

    print(inverted_num)

'''Ok so it has come to my attention that a 32 bit integer is not the same 
as a 32 digit number (obviously, idk what I was thinking). So while this 
solution would work for a 32 bit integer a quicker solution for specifically 
binary numbers would be as follows:'''

def final_func(binary_num):
    numbers = str(binary_num)
    inverted_num = ""

    for i in range(len(numbers),0, -1):
        inverted_num += numbers[i-1]

    return(inverted_num)

print(final_func(11110000))

#Final Thoughts:
'''At first I was hoping to use split to separate the number into a list of characters 
until i remembered strings are lists in of themselves. With this in mind i would iterate 
through the list which would naturally invert the order of numbers. This did not work 
however as computers read numbers from left to right and not by their place value). 

In the end I knew there had to be a way to invert the range function itself which 
I figured out with a with a little help from ChatGPT which resulted in the solution above :)'''
