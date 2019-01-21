"""
Ky Kartchner
CS 1400-1
Assignment 4

task2: Prompts the user for the location of the target center and for the radius of the bulls-eye, then draws the
target using the turtle module.
"""
import turtle

print("Welcome to the Archery range!")                                          # Get user input
print ("Enter the location for the center of the target and the radius of the bulls-eye:")
center_x = eval(input("X: "))
center_y = eval(input("Y: "))
center_radius = eval(input("Radius: "))
ring_radius = center_radius + 75

print("Opening turtle...")
turtle.showturtle()

turtle.penup()                                                          # Outermost ring
turtle.setposition(center_x, center_y - ring_radius)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(ring_radius)
turtle.end_fill()

ring_radius -= 25                                                       # 1st ring in from outermost
turtle.penup()
turtle.setposition(center_x, center_y - ring_radius)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("cyan")
turtle.circle(ring_radius)
turtle.end_fill()

ring_radius -= 25                                                       # 2nd ring in from outermost
turtle.penup()
turtle.setposition(center_x, center_y - ring_radius)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("red")
turtle.circle(ring_radius)
turtle.end_fill()

turtle.penup()                                                          # Bulls-eye
turtle.setposition(center_x, center_y - center_radius)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.circle(center_radius)
turtle.end_fill()

turtle.hideturtle()
turtle.done()
