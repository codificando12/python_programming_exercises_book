"""Write a getChessSquareColor() function that has parameters column and row. 
The function either returns 'black' or 'white' depending on the color at the specified column and row. 
Chess boards are 8 x 8 spaces in size, and the columns and rows in this program begin at 0 and end at 7 like in Figure 9-1. 
If the arguments for column or row are outside the 0 to 7 range, the function returns a blank string."""

def getChessSquareColor(height, width):

    if height > 7 or width > 7:
        return ''
    elif height == 0 and width == 0:
        return "white"
    elif height % 2 == width % 2:
        return "white"
    else: 
        return "black"

assert getChessSquareColor(0, 0) == 'white'

assert getChessSquareColor(1, 0) == 'black'

assert getChessSquareColor(0, 1) == 'black'

assert getChessSquareColor(7, 7) == 'white'

assert getChessSquareColor(0, 8) == ''

assert getChessSquareColor(2, 9) == ''