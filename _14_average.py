"""Exercise Description

Write an average() function that has a numbers parameter. This function returns the statistical average of the list of integer and 
floating-point numbers passed to the function. While Python’s built-in sum() function can help you solve this exercise, try writing the solution without using it.

Passing an empty list to average() should cause it to return None.

These Python assert statements stop the program if their condition is False. 
Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ conditions are all True:

assert average([1, 2, 3]) == 2

assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2

assert average([12, 20, 37]) == 23

assert average([0, 0, 0, 0, 0]) == 0

import random

random.seed(42)

testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]

for i in range(1000):

    random.shuffle(testData)

    assert average(testData) == 2

Shuffling the order of the numbers should not affect the average. 
The for loop does 1,000 such random shuffles to thoroughly check that this fact remains true.
 For an explanation of the random.seed() function, see the Further Reading section of Exercise #19, “Password Generator”.

Try to write a solution based on the information in this description. 
If you still have trouble solving this exercise, read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: len(), for loops, augmented assignment operators"""

def average(nums):
    
    if len(nums) == 0:
        return 0
    
    else:
        res = 0
        for i in nums:
            res = i + res
       
        return res / len(nums)
        

assert average([1, 2, 3]) == 2

assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2

assert average([12, 20, 37]) == 23

assert average([0, 0, 0, 0, 0]) == 0

import random

random.seed(42)

testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]

for i in range(1000):

    random.shuffle(testData)

    assert average(testData) == 2