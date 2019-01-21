"""
Ky Kartchner
CS 1400-1
Assignment 11

task2: Randomly generates 1,000 integers between 0 and 9 then displays the count for each number.
"""

from random import randint

NUMBERS_TO_GENERATE = 1000
number_counts = []

for n in range(0, 10):
    number_counts.append(0)

print("Generating random integers between 0 and 9...")
for i in range(0, NUMBERS_TO_GENERATE):
    random_int = randint(0, 9)
    number_counts[random_int] += 1

print("Here is the count for each:")
for i in range(0, len(number_counts)):
    print(str(i) + "'s:", number_counts[i])

input("Press any key to exit")


