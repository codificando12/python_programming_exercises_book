"""Exercise Description

Write a median() function that has a numbers parameter. This function returns the statistical median of the numbers list. 
The median of an odd-length list is the number in the middlemost number when the list is in sorted order. 
If the list has an even length, the median is the average of the two middlemost numbers when the list is in sorted order. 
Feel free to use Python’s built-in sort() method to sort the numbers list.

Passing an empty list to average() should cause it to return None.

These Python assert statements stop the program if their condition is False. 
Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ conditions are all True:

assert median([]) == None

assert median([1, 2, 3]) == 2

assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5

assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

import random

random.seed(42)

testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]

for i in range(1000):

    random.shuffle(testData)

    assert median(testData) == 6

Shuffling the order of the numbers should not affect the median. The for loop does 1,000 such random shuffles to thoroughly check that this fact remains true. For an explanation of the random.seed() function, see the Further Reading section of Exercise #19, “Password Generator”.

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: len(), for loops, augmented assignment operators, integer division, modulo operator, indexes"""

def median(nums):

    order = sorted(nums)

    if len(nums) == 0:
        return None
    else:
        if len(nums) % 2 != 0:
            index = int(len(nums) / 2)
            return order[index]
        else:
            index = int(len(nums) / 2)
            average = round((order[index] + order[index - 1]) / 2, 1)
            return average
            



assert median([]) == None

assert median([1, 2, 3]) == 2

assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5

assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6