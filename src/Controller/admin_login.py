import maskpass
from src.Model.database import Database
from src.View.view_details import ViewDetails
from src.Controller.validation import AuthValidation

class Admin:
    def __init__(self):
        self.db = Database()
        self.view = ViewDetails()

    def check_login(self, email, password):
        query = 'SELECT COUNT(*) FROM admin WHERE email=? AND password=?'
        result = self.db.execute_select(query, (email, password))
        return result[0][0] > 0

    def admin_login(self):
        while True:
            email = self.get_valid_email()
            password = str(maskpass.askpass(prompt='Password: ', mask="*"))

            if self.check_login(email, password):
                print('-----------------------------------Logged in successfully!---------------------------------\n')
                self.view.choice_view()
                break
            else:
                print("Sorry, you aren't signed up yet.")
        
    def get_valid_email(self):
        while True:
            email = str(input('Email: '))
            if AuthValidation.validate_email(email):
                return email
            else:
                print("Please enter a valid email")