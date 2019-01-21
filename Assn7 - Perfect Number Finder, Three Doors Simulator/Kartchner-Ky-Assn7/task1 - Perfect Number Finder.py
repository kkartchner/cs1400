"""
Ky Kartchner
CS 1400-1
Assignment 7

task1: Finds and prints the first 4 perfect numbers that are less than 10,000.
"""
import time
inner_loop_iterations = 0
found_perfect_numbers = 0
start_time = time.time()

for number in range(2, 10000):
    divisor_sum = 1                       # Every number has 1 as a divisor so the divisor sum will be at least 1

    #  A number's second highest possible divisor will be less than half itself plus 1
    divisor_cap = int(number / 2) + 1

    test_divisor = 0
    for test_divisor in range(2, divisor_cap):
        if number % test_divisor == 0:                 # If test_divisor is a divisor of num
            divisor_sum += test_divisor                # Add it to the divisor_sum
        if divisor_sum > number:                       # No need to continue if divisor_sum is greater than the number
            break

    inner_loop_iterations += test_divisor              # Add the number of inner iterations to total iterations

    if divisor_sum == number:                          # If the sum of the divisors equals the number
        found_perfect_numbers += 1                     # It's a perfect number so increment perfect numbers
        print(number, "is a perfect number\n")

    if found_perfect_numbers == 4:                     # Break once the first 4 perfect numbers have been found
        end_time = time.time()
        break

elapsed_time = end_time - start_time                            # Print results
print("Total runtime (seconds):", elapsed_time)
print("Total inner loop iterations:", inner_loop_iterations)

input("\nPress any key to exit")
