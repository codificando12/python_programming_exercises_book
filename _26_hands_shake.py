"""Exercise Description

Write a function named printHandshakes() with a list parameter named people which will be a 
list of strings of people’s names. The function prints out 'X shakes hands with Y', 
where X and Y are every possible pair of handshakes between the people in the list. 
No duplicates are permitted: if “Alice shakes hands with Bob” appears in the output, 
then “Bob shakes hands with Alice” should not appear.

For example, printHandshakes(['Alice', 'Bob', 'Carol', 'David']) should print:

Alice shakes hands with Bob

Alice shakes hands with Carol

Alice shakes hands with David

Bob shakes hands with Carol

Bob shakes hands with David

Carol shakes hands with David

The printHandshakes() function must also return an integer of the number of handshakes.

These Python assert statements stop the program if their condition is False. 
 them to the bottom of your solution program. Your solution is correct if the output 
 displays all possible handshakes and the following assert statements’ conditions are all True:

assert printHandshakes(['Alice', 'Bob']) == 1

assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3

assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, 
read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: for loops, range() with two arguments, len(), augmented assignment operators

"""

def printHandshakes(names):

    shake = 0
    next_person = 1
    for i in range(shake, len(names)):
        for j in range(next_person, len(names)):
            print(names[i], 'shake hands with', names[j])
            shake += 1
        next_person += 1
    
    return shake
    
assert printHandshakes(['Alice', 'Bob']) == 1

assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3

assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6