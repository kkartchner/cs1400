"""
Ky Kartchner
CS 1400-1
Assignment 4

task1: Reads in an investment amount, the annual interest rate, and the number of years, then displays the future
investment amount.
"""

print("Welcome to Invest-a-Calc!")
investment_amount = eval(input("Enter investment amount: ")) * 100                # Convert dollars to cents
monthly_interest_rate = (eval(input("Enter annual interest rate: ")) / 12) / 100  # Convert percentage to decimal
number_of_months = eval(input("Enter number of years: ")) * 12                    # Convert years to months

# Future investment amount in dollars:
future_investment_amount = int(investment_amount * ((1 + monthly_interest_rate) ** number_of_months)) / 100

print("\nFuture value is", future_investment_amount)

