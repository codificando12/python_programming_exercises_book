"""Write a drawBox() function with a size parameter. The size parameter contains an integer for the width, length, and height of the box. 
The horizontal lines are drawn with - dash characters, the vertical lines with | pipe characters, and the diagonal lines with / forward slash characters. 
The corners of the box are drawn with + plus signs.

There are no Python assert statements to check the correctness of your program. Instead, you can visually inspect the output yourself. 
For example, calling drawBox(1) through drawBox(5) would output the following boxes, respectively"""

def drawBox(width, length_height):
    h_line = "-"
    v_line = "|"
    d_line = "/"
    corner = "+"

    first_lenght = length_height
    top_border = " " * (length_height + 1)+ corner + (width) * h_line + corner
    second_line = " " * (length_height) + d_line + " " * (width) + d_line + v_line
    print(top_border)
    print(second_line)
    space = 1
    for i in range(1, length_height):
        print(" " * (first_lenght - 1) + d_line + " " * (width) + d_line + " " * space + v_line)
        first_lenght -= 1
        space += 1
    print(corner + (width) * h_line + corner + " " * (length_height) + corner)
    space = length_height - 1
    for i in range( length_height):
        print(v_line + " " * (width) + v_line + " " * space + d_line)
        space -= 1
    print(corner + (width) * h_line + corner)
if __name__ == "__main__":
    drawBox(8, 5)