"""Write a getTitleCase() function with a text parameter. The function should return the title case form of the string: 
every word begins with an uppercase and the remaining letters are lowercase. Non-letter characters separate words in the string. 
This means that 'Hello World' is considered to be two words while 'HelloWorld' is considered to be one word. 
Not only spaces, but all non-letter characters can separate words, so 'Hello5World' and 'Hello@World' also have two words.

Python’s upper() and lower() string methods return uppercase and lowercase forms of the string, 
and you can use these in your implementation. You may also use the isalpha() string method, 
which returns True if the string contains only uppercase or lowercase letter characters. 
However, you may not use Python’s title() string method, as that would defeat the purpose of the exercise. 
Similarly, while you need to split up a string into individual words, don’t use Python’s split() string method.

These Python assert statements stop the program if their condition is False. 
Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ conditions are all True:

assert getTitleCase('Hello, world!') == 'Hello, World!'

assert getTitleCase('HELLO') == 'Hello'

assert getTitleCase('hello') == 'Hello'

assert getTitleCase('hElLo') == 'Hello'

assert getTitleCase('') == ''

assert getTitleCase('abc123xyz') == 'Abc123Xyz'

assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'

assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'

import random

random.seed(42)

chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')

for i in range(1000):

    random.shuffle(chars)

    assert getTitleCase(''.join(chars)) == ''.join(chars).title()

The code in the for loop generates random strings and checks that your getTitleCase() function returns the same string that Python’s built-in title() string method does. This allows us to quickly generate 1,000 test cases for your solution.

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: strings, for loops, range(), len(), upper(), isalpha(), lower()"""

def getTitleCase(sentence):
    
    sentence = sentence.lower()
    result = ""
    upper_case = 0
    for i in sentence:
        if i.isalpha() and upper_case == 0:
            upper = i.upper()
            result += upper
            upper_case = 1
        elif i.isalpha() and upper_case == 1:
            result += i
        else:
            upper_case = 0
            result += i
    
    return result

assert getTitleCase('Hello, world!') == 'Hello, World!'

assert getTitleCase('HELLO') == 'Hello'

assert getTitleCase('hello') == 'Hello'

assert getTitleCase('hElLo') == 'Hello'

assert getTitleCase('') == ''

assert getTitleCase('abc123xyz') == 'Abc123Xyz'

assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'

assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'

import random

random.seed(42)

chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')

for i in range(1000):

    random.shuffle(chars)

    assert getTitleCase(''.join(chars)) == ''.join(chars).title()