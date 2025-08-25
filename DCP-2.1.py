'''Given a list of numbers and a number k, 
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, 
return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?'''

def sum():
    nums = [10, 15, 3, 7]
    k = 17

    flag = False
    for i in range(0, len(nums)):
        val = nums[i]
        #print(f"val = {val}")
        for j in range(i + 1, len(nums)):
            nxt_val = nums[j]
            #print(f"nxt_val = {nxt_val}")
            sum_val = val + nxt_val
            #print(f"sum_val = {sum_val} | k = {k}")
            if sum_val == k:
                flag = True
                break
        if flag == True:
            print(flag)
            break

sum()

#revised version
def two_sum(nums, k):
    seen = set()
    for num in nums:
        complement = k - num #by determining the compliment, I can avoid the need for two for loops
        if complement in seen:
            return True
        seen.add(num)
    return False

outcome = two_sum([10, 15, 3, 7], 17)
print(outcome)