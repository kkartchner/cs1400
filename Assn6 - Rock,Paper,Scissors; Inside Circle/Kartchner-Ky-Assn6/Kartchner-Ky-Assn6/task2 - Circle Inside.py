"""
Ky Kartchner
CS 1400-1
Assignment 6

task2: Prompts user to enter the x and y coordinates and radius of two circles, and prints if one circle is inside
another, if they intersect, or if they don't intersect.
"""

import math

x1, y1, radius1 = eval(input("Enter circle1's center x-y coordinates and radius (x, y, radius): "))
x2, y2, radius2 = eval(input("Enter circle2's center x-y coordinates and radius (x, y, radius): "))

distance_between_centers = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
output = ""

if distance_between_centers <= abs(radius1 - radius2):
    if radius1 > radius2:
        output = "circle2 is inside circle1"
    elif radius1 < radius2:
        output = "circle1 is inside circle2"
    else:
        output = "circle1 and circle2 have the same radius and location"
elif distance_between_centers <= radius1 + radius2:
    output = "circle2 overlaps circle1"
else:
    output = "circle2 does not overlap circle1"

print("\n" + output)

input("\nPress any key to exit")


