"""Write a program that displays the time for every 15 minute interval from 12:00 am to 11:45 pm. Your solution should produce the following output:

12:00 am

12:15 am

12:30 am

12:45 am

1:00 am

1:15 am

--cut--

11:30 pm

11:45 pm

There are 96 lines in the full output.

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, 
read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: for loops, lists, nested loops, string concatenation"""


def run():

    am_pm = ['am', 'pm']
    time = ['12', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
    minutes = ['00', '15', '30', '45']
    
    for i in am_pm:
        for hour in time:
            for minute in minutes:
                print(f'{hour}:{minute} {i}')

if __name__ == '__main__':
    run()