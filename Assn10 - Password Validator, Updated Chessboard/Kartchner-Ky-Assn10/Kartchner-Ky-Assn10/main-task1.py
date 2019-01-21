import turtle
from chessboard import Chessboard


def main():
    start_x, start_y = eval(input("Enter a starting point: "))
    width = input("Input a width: ")
    height = input("Input a height: ")

    if width == "" and height == "":
        chessboard = Chessboard(start_x, start_y)
    elif height == "":
        chessboard = Chessboard(start_x, start_y, width=eval(width))
    elif width == "":
        chessboard = Chessboard(start_x, start_y, height=eval(height))
    else:
        chessboard = Chessboard(start_x, start_y, eval(width), eval(height))

    chessboard.draw()

    turtle.hideturtle()
    turtle.done()


main()