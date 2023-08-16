"""Exercise Description

Write a generatePassword() function that has a length parameter. 
The length parameter is an integer of how many characters the generated password should have. 
For security reasons, if length is less than 12, the function forcibly sets it to 12 
characters anyway. The password string returned by the function must have at least one 
lowercase letter, one uppercase letter, one number, and one special character. 
The special characters for this exercise are ~!@#$%^&*()_+.

Your solution should import Python’s random module to help randomly generate these passwords.

These Python assert statements stop the program if their condition is False. 
Copy them to the bottom of your solution program. Your solution is correct if 
the following assert statements’ conditions are all True:

assert len(generatePassword(8)) == 12

 

pw = generatePassword(14)

assert len(pw) == 14

hasLowercase = False

hasUppercase = False

hasNumber = False

hasSpecial = False

for character in pw:

    if character in LOWER_LETTERS:

        hasLowercase = True

    if character in UPPER_LETTERS:

        hasUppercase = True

    if character in NUMBERS:

        hasNumber = True

    if character in SPECIAL:

        hasSpecial = True

assert hasLowercase and hasUppercase and hasNumber and hasSpecial

Try to write a solution based on the information in this description. 
If you still have trouble solving this exercise, read the Solution Design and 
Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: import statements, random module, strings, 
string concatenation, len(), append(), randint(), shuffle(), join()"""

import random

LOWERCASES = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASES = LOWERCASES.upper()
NUMBERS = '0123456789'
SPECIAL_CHARACTERS = '~!@#$%^&*()_+'

def generatePassword(length):
    
    if length < 12:
        length = 12
    
    LOWERCASES = 'abcdefghijklmnopqrstuvwxyz'
    UPPERCASES = LOWERCASES.upper()
    NUMBERS = '0123456789'
    SPECIAL_CHARACTERS = '~!@#$%^&*()_+'

    all_chars = LOWERCASES+UPPERCASES+NUMBERS+SPECIAL_CHARACTERS
    password = []
    
    for i in range(length):
        ran_num = random.randint(0, 74)
        password.append(all_chars[ran_num])

    
    final_pass = ''.join(password)
    return final_pass

assert len(generatePassword(8)) == 12

 

pw = generatePassword(14)

assert len(pw) == 14

hasLowercase = False

hasUppercase = False

hasNumber = False

hasSpecial = False

for character in pw:

    if character in LOWERCASES:

        hasLowercase = True

    if character in UPPERCASES:

        hasUppercase = True

    if character in NUMBERS:

        hasNumber = True

    if character in SPECIAL_CHARACTERS:

        hasSpecial = True
