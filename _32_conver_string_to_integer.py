"""Exercise Description

Write a convertStrToInt() function with a stringNum parameter. This function returns an integer form of the parameter just like the int() function. For example, 
convertStrToInt('42') should return the integer 42. The function doesn’t have to work for floating-point numbers with a decimal point, but it should work for negative number values.

Avoid using int()in your code, as that would do the conversion for you and defeat the purpose of this exercise. However, 
we do use int() with assert statements to check that your convertStrToInt() function works the same as int() for all integers from -10000 to 9999:

for i in range(-10000, 10000):

    assert convertStrToInt(str(i)) == i

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, read the Solution Design and Special Cases and Gotchas sections for additional hints."""


def convertStrToInt(string):
    
    STR_TO_INT = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9 }

    final_num = 0
    if string[0] == "-":

        for num in string[1:]:

            final_num = (final_num * 10) + STR_TO_INT[num]

        return final_num * (-1)
    else:
        for num in string:

            final_num = (final_num * 10) + STR_TO_INT[num]

        return final_num

for i in range(-10000, 10000):

    assert convertStrToInt(str(i)) == i