"""
Ky Kartchner
CS 1400-1
Assignment 9

task1.py: Draws an initial smiley face and then displays a menu of commands. The face is then modified based on user input.
"""

import turtle


class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__dark_eyes = True

    def __draw_head(self):
        self.__face_color = "yellow" if self.__happy else "red"
        turtle.penup()
        turtle.setheading(0)
        turtle.goto(0, -100)
        turtle.pensize(2)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor(self.__face_color)
        turtle.circle(100)
        turtle.end_fill()
        turtle.penup()

    def __draw_eyes(self):
        self.__eye_color = "black" if self.__dark_eyes else "blue"

        turtle.penup()                                      # Left eye
        turtle.goto(-25, 25)
        turtle.begin_fill()
        turtle.fillcolor(self.__eye_color)
        turtle.circle(10)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(25, 25)                                 # Right eye
        turtle.begin_fill()
        turtle.fillcolor(self.__eye_color)
        turtle.circle(10)
        turtle.end_fill()
        turtle.penup()

    def __draw_mouth(self):
        turtle.penup()
        if self.__smile:
            turtle.goto(-50, -50)
            turtle.right(45)
            turtle.pensize(6.5)
            turtle.pendown()
            turtle.circle(75, 90)
            turtle.penup()
        else:
            turtle.goto(50, -50)
            turtle.right(225)
            turtle.pensize(6.5)
            turtle.pendown()
            turtle.circle(75, 90)
            turtle.penup()

    def draw_face(self):
        turtle.clear()
        self.__draw_head()
        self.__draw_eyes()
        self.__draw_mouth()

    def is_smile(self):
        return self.__smile

    def is_happy(self):
        return self.__happy

    def is_dark_eyes(self):
        return self.__dark_eyes

    def change_mouth(self):
        self.__smile = not self.__smile
        self.draw_face()

    def change_emotion(self):
        self.__happy = not self.__happy
        self.draw_face()

    def change_eyes(self):
        self.__dark_eyes = not self.__dark_eyes
        self.draw_face()


def main():
    face = Face()
    face.draw_face()

    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" if face.is_smile() else "smile"
        emotion = "angry" if face.is_happy() else "happy"
        eyes = "blue" if face.is_dark_eyes() else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.change_mouth()
        elif menu == 2:
            face.change_emotion()
        elif menu == 3:
            face.change_eyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


main()
