"""Exercise Description

Write a getSmallest() function that has a numbers parameter. The numbers parameter will be a list of integer and floating-point number values. 
The function returns the smallest value in the list. If the list is empty, the function should return None. 
Since this function replicates Python’s min() function, your solution shouldn’t use it.

These Python assert statements stop the program if their condition is False. Copy them to the bottom of your solution program. 
Your solution is correct if the following assert statements’ conditions are all True:

assert getSmallest([1, 2, 3]) == 1

assert getSmallest([3, 2, 1]) == 1

assert getSmallest([28, 25, 42, 2, 28]) == 2

assert getSmallest([1]) == 1

assert getSmallest([]) == None

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, read the Solution Design and Special Cases and Gotchas sections for additional hints.

When you are done with this exercise, write a getBiggest() function which returns the biggest number instead of the smallest number.

Prerequisite concepts: len(), for loops, lists, None value"""

def getSmallest(list):
    
    if len(list) == 0:
        return None
    else:
        smallest = list[0]
        for small in list:
            if small < smallest:
                smallest = small
            else:
                continue
        
        return smallest

assert getSmallest([1, 2, 3]) == 1

assert getSmallest([3, 2, 1]) == 1

assert getSmallest([28, 25, 42, 2, 28]) == 2

assert getSmallest([1]) == 1

assert getSmallest([]) == None
