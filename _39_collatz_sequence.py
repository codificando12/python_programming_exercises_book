"""Write a function named collatz() with a startingNumber parameter. '
The function returns a list of integers of the Collatz sequence that startingNumber produces. 
The first integer in this list must be startingNumber and the last integer must be 1.

Your function should check if startingNumber is an integer less than 1, and in that case, return an empty list.

These Python assert statements stop the program if their condition is False. 
Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ conditions are all True:"""

def collatz(num):

    result = []

    if num == 0:
        return result
    else:
        result.append(num)

    while num > 1:
        if num % 2 == 0:
            num = num / 2
            result.append(num)
        elif num % 2 != 0:
            num = 3 * num + 1
            result.append(num)
        elif num == 1:
            result.append(num)
            break
    return result
    
    

assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert len(collatz(256)) == 9
assert len(collatz(257)) == 123
import random

random.seed(42)

for i in range(1000):

    startingNum = random.randint(1, 10000)

    seq = collatz(startingNum)

    assert seq[0] == startingNum # Make sure it includes the starting number.

    assert seq[-1] == 1  # Make sure the last integer is 1.