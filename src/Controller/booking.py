from time import sleep as wait
import datetime
from src.Model.database import Database
from src.View.booking_view import BookingView

class Book:
    def __init__(self):
        self.__name = ""
        self.__service = 0
        self.__date_time = ""

    def booking(self):
        while True:
            service_name = ["Scanning", "X-ray", "Testing"]
            self.__name = input("Enter Patient Name: ")
            self.__service = int(input("Please enter \n0. Scanning\n1. X-ray\n2. Testing\nHere: "))
            self.__date_time = input("Enter date (date-month-year): ")

            try:
                datetime.datetime.strptime(self.__date_time, '%d-%m-%Y')
            except ValueError:
                print("Incorrect date string")
            else:
                if 0 <= self.__service <= len(service_name):
                    db = Database()
                    db.execute_query('''
                        CREATE TABLE IF NOT EXISTS booking_details (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            service TEXT,
                            date TEXT
                        )
                    ''')

                    db.execute_query('''
                        INSERT INTO booking_details (name, service, date)
                        VALUES (?, ?, ?)
                    ''', (self.__name, str(self.__service), self.__date_time))

                    rows = db.execute_select('SELECT * FROM booking_details')

                    BookingView.display_booking_confirmation(rows)
                    BookingView.display_confirmation_message(self.__name, str(self.__service), self.__date_time)

                    wait(2)
                    break
                else:
                    print("wrong choice")
