import re

class AuthValidation:
    @staticmethod
    def validate_email(email):
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return re.fullmatch(email_regex, email)

    @staticmethod
    def validate_password(password):
        pwd_reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pwd_cmp = re.compile(pwd_reg)
        return re.search(pwd_cmp, password)

    @staticmethod
    def validate_phone_number(phone_number):
        ph_pattern = re.compile("(0|91)?[6-9][0-9]{9}")
        return ph_pattern.match(phone_number)
