"""Exercise Description

Write an isValidDate() function with parameters year, month, and day. The function should return True 
if the integers provided for these parameters represent a valid date. Otherwise, the function returns False. 
Months are represented by the integers 1 (for January) to 12 (for December) and days are represented by integers 
1 up to 28, 29, 30, or 31 depending on the month and year. Your solution should import your leapyear.py program from 
Exercise #20 for its isLeapYear() function, as February 29th is a valid date on leap years.

September, April, June, and November have 30 days. The rest have 31, except February which has 28 days. On leap years, February has 29 days.

These Python assert statements stop the program if their condition is False. Copy them to the bottom of your solution program. 
Your solution is correct if the following assert statements’ conditions are all True:

assert isValidDate(1999, 12, 31) == True

assert isValidDate(2000, 2, 29) == True

assert isValidDate(2001, 2, 29) == False

assert isValidDate(2029, 13, 1) == False

assert isValidDate(1000000, 1, 1) == True

assert isValidDate(2015, 4, 31) == False

assert isValidDate(1970, 5, 99) == False

assert isValidDate(1981, 0, 3) == False

assert isValidDate(1666, 4, 0) == False

 

import datetime

d = datetime.date(1970, 1, 1)

oneDay = datetime.timedelta(days=1)

for i in range(1000000):

    assert isValidDate(d.year, d.month, d.day) == True

    d += oneDay

Try to write a solution based on the information in this description. If you still have trouble solving this exercise,
read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: import statements, Boolean operators, chaining operators, elif statements"""

from _20_leap_year import isLeapYear

def isValidDate(year, month, day):
    
    if not (1 <= month <= 12):
        return False
    
    if isLeapYear(year) and month == 2 and day == 29:
        return True
    
    if month in (1, 3, 5, 7, 8, 10, 12) and not (1 <= day <=31):
        return False

    elif month in (4, 6, 9, 11) and not (1 <= day <=30):
        return False

    elif month == 2 and not (1 <= day <= 28):
        return False
    
    return True

    
    
assert isValidDate(1999, 12, 31) == True

assert isValidDate(2000, 2, 29) == True

assert isValidDate(2001, 2, 29) == False

assert isValidDate(2029, 13, 1) == False

assert isValidDate(1000000, 1, 1) == True

assert isValidDate(2015, 4, 31) == False

assert isValidDate(1970, 5, 99) == False

assert isValidDate(1981, 0, 3) == False

assert isValidDate(1666, 4, 0) == False

import datetime

d = datetime.date(1970, 1, 1)

oneDay = datetime.timedelta(days=1)

for i in range(1000000):

    assert isValidDate(d.year, d.month, d.day) == True

    d += oneDay