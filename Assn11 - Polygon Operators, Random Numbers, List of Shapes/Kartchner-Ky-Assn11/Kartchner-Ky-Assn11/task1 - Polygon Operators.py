"""
Ky Kartchner
CS 1400-1
Assignment 11

task1: Defines a class called Polygon with overridden operators, prompts the user to enter the number of sides for
two polygons and uses this information to create instances of the Polygon class, and then prints the result of using the
operators +, -, <, >, ==, and len() and str() between the two polygons.
"""

class Polygon:
    def __init__(self, side_count):
        self.__side_count = side_count

    def __add__(self, other):
        return self.__side_count + other.__side_count

    def __sub__(self, other):
        return self.__side_count - other.__side_count

    def __lt__(self, other):
        return self.__side_count < other.__side_count

    def __gt(self, other):
        return self.__side_count > other.__side_count

    def __eq__(self, other):
        return self.__side_count == other.__side_count

    def __len__(self):
        return self.__side_count

    def __str__(self):
        return str(self.__side_count)


def main():
    poly1 = Polygon(eval(input("Enter number of sides for polygon1: ")))
    poly2 = Polygon(eval(input("Enter number of sides for polygon2: ")))

    poly_sum = poly1 + poly2
    poly_difference1 = poly1 - poly2
    poly_difference2 = poly2 - poly1

    print("poly1 + poly2 =", poly_sum)
    print("poly1 - poly2 =", poly_difference1)
    print("poly2 - poly2 =", poly_difference2)
    print("poly1 < poly2 ?", poly1 < poly2)
    print("poly1 > poly2 ?", poly1 > poly2)
    print("poly1 == poly2 ?", poly1 == poly2)
    print("len(poly1) :", len(poly1))
    print("len(poly2) :", len(poly2))
    print("str(poly1) :", str(poly1))
    print("str(poly2) :", str(poly2))


main()
