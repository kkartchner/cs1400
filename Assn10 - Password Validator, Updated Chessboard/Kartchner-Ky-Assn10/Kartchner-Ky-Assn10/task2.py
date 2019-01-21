"""
Ky Kartchner
CS 1400-1
Assignment 10

task2.py: Prompts the user to enter a password and then utilizes the Password class to 
check for validity. Prints the validity of the password and then asks user if they
would like to enter another password. If yes, process repeats; if no, program exits.
"""

from password import Password


def main():
    print("NEW ACCOUNT:")
    password = Password(input("Enter account password: "))

    done = False
    while not done:
        command = input("Would you like to enter another password? (Y/N): ")
        if command == 'Y' or command == 'y':
            password.set_value(input("Enter account password: "))
        else:
            done = True
main()