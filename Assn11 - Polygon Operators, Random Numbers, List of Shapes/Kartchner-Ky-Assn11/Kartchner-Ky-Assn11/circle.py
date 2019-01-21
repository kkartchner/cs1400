"""
Ky Kartchner
CS 1400-1
Assignment 11

circle.py: Contains definitions for the Circle class to be used in task3.
"""


import turtle
from math import pi


class Circle:
    def __init__(self, center_x, center_y, radius, color):
        self.__center_x = center_x
        self.__center_y = center_y
        self.__radius = radius
        self.__color = color
        self.__area = pi * radius**2

    def draw(self):
        turtle.penup()
        turtle.goto(self.__center_x, self.__center_y)
        turtle.begin_fill()
        turtle.fillcolor(self.__color)
        turtle.circle(self.__radius)
        turtle.end_fill()
        return

    def get_area(self):
        return self.__area

    def get_color_code(self):
        return {"red": 0, "yellow": 1, "blue": 2, "green": 3}.get(self.__color)

    @staticmethod
    def show_create_menu():
        print("\nENTER CIRCLE")
        pos_x, pos_y = eval(input("Enter the position (x, y): "))

        user_input = input("Enter the radius: ")
        while not user_input.isdigit():
            print("Invalid input. Radius must be a number!\n")
            user_input = input("Enter the radius: ")
        radius = eval(user_input)

        center_x = pos_x
        center_y = pos_y - radius

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

        print("Circle created successfully!")

        return Circle(center_x, center_y, radius, color)
