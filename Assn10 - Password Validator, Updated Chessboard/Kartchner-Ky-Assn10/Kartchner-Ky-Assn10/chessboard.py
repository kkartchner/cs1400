"""
Ky Kartchner
CS 1400-1
Assignment 10

chessboard.py: Provides the chessboard class and functions used in main.py for drawing a chessboard at the specified
position with the specified width and height.
"""

import turtle


class Chessboard:
    def __init__(self, start_x, start_y, width=250, height=250):
        self.__start_x = start_x
        self.__start_y = start_y
        self.__width = width
        self.__height = height

        turtle.speed(0)

    # Draws the chess board outline then calls draw_all_squares():
    def draw(self):
        # Calculate dimension of an individual square
        square_width, square_height = self.__width / 8, self.__height / 8

        # Draw board outline
        Chessboard.__draw_square(self.__start_x, self.__start_y, self.__width, self.__height, pen_color="red")

        # Draw all black squares
        Chessboard.__draw_all_squares(self.__start_x, self.__start_y, square_width, square_height)
        Chessboard.__draw_all_squares(self.__start_x + square_width, self.__start_y + square_height,
                                      square_width, square_height)
        return

    # Draws all of the black squares by calling draw_square() many times:
    @staticmethod
    def __draw_all_squares(start_x, start_y, square_width, square_height):
        for y in range(4):
            offset_y = square_height * y * 2
            for x in range(4):
                offset_x = square_width * x * 2
                Chessboard.__draw_square(start_x + offset_x, start_y + offset_y,
                                         square_width, square_height, fill_color = "black")
        return

    # Draws a single black square:
    @staticmethod
    def __draw_square(pos_x, pos_y, width, height, fill_color="", pen_color="black"):
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

