def drawPyramid(heigh):
    num = 1

    for i in range(heigh):
        space = (heigh * 2 - num)//2
        print(" " * space + "#" * num)
        num += 2


if __name__ == "__main__":
    drawPyramid(9)