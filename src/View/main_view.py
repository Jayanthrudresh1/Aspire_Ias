class main_view:
    @staticmethod
    def display_welcome_message():
        print("-----------------------------------Welcome--------------------------------------------")

    @staticmethod
    def display_menu():
        print("Please Enter Choice Given")
        print("1. User login")
        print("2. Admin login")
        print("3. Exit")

    @staticmethod
    def get_choice():
        return int(input("Enter your choice: "))

    @staticmethod
    def display_exit_message():
        print("Exiting the program. Goodbye!")

    @staticmethod
    def clear_screen():
        print("\n" * 50)  # Add enough empty lines to clear the screen
