"""Write a commaFormat() function with a number parameter. The argument for this parameter can be an integer or floating-point number. 
Your function returns a string of this number with proper US/UK comma formatting. There is a comma after every third digit in the whole number part. 
There are no commas at all in the fractional part: The proper comma formatting of 1234.5678 is 1,234.5678 and not 1,234.567,8.           

These Python assert statements stop the program if their condition is False. Copy them to the bottom of your solution program. 
Your solution is correct if the following assert statements’ conditions are all True:

assert commaFormat(1) == '1'

assert commaFormat(10) == '10'

assert commaFormat(100) == '100'

assert commaFormat(1000) == '1,000'

assert commaFormat(10000) == '10,000'

assert commaFormat(100000) == '100,000'

assert commaFormat(1000000) == '1,000,000'

assert commaFormat(1234567890) == '1,234,567,890'

assert commaFormat(1000.123456) == '1,000.123456'

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, 
read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: strings, str(), in operator, index(), slices, string concatenation"""

def commaFormat(num):
    
    str_num = str(num)
    if "." in str_num:
        decimal_dot = str_num.index(".")
        decimal_num = str_num[decimal_dot:]
        add_coma_num = str_num[: decimal_dot]
    else:
        decimal_num = ""
        add_coma_num = str_num
    added_comma_num = ""
    if num < 1000:
        return str_num
    
    elif len(add_coma_num) > 3:
        comma_index = 0
        for i in add_coma_num[::-1]:
            if comma_index < 3:
                added_comma_num += i
                comma_index += 1
            else:
                comma_index = 0
                added_comma_num += ","
                added_comma_num += i
                comma_index += 1
    return added_comma_num[::-1] + decimal_num

assert commaFormat(1) == '1'

assert commaFormat(10) == '10'

assert commaFormat(100) == '100'

assert commaFormat(1000) == '1,000'

assert commaFormat(10000) == '10,000'

assert commaFormat(100000) == '100,000'

assert commaFormat(1000000) == '1,000,000'

assert commaFormat(1234567890) == '1,234,567,890'

assert commaFormat(1000.123456) == '1,000.123456'