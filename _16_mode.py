

"""Exercise Description

Write a mode() function that has a numbers parameter. This function returns the mode, or most frequently appearing number, 
of the list of integer and floating-point numbers passed to the function.

These Python assert statements stop the program if their condition is False. 
Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ conditions are all True:

assert mode([]) == None

assert mode([1, 2, 3, 4, 4]) == 4

assert mode([1, 1, 2, 3, 4]) == 1

import random

random.seed(42)



Shuffling the order of the numbers should not affect the mode. The for loop does 1,000 such random shuffles to thoroughly check that this fact remains true. 
For an explanation of the random.seed() function, see the Further Reading section of Exercise #19, “Password Generator”.

Try to write a solution based on the information in this description. If you still have trouble solving this exercise,
 read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: for loops, augmented assignment operators, indexes, not in operator"""

def mode(nums):

    if len(nums) == 0:
        return None
    
    else:
        dict_nums = {}
        
        for i in nums:
            if i  not in dict_nums:
                dict_nums[i] += 1
            else:
                dict_nums[i] = 1

        return max(dict_nums, key=dict_nums.get)


assert mode([]) == None

assert mode([1, 2, 3, 4, 4]) == 4

assert mode([1, 1, 2, 3, 4]) == 1

