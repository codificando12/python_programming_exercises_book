"""Write a drawBox() function with a size parameter. The size parameter contains an integer for the width, length, and height of the box. 
The horizontal lines are drawn with - dash characters, the vertical lines with | pipe characters, and the diagonal lines with / forward slash characters. 
The corners of the box are drawn with + plus signs.

There are no Python assert statements to check the correctness of your program. Instead, you can visually inspect the output yourself. 
For example, calling drawBox(1) through drawBox(5) would output the following boxes, respectively"""

def drawBox(width, length, height):
    h_line = "-"
    v_line = "|"
    d_line = "/"
    corner = "+"

    top_border = " " * (length + 1)+ corner + (width - 2) * h_line + corner
    second_line = " " * length + d_line + " " * (width - 2) + d_line + v_line
    print(top_border)
    print(second_line)
    space = 1
    for i in range(length - 1):
        print(" " * (length - 1) + d_line + " " * (width - 2) + d_line + " " * space + v_line)
        length -= 1
        space += 1
    print(corner + (width - 2) * h_line + corner)
if __name__ == "__main__":
    drawBox(4, 2, 0)