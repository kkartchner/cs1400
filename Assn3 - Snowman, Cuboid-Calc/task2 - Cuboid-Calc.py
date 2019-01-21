"""
Ky Kartchner
CS 1400 - 1
Assignment 3

task2: Prompts the user to enter the dimensions of a cuboid and then calculates and prints its volume and surface area.
"""

print("Welcome to Cuboid-Calc!")                                            # Print program instructions
print("Enter the Cuboid's dimensions in feet:")

length = eval(input("Length: "))                                            # Get cuboid dimensions
width = eval(input("Width: "))
height = eval(input("Height: "))

volume = length * width * height                                            # Calculate volume (V = lwh)
surface_area = 2 * (length * width + width * height + height * length)      # Surface area = sum of each side's area

print("\nYour", length, "X", width, "X", height, "foot cuboid has the following:")             # Print results
print("Volume:", volume, "cubic feet")
print("Surface Area:", surface_area, "square feet")