"""
Ky Kartchner
CS 1400-1
Assignment 11

circle.py: Contains definitions for the Rectangle class to be used in task3.
"""
import turtle


class Rectangle:
    def __init__(self, lower_left_x, lower_left_y, height, width, color):
        self.__lower_left_x = lower_left_x
        self.__lower_left_y = lower_left_y
        self.__height = height
        self.__width = width
        self.__color = color
        self.__area = width * height

    def draw(self):
        turtle.penup()
        turtle.goto(self.__lower_left_x, self.__lower_left_y)
        turtle.begin_fill()
        turtle.fillcolor(self.__color)
        for times in range(0, 2):
            turtle.forward(self.__width)
            turtle.left(90)
            turtle.forward(self.__height)
            turtle.left(90)

        turtle.end_fill()
        return

    def get_area(self):
        return self.__area

    def get_color_code(self):
        return {"red": 0, "yellow": 1, "blue": 2, "green": 3}.get(self.__color)

    @staticmethod
    def show_create_menu():
        print("\nENTER RECTANGLE")
        lower_left_x, lower_left_y = eval(input("Enter the position (x, y): "))
        user_input = input("Enter the height: ")
        while not user_input.isdigit():
            print("Invalid input. Height must be a number!\n")
            user_input = input("Enter the height: ")
        height = eval(user_input)

        user_input = input("Enter the width: ")
        while not user_input.isdigit():
            print("Invalid input. Width must be a number!\n")
            user_input = input("Enter the width: ")
        width = eval(user_input)

        color = "Invalid"
        while color == "Invalid":
            user_input = input("Enter the fill color (0-Red, 1-Yellow, 2-Blue, 3-Green): ")
            if not user_input.isdigit():
                print("Invalid input. Must enter a number between 0 and 3.\n")
                continue
            color_code = eval(user_input)
            color = {0: "red", 1: "yellow", 2: "blue", 3: "green"}.get(color_code, "Invalid")
            if color == "Invalid":
                print("Invalid input. Must enter a number between 0 and 3.\n")

        print("Rectangle created successfully!")

        return Rectangle(lower_left_x, lower_left_y, height, width, color)
