from rich.console import Console
from rich.table import Table

class BookingView:
    @staticmethod
    def display_booking_confirmation(rows):
        table = Table(title="Booking Confirmed")
        table.add_column("Token No")
        table.add_column("Name")
        table.add_column("Service")
        table.add_column("Date")
        console = Console()

        for row in rows:
            service = "Scanning" if row[2] == '0' else "X-ray" if row[2] == '1' else "Testing"
            table.add_row(str(row[0]), row[1], service, row[3], style='bright_green')

        console.print("\n", table)

    @staticmethod
    def display_confirmation_message(name, service, date):
        service_name = "Scanning" if service == '0' else "X-ray" if service == '1' else "Testing"
        print('{0} your {1} is scheduled on {2}'.format(name, service_name, date))
        print("\n_____Thank You!_____")
