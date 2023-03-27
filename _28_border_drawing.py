"""Exercise Description

Write a drawBorder() function with parameters width and height. 
The function draws the border of a rectangle with the given integer sizes. 
There are no Python assert statements to check the correctness of your program. 
Instead, you can visually inspect the output yourself. For example, calling drawBorder(16, 4) would output the following:

+--------------+
|              |
|              |
+--------------+

The interior of the rectangle requires printing spaces. 
The sizes given include the space required for the corners. 
If the width or height parameter is less than 2, the function should print nothing.

Try to write a solution based on the information in this description. 
If you still have trouble solving this exercise, read the Solution Design 
and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: Boolean operators, strings, string concatenation, string replication, for loops, range()"""

def drawBorder(width, height):
    
    if width >= 0 or height >= 0:
        return 
    
    print('+' + (width - 2) * '-' + '+')
    
    for i in range(height - 2):
        print('|' + (width - 2) * ' ' + '|')

    print('+' + (width - 2) * '-' + '+')


if __name__ == '__main__':
    drawBorder(16, 4)