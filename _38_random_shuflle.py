"""A random shuffle algorithm puts the values in a list into a random order, like shuffling a deck of cards. This algorithm produces a new permutation, or ordering, of the values in the list. The algorithm works by looping over each value in the list and randomly determining a new index with which to swap it. As a result, the values in the list are in random order.

For a list of n values, there are n! (“n factorial”) possible permutations. For example, a 10-value list has 10! or 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 or 3,628,800 possible ways to order them.

This exercise modifies the list passed to it in-place, rather than creating a new list and returning it. Because lists are mutable objects in Python, modifications made to a parameter are actually modifying the original object passed to the function call for that parameter. For example, enter the following into the interactive shell:

>>> someList = [1, 2, 3]  # Let's create a list object.

>>> def someFunc(someParam):

...     someParam[0] = 'dog'  # This is changing the list in-place.

...     someParam.append('xyz')  # This is changing the list in-place.

...

>>> someList 

[1, 2, 3]

>>> someFunc(someList)  # Pass the list as the argument.

>>> someList  # Note that the list object has been modified by the function.

['dog', 2, 3, 'xyz']

Notice that the someList list is passed as the argument for the someParam parameter of the someFunc() function. This function modifies someParam (which refers to the same list object that the someList variable refers to), so these modifications are still there after the function returns. The someFunc() function isn’t returning a new list to replace someList; it’s modifying someList in-place.

In Python, only mutable objects (such as lists, dictionaries, and sets) can be modified in-place. Immutable objects (such a strings, integers, tuples, and frozen sets) can’t be modified in-place."""

import random


def shuffle(lst):

    shuffled = []
    while len(lst) != len(shuffled):
        random_int = random.randint(0, len(lst) - 1)
        if lst[random_int] not in shuffled:
            shuffled.append(lst[random_int])
        else:
            continue   
    
    return shuffled


random.seed(42)

# Perform this test ten times:

for i in range(10):

    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    testData1 = shuffle(testData1)

    # Make sure the number of values hasn't changed:

    assert len(testData1) == 10

    # Make sure the order has changed:

    assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Make sure that when re-sorted, all the original values are there:

    assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

 

# Make sure an empty list shuffled remains empty:

testData2 = []

shuffle(testData2)

assert testData2 == []