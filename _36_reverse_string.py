"""Write a reverseString() function with a text parameter. The function should 
return a string with all of text’s characters in reverse order. 
For example, reverseString('Hello') returns 'olleH'. 
The function should not alter the casing of any letters. 
And, if text is a blank string, the function returns a blank string.

These Python assert statements stop the program if their condition is False. 
Copy them to the bottom of your solution program. 
Your solution is correct if the following assert statements’ conditions are all True:

assert reverseString('Hello') == 'olleH'

assert reverseString('') == ''

assert reverseString('aaazzz') == 'zzzaaa'

assert reverseString('xxxx') == 'xxxx'

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: lists, list(), for loops, range(), len(), integer division, indexes, swapping values, join()"""

def reverseString(string):
    len_chars = len(string)
    result = ""
    for i in range(len_chars):
        result += string[len_chars - 1]
        len_chars -= 1

    return result



assert reverseString('Hello') == 'olleH'

assert reverseString('') == ''

assert reverseString('aaazzz') == 'zzzaaa'

assert reverseString('xxxx') == 'xxxx'