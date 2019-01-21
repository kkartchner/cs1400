"""
Ky Kartchner
CS 1400 - 1
Assignment 3

task1: Draws an epic snowman using the turtle module.
"""
import turtle
turtle.showturtle()
turtle.shape("turtle")
turtle.pensize(2)

turtle.penup()                          # Draw head
turtle.setposition(0, 150)
turtle.pendown()
turtle.circle(75)

turtle.penup()                          # Draw hat
turtle.setposition(-100, 262.5)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#800020")                 # Burgundy color fill
turtle.forward(200)
turtle.left(90)
turtle.forward(15)
turtle.left(90)
turtle.forward(42.5)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(115)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(42.5)
turtle.left(90)
turtle.forward(15)
turtle.end_fill()
turtle.setheading(0)

turtle.penup()                          # Draw left eye
turtle.setposition(-26, 225)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(10)
turtle.end_fill()

turtle.penup()                          # Draw right eye
turtle.setposition(26, 225)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(10)
turtle.end_fill()

turtle.penup()                          # Draw torso
turtle.setposition(0, -50)
turtle.pendown()
turtle.circle(100)

turtle.penup()                          # Draw right arm
turtle.setposition(-88, 102)
turtle.right(35)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#d67e2b")                 # Brown color fill
turtle.circle(5, 180)
turtle.forward(125)
turtle.right(90)                            # Thumb
turtle.forward(25)
turtle.circle(3, 180)
turtle.forward(25)
turtle.right(90)                            # Finger 1
turtle.forward(25)
turtle.circle(3, 180)
turtle.forward(25)
turtle.right(135)                           # Finger 2
turtle.forward(25)
turtle.circle(3, 180)
turtle.forward(25)
turtle.right(45)
turtle.forward(127)
turtle.setheading(0)
turtle.end_fill()

turtle.penup()                          # Draw left arm
turtle.setposition(88, 102)
turtle.setheading(0)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#d67e2b")                 # Brown color fill
turtle.circle(5, 180)
turtle.forward(125)
turtle.right(90)                            # Thumb
turtle.forward(25)
turtle.circle(3, 180)
turtle.forward(25)
turtle.right(90)                            # Finger 1
turtle.forward(25)
turtle.circle(3, 180)
turtle.forward(25)
turtle.right(135)                           # Finger 2
turtle.forward(25)
turtle.circle(3, 180)
turtle.forward(25)
turtle.right(45)
turtle.forward(127)
turtle.setheading(0)
turtle.end_fill()

turtle.penup()                          # Draw top button
turtle.setposition(0, 75)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("red")
turtle.circle(10)
turtle.end_fill()

turtle.penup()                          # Draw middle button
turtle.setposition(0, 50)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("green")
turtle.circle(10)
turtle.end_fill()

turtle.penup()                          # Draw bottom button
turtle.setposition(0, 25)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("blue")
turtle.circle(10)
turtle.end_fill()

turtle.penup()                          # Draw base
turtle.setposition(0, -300)
turtle.pendown()
turtle.circle(125)

turtle.penup()                          # Mouth pebble 1
turtle.setposition(-40, 180)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(6)
turtle.end_fill()

turtle.penup()                          # Mouth pebble 2
turtle.setposition(-30, 170)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(6)
turtle.end_fill()

turtle.penup()                          # Mouth pebble 3
turtle.setposition(-15, 165)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(6)
turtle.end_fill()

turtle.penup()                          # Mouth pebble 4
turtle.setposition(0, 165)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(6)
turtle.end_fill()

turtle.penup()                          # Mouth pebble 5
turtle.setposition(15, 165)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(6)
turtle.end_fill()

turtle.penup()                          # Mouth pebble 6
turtle.setposition(30, 170)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(6)
turtle.end_fill()

turtle.penup()                          # Mouth pebble 7
turtle.setposition(40, 180)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(6)
turtle.end_fill()


turtle.hideturtle()

turtle.done()