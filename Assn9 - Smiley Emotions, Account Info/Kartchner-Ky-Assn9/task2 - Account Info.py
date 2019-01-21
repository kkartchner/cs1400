"""
Ky Kartchner
CS 1400-1
Assignment 9

task2.py: Prompts the user to enter account id, balance, and annual interest rate, then displays account action menu.
"""

from account import Account

account_created = False
while not account_created:
    print("CREATE NEW ACCOUNT")
    id_number = eval(input("Enter user id number: "))
    balance = eval(input("Enter current balance: "))
    if balance < 0:
        print("Invalid input. Balance must be a positive number.\n")
        continue

    annual_interest_rate = eval(input("Enter annual interest rate (%): "))
    if annual_interest_rate > 10:
        print("Invalid input. Annual interest rate must not be greater than 10%.\n")
    else:
        annual_interest_rate /= 100
        account_created = True


account = Account(id_number, balance, annual_interest_rate)

command = 0
while not command == 8:
    print("\nMAIN MENU",
          "(1): Display ID",
          "(2): Display Balance",
          "(3): Display Annual Interest Rate",
          "(4): Display Monthly Interest Rate",
          "(5): Display Monthly Interest",
          "(6): Withdraw Money",
          "(7): Deposit Money",
          "(8): Exit", sep="\n")

    command = eval(input("Enter a command: "))

    if command == 1:
        print("ID is", account.get_id())
    elif command == 2:
        print("Current balance is: $" + format(account.get_balance(), ".2f"))
    elif command == 3:
        print("Annual interest rate is: ", format(account.get_annual_interest_rate(), "%"))
    elif command == 4:
        print("Monthly interest rate is: ", format(account.get_monthly_interest_rate(), "%"))
    elif command == 5:
        print("Monthly interest is: $" + format(account.get_monthly_interest(), ".2f"))
    elif command == 6:
        amount = eval(input("Enter amount to withdraw: "))
        account.withdraw(amount)
        print("You withdrew $" + str(amount),
              "New balance is: $" + format(account.get_balance(), ".2f"), sep="\n")
    elif command == 7:
        amount = eval(input("Enter amount to deposit: "))
        account.deposit(amount)
        print("You deposited $" + str(amount),
              "New balance is: $" + format(account.get_balance(), ".2f"), sep="\n")
    elif command == 8:
        print("Exiting now...")
    else:
        print("Invalid command. Please enter between 1 and 8 only.")

