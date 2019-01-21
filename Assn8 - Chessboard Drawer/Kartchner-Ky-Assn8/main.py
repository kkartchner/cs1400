"""
Ky Kartchner
CS 1400-1
Assignment 8

main: Prompts the user for starting x/y coordinates and dimensions (width and height) and then uses the provided
information and functions found in chessboard.py to draw a chessboard using the turtle module
"""

import turtle
from chessboard import draw_chessboard

# Prompt user for starting location (x, y)
start_x, start_y = eval(input("Enter starting location (x, y): "))
# start_x, start_y = 0, 0

# Prompt user for height and width of the board (set to default value of 250 if left blank)
width = input("Enter width of board: ")
height = input("Enter height of board: ")
# width = height = ""

# Use this information to draw a single 8x8 chessboard (might not be square)
turtle.showturtle()
turtle.speed(0)
turtle.shape("turtle")

print("\nOpening turtle...")


def main():
    if width == "" and height == "":
        draw_chessboard(start_x, start_y)
    elif height == "":
        draw_chessboard(start_x, start_y, width=eval(width))
    elif width == "":
        draw_chessboard(start_x, start_y, height=eval(height))
    else:
        draw_chessboard(start_x, start_y, eval(width), eval(height))

    turtle.hideturtle()
    turtle.done()


main()
