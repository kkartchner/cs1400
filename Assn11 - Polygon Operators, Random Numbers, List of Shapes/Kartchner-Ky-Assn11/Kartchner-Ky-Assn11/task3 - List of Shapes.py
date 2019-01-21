"""
Ky Kartchner:
CS 1400-1
Assignment 11

task3: Utilizes the Circle and Rectangle classes allowing the user to create, sort, and draw shapes.
"""

import turtle
from circle import Circle
from rectangle import Rectangle

shapes_original = []
shapes_copy = shapes_original.copy()


def sort_by_area(element):
    return element.get_area()


def sort_by_color(element):
    return element.get_color_code()


command = 0
while command != 5:
    print("MAIN MENU",
          "1) Enter Circle",
          "2) Enter Rectangle",
          "3) Sort Shapes",
          "4) Draw Shapes",
          "5) Exit", sep="\n")

    command = eval(input("Enter a command: "))

    if command == 1:
        shapes_original.append(Circle.show_create_menu())                 # show circle menu
        shapes_copy = shapes_original.copy()
    elif command == 2:
        shapes_original.append(Rectangle.show_create_menu())              # show rectangle menu
        shapes_copy = shapes_original.copy()
    elif command == 3:
        if len(shapes_original) == 0:
            print("No shapes have been entered! Use the commands above to enter some.")
        else:
            command_2 = 0                                                     # show sort menu
            while not command_2:
                print("\nSORT SHAPES",
                      "1) By area (ascending)",
                      "2) By area (descending)",
                      "3) By color",
                      "4) By original input order", sep="\n")
                command_2 = eval(input("Enter a command: "))
                if command_2 == 1:
                    shapes_copy.sort(key=sort_by_area)
                    print("Sorting by area (ascending)")
                elif command_2 == 2:
                    shapes_copy.sort(key=sort_by_area, reverse=True)
                    print("Sorting by area (descending)")
                elif command_2 == 3:
                    print_order = []
                    print("\nSORT BY COLOR",
                          "0-Red, 1-Yellow, 2-Blue, 3-Green:", sep="\n")

                    print_order = eval(input("Enter order to draw color groups i.e. (0,2,3,1): "))

                    shapes_copy.sort(key=sort_by_color)
                    temp_list = []
                    for i in range(0, 4):
                        for shape in shapes_copy:
                            if shape.get_color_code() == print_order[i]:
                                temp_list.append(shape)

                    shapes_copy = temp_list.copy()

                    print("Sorting by color")
                elif command_2 == 4:
                    shapes_copy = shapes_original.copy()
                    print("Sorting by original input order.")
                else:
                    command_2 = 0
                    print("Invalid command. Enter a number between 1 and 4 only.\n")
    elif command == 4:
        if len(shapes_original) == 0:
            print("No shapes have been entered! Use the commands above to enter some.")
        else:
            turtle.clear()
            turtle.showturtle()
            print("Opening turtle...")
            for shape in shapes_copy:                         # draw shapes
                shape.draw()
    elif command != 5:
        print("Invalid command. Enter a number between 1 and 5 only.")
    else:
        print("Exiting program...")

    print("")

turtle.hideturtle()
