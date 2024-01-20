from sys import exit
from rich.console import Console
from rich.table import Table
from src.Model.database import Database

console = Console()

class ViewDetails:
    def choice_view(self):
        while True:
            view = int(input("Please Enter to View \n1. Login Details\n2. Booking Details\n3. Exit\nHere: "))
            if view == 1:
                self.login_details()
            elif view == 2:
                self.booking_details()
            elif view == 3:
                exit(0)
            else:
                print("Invalid Choice")     

    def booking_details(self):
        table = Table(title="Booking Details")
        table.add_column("Token")
        table.add_column("Name")
        table.add_column("Service")
        table.add_column("Date")
        
        db = Database()
        rows = db.execute_select('SELECT * FROM booking_details')

        for row in rows:
            if row[2] == '0':
                service = 'Scanning'
            elif row[2] == '1':
                service = 'X-ray'
            else:
                service = 'Testing'
            table.add_row(str(row[0]), row[1], service, row[3], style='bright_green')
        
        console.print("\n", table)

    def login_details(self):
        table = Table(title="Login Details")
        table.add_column("ID")
        table.add_column("Email")
        table.add_column("Password")
        
        db = Database()
        rows = db.execute_select('SELECT * FROM users')

        for row in rows:
            table.add_row(str(row[0]), row[1], row[2], style='bright_green')
        
        console = Console()
        console.print("\n", table)
