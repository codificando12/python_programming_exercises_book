"""Write a getUppercase() function with a text string parameter. The function returns a string with 
all lowercase letters in text converted to uppercase. Any non-letter characters in text remain as they are.
 For example, 'Hello' causes getUppercase() to return 'HELLO' but 'goodbye 123!' returns 'GOODBYE 123!'.

These Python assert statements stop the program if their condition is False. Copy them to the bottom of 
your solution program. Your solution is correct if the following assert statements’ conditions are all True:

assert getUppercase('Hello') == 'HELLO'

assert getUppercase('hello') == 'HELLO'

assert getUppercase('HELLO') == 'HELLO'

assert getUppercase('Hello, world!') == 'HELLO, WORLD!'

assert getUppercase('goodbye 123!') == 'GOODBYE 123!'

assert getUppercase('12345') == '12345'

assert getUppercase('') == ''

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, 
read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: for loops, in operator, string concatenation, indexes"""

def getUppercase(sentence):

    SMALL = "abcdefghijklmnopqrstuvwxyz"
    UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = ""

    for i in sentence:
        if i in SMALL:
            ind = SMALL.index(i)
            result += UPPER[ind]
        else:
            result += i

    return result

assert getUppercase('Hello') == 'HELLO'

assert getUppercase('hello') == 'HELLO'

assert getUppercase('HELLO') == 'HELLO'

assert getUppercase('Hello, world!') == 'HELLO, WORLD!'

assert getUppercase('goodbye 123!') == 'GOODBYE 123!'

assert getUppercase('12345') == '12345'

assert getUppercase('') == ''