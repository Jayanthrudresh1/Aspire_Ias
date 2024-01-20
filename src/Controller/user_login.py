from sys import exit
from src.View.auth_view import AuthView
from src.Model.database import Database
from src.Controller.change_password import PasswordReset
import src.Controller.booking as booking

def choice_method():
    print("-----------------------------------Welcome User--------------------------------------------")
    while True:
        print("Please Enter Choice Given \n1. Login\n2. Register\n3. Change Password\n4. Exit")
        try:
            choice = int(input("Enter Here: "))
        except:
            print("XXXXXX---Warning---XXXXXX\nPlease Follow The Instruction Correctly")
        else:
            if choice == 1:
                auth.login()
                break
            elif choice == 2:
                auth.sign_up()
                break
            elif choice == 3:
                PasswordReset.reset_password()
                break
            elif choice == 4:
                exit
                break
            else:
                print("XXXXXX---Warning---XXXXXX\nInvalid choice\nEnter The Choice Correctly")

class auth:
    @staticmethod
    def login():
        email = AuthView.get_email()
        password = AuthView.get_password()
        
        if auth.check_login(email, password):
            AuthView.display_logged_in_successfully()
            booking.Book().booking()
            exit(0)
        AuthView.display_not_signed_up()
        choice_method()

    @staticmethod
    def sign_up():
        while True:
            email = AuthView.get_email()
            password = AuthView.get_password()
            re_password = AuthView.get_repeated_password()
            phone_no = AuthView.get_phone_number()

            if password == re_password:
                db = Database()
                db.execute_query('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT,
                        password TEXT
                    )
                ''')
                db.execute_query('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))

                print('Do you want to log in? [Yes/No]')
                start_over = str(input()).lower()
                if 'y' in start_over:
                    auth.login()
                else:
                    choice_method()
                break
            else:
                AuthView.display_password_mismatch()
                break

    @staticmethod
    def check_login(email, password):
        db = Database()
        result = db.execute_select('SELECT COUNT(*) FROM users WHERE email=? AND password=?', (email, password))

        return result[0][0] > 0