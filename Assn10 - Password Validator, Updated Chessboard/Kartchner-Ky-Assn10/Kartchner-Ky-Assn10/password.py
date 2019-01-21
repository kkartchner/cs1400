"""
Ky Kartchner
CS 1400-1
Assignment 10

password.py: Contains the definition of the password class used in task2.py. 
"""

class Password:
    def __init__(self, password):
        self.__value = ""
        self.__value_to_check = password
        self.__error_message = ""
        self.__is_valid = True

        self.set_value(password)

    def set_value(self, password):
        self.__value_to_check = password
        if self.is_valid(password):
            self.__value = password
            print("valid password\n")
        else:
            print("invalid password\n")
            print(self.get_error_message())

    def get_error_message(self):
        return self.__error_message

    def is_valid(self, password):
        self.__value_to_check = password
        self.__is_valid = True
        self.__error_message = ""

        self.__check_length()
        self.__check_alpha_numeric()
        self.__check_number_of_digits()
        self.__check_if_contains_password()
        self.__check_if_ends_with_123()

        return self.__is_valid

    def __check_length(self):
        if len(self.__value_to_check) < 8:
            self.__error_message += "Password must have at least 8 characters\n"
            self.__is_valid = False

    def __check_alpha_numeric(self):
        if not self.__value_to_check.isalnum():
            self.__error_message += "Password must only consist of letters and digits\n"
            self.__is_valid = False

    def __check_number_of_digits(self):
        number_of_digits = 0
        for char in self.__value_to_check:
            if str(char).isdigit():
                number_of_digits += 1

        if number_of_digits < 2:
            self.__error_message += "Password must contain at least two digits\n"
            self.__is_valid = False

    def __check_if_contains_password(self):
        if "password" in self.__value_to_check:
            self.__error_message += "Password cannot contain the word \"password\"\n"
            self.__is_valid = False

    def __check_if_ends_with_123(self):
        value = self.__value_to_check
        last_char = len(self.__value_to_check) - 1
        if value[last_char - 2] == "1" and value[last_char - 1] == "2" and value[last_char] == "3":
            self.__error_message += "Password cannot end with \"123\"\n"
            self.__is_valid = False





