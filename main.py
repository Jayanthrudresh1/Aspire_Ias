#Title: Online Diagnostic Booking System 
#Author: Jayanth R 
#Created On: 7/02/2023 
#Last Modified Data: 19/02/2023 
#Reviewed By: Shilpa
#Reviewed On: 26/02/2023

from sys import exit
from src.Controller.admin_login import Admin
import src.Controller.user_login as user_login
from src.View.main_view import main_view

class Main:
    def __init__(self):
        self.__choice = 0

    def start(self):
        main_view.display_welcome_message()
        
        while True:
            main_view.display_menu()
            self.__choice = main_view.get_choice()

            if self.__choice == 1:
                user_login.choice_method()
            elif self.__choice == 2:
                Admin().admin_login()
            elif self.__choice == 3:
                main_view.display_exit_message()
                exit()
            else:
                main_view.clear_screen()
                print("Invalid choice. Please choose again.\n")

if __name__ == "__main__":
    object = Main()
    object.start()

