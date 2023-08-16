"""Exercise Description

Write a getHoursMinutesSeconds() function that has a totalSeconds parameter. 
The argument for this parameter will be the number of seconds to be translated into the number of hours, minutes, and seconds. 
If the amount for the hours, minutes, or seconds is zero, don’t show it: the function should return '10m' rather than '0h 10m 0s'. 
The only exception is that getHoursMinutesSeconds(0) should return '0s'.

These Python assert statements stop the program if their condition is False. Copy them to the bottom of your solution program. 
Your solution is correct if the following assert statements’ conditions are all True:

assert getHoursMinutesSeconds(30) == '30s'

assert getHoursMinutesSeconds(60) == '1m'

assert getHoursMinutesSeconds(90) == '1m 30s'

assert getHoursMinutesSeconds(3600) == '1h'

assert getHoursMinutesSeconds(3601) == '1h 1s'

assert getHoursMinutesSeconds(3661) == '1h 1m 1s'

assert getHoursMinutesSeconds(90042) == '25h 42s'

assert getHoursMinutesSeconds(0) == '0s'

 

For an additional challenge, break up 24 hour periods into days with a “d” suffix. For example, getHoursMinutesSeconds(90042) would return '1d 1h 42s'.

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: join(), append(), lists, string concatenation, while loops"""

def getHoursMinutesSeconds(seconds):

    if seconds == 0:
        return f'{seconds}s'
    
    hours = 0
    while seconds >= 3600:
        hours += 1
        seconds -= 3600
    
    minutes = 0
    while seconds >= 60:
        minutes += 1
        seconds -= 60
    
    reminding_seconds = seconds

    hour_min_sec = []

    if hours > 0:
        hour_min_sec.append(str(hours) + 'h')
    if minutes > 0:
        hour_min_sec.append(str(minutes) + 'm')
    if reminding_seconds > 0:
        hour_min_sec.append(str(reminding_seconds) + 's')

    return " ".join(hour_min_sec)  
   


assert getHoursMinutesSeconds(30) == '30s'

assert getHoursMinutesSeconds(60) == '1m'

assert getHoursMinutesSeconds(90) == '1m 30s'

assert getHoursMinutesSeconds(3600) == '1h'

assert getHoursMinutesSeconds(3601) == '1h 1s'

assert getHoursMinutesSeconds(3661) == '1h 1m 1s'

assert getHoursMinutesSeconds(90042) == '25h 42s'

assert getHoursMinutesSeconds(0) == '0s'
    
