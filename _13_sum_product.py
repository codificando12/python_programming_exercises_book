"""Exercise Description

Write two functions named calculateSum() and calculateProduct(). They both have a parameter named numbers, 
which will be a list of integer or floating-point values. The calculateSum() function adds these numbers and 
returns the sum while the calculateProduct() function multiplies these numbers and returns the product. 
If the list passed to calculateSum() is empty, the function returns 0. If the list passed to calculateProduct() 
is empty, the function returns 1. Since this function replicates Python’s sum() function, your solution shouldn’t call.

These Python assert statements stop the program if their condition is False. 
Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ 
conditions are all True:

assert calculateSum([]) == 0

assert calculateSum([2, 4, 6, 8, 10]) == 30

assert calculateProduct([]) == 1

assert calculateProduct([2, 4, 6, 8, 10]) == 3840

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: lists, indexes, for loops, augmented assignment operator"""


def calculateSum(nums):
    if len(nums) == 0:
        return 0
    
    else:
        res = 0
        for i in nums:
            res = i + res
        return res

def calculateProduct(nums):
    if len(nums) == 0:
        return 1
    else:
        res = nums[0]
        for i in nums[1:]:
            res = i * res
        return res
    
assert calculateSum([]) == 0

assert calculateSum([2, 4, 6, 8, 10]) == 30

assert calculateProduct([]) == 1

assert calculateProduct([2, 4, 6, 8, 10]) == 3840