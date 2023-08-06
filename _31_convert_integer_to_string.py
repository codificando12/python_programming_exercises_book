"""Exercise Description

Write a convertIntToStr() function with an integerNum parameter. This function operates similarly to the str() 
function in that it returns a string form of the parameter. For example, convertIntToStr(42) should return the string '42'. 
The function doesn’t have to work for floating-point numbers with a decimal point, but it should work for negative integer values.

Avoid using Python’s str() function in your code, as that would do the conversion for you and defeat the purpose of this exercise. 
However, we use str() with assert statements to check that your convertIntToStr() function works the same as str() for all integers from -10000 to 9999:

for i in range(-10000, 10000):

    assert convertIntToStr(i) == str(i)

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, read the Solution 
Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: dictionaries, while loops, string concatenation, integer division"""

def convertIntToStr(integerNum):
    
    INT_TO_STR = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    
    negative = ""
    string = ""
    if integerNum == 0:
        string = INT_TO_STR[0]
        return string
    elif integerNum < 0:
        negative += "-"
        integerNum *= -1
        while integerNum > 0:
            number_convert = integerNum % 10
            if number_convert in INT_TO_STR:
                string += INT_TO_STR[number_convert]
            integerNum = integerNum // 10
    else:
        while integerNum > 0:
            number_convert = integerNum % 10
            if number_convert in INT_TO_STR:
                string += INT_TO_STR[number_convert]
            integerNum = integerNum // 10
    if negative != "":
        string += negative
    return string[::-1]

for i in range(-10000, 10000):
    assert convertIntToStr(i) == str(i)

    

    