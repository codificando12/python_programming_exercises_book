"""Exercise Description

Write a drawRectangle() function with two integer parameters: width and height. 
The function doesn’t return any values but rather prints a rectangle with the given number of hashtags in the 
horizontal and vertical directions.

There are no Python assert statements to check the correctness of your program. 
Instead, you can visually inspect the output yourself. For example, calling drawRectangle(10, 4) 
should produce the following output:

##########

##########

##########

##########

If either the width or height parameter is 0 or a negative number, the function should print nothing.

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, 
read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: for loops, range(), print(), end keyword argument for print()"""

def drawRectangle(width, height):
    if height <= 0 or width <= 0:
        print("The rectangle can't be drawn")
    else: 

        for i in range(height):
            print('#' * width)

if __name__ == '__main__':
    drawRectangle(-1, 4)
