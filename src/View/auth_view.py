from sys import exit
import maskpass
from src.Controller.validation import AuthValidation

class AuthView:
    @staticmethod
    def get_email():
        while True:
            email = input('Email: ')
            if AuthValidation.validate_email(email):
                return email
            else:
                print("Please enter a valid email")

    @staticmethod
    def get_password():
        while True:
            password = maskpass.askpass(prompt='Password: ', mask="*")
            if AuthValidation.validate_password(password):
                return password
            else:
                print("Please enter a valid password")

    @staticmethod
    def get_repeated_password():
        while True:
            re_password = maskpass.askpass(prompt='Re-Enter Password: ', mask="*")
            if AuthValidation.validate_password(re_password):
                return re_password
            else:
                print("Please enter a valid password")

    @staticmethod
    def get_phone_number():
        while True:
            phone_number = input('Ph_No: ')
            if AuthValidation.validate_phone_number(phone_number):
                return phone_number
            else:
                print("Please enter a valid phone number")

    @staticmethod
    def display_logged_in_successfully():
        print('-----------------------------------Logged in successfully!---------------------------------\n')
        print('                              *********Booking Details*********                            ')

    @staticmethod
    def display_not_signed_up():
        print("Sorry, you aren't signed up yet.")

    @staticmethod
    def display_password_mismatch():
        print("Password does not match")

    @staticmethod
    def display_invalid_email_password():
        print("Please enter a valid email, password, and phone number")
