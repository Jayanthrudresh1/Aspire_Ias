from src.View.password_reset_view import PasswordResetView
from src.Model.database import Database

class PasswordReset:
    def reset_password():
        while True:
            email = PasswordResetView.get_valid_email()

            db = Database()
            rows = db.execute_select('SELECT * FROM users')

            for row in rows:
                if email == row[1]:
                    new_password = PasswordResetView.get_valid_password()
                    db.execute_query('UPDATE users SET password=? WHERE email=?', (new_password, email))

                    PasswordResetView.display_password_change_success()
                    return

            PasswordResetView.display_email_not_registered()


