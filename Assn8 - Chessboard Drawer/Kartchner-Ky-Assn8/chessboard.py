"""
Ky Kartchner
CS 1400-1
Assignment 8

chessboard.py: Provides the functions used in main.py for drawing a chessboard at the specified position with the
specified width and height.
"""

import turtle


# Draws the chess board outline then calls draw_all_squares():
def draw_chessboard(start_x, start_y, width=250, height=250):
    square_width, square_height = width / 8, height / 8         # Calculate dimension of an individual square

    draw_square(start_x, start_y, width, height, pen_color="red")     # Draw board outline

    draw_all_squares(start_x, start_y, square_width, square_height)   # Draw all black squares
    draw_all_squares(start_x + square_width, start_y + square_height, square_width, square_height)
    return


# Draws all of the black squares by calling draw_square() many times:
def draw_all_squares(start_x, start_y, square_width, square_height):
    for y in range(4):
        offset_y = square_height * y * 2
        for x in range(4):
            offset_x = square_width * x * 2
            draw_square(start_x + offset_x, start_y + offset_y, square_width, square_height, "black")
    return


# Draws a single black square:
def	draw_square(pos_x, pos_y, width, height, fill_color="", pen_color="black"):
    turtle.penup()
    turtle.pencolor(pen_color)
    turtle.setposition(pos_x, pos_y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(fill_color)

    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()
    turtle.penup()
    return
