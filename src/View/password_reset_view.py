import re
import maskpass
from src.Model.database import Database

class PasswordResetView:
    @staticmethod
    def get_valid_email():
        while True:
            email = input("Enter Your Email: ")
            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if re.fullmatch(email_regex, email):
                return email
            else:
                print("Please Check Your Email")

    @staticmethod
    def get_valid_password():
        while True:
            pwd_reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
            pwd_cmp = re.compile(pwd_reg)
            new_password = str(maskpass.askpass(prompt='Enter New Password: ', mask="*"))
            if re.search(pwd_cmp, new_password):
                return new_password
            else:
                print("Please Enter Password correctly")

    @staticmethod
    def display_password_change_success():
        print('Password changed successfully!')

    @staticmethod
    def display_email_not_registered():
        print("Email Has Not Registered")
