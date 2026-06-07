import re

class InputValidator:
    @staticmethod
    def validate_email(email):
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        if not re.match(pattern, email):
            raise ValueError('Invalid email address')

    @staticmethod
    def validate_username(username):
        if len(username) < 3 or len(username) > 20:
            raise ValueError('Username must be between 3 and 20 characters')
        if not username.isalnum():
            raise ValueError('Username must be alphanumeric')

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(char.isdigit() for char in password):
            raise ValueError('Password must contain at least one numeral')
        if not any(char.isupper() for char in password):
            raise ValueError('Password must contain at least one uppercase letter')
