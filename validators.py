import re

class InputValidator:
    @staticmethod
    def validate_username(username):
        pattern = r'^[a-zA-Z0-9_]{3,20}$'
        if not re.match(pattern, username):
            raise ValueError('Invalid username. Must be 3-20 characters long and can include letters, numbers, and underscores.')
        return True

    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValueError('Invalid email format.')
        return True

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long.')
        if not re.search(r'[A-Z]', password):
            raise ValueError('Password must contain at least one uppercase letter.')
        if not re.search(r'[0-9]', password):
            raise ValueError('Password must contain at least one digit.')
        return True

if __name__ == '__main__':
    # Example usage
    try:
        InputValidator.validate_username('user123')
        InputValidator.validate_email('user@example.com')
        InputValidator.validate_password('Password1')
        print('All validations passed.')
    except ValueError as e:
        print(e)