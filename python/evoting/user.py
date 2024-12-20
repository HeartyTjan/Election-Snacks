import re


class User:

    def __init__(self, name, phone_number, email):
        self.__name = name
        self.__phone_number = phone_number
        self.__email = email

    def get_name(self):
        return self.__name

    # def validate_name(self, name):
    #     name_pattern = "^[A-Za-z'-]+(?: [A-Za-z'-]+)*$"
    #     if not re.match(name, name_pattern):
    #         raise ValueError("Enter a valid name")
    #
    #     if len(name) == 0:
    #         return "Name cannot be empty"
    #     else:
    #         self.__name = name
    #         return self.__name

    def get_phone_number(self):
        return self.__phone_number

    def get_email(self):
        return self.__email
