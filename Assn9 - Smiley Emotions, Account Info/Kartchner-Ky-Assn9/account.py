"""
Ky Kartchner
CS 1400-1
Assignment 9

account.py: Contains the account class that is used by task2.py to keep track of user account information.
"""


class Account:
    def __init__(self, id=0, balance=100, annual_interest_rate=0):
        self.__id = id
        self.__balance = balance
        self.__annual_interest_rate = annual_interest_rate

    def get_monthly_interest_rate(self):
        return self.__annual_interest_rate / 12

    def get_monthly_interest(self):
        return self.get_monthly_interest_rate() * self.__balance

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    # ID
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    # Balance
    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    # Annual Interest Rate
    def get_annual_interest_rate(self):
        return self.__annual_interest_rate

    def set_annual_interest_rate(self, annual_interest_rate):
        self.__annual_interest_rate = annual_interest_rate
