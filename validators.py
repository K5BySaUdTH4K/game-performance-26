import re

class Validator:
    def __init__(self):
        self.patterns = {
            'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            'username': r'^[a-zA-Z0-9]{3,16}$',
            'password': r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
        }

    def validate_email(self, email):
        if re.match(self.patterns['email'], email):
            return True
        raise ValueError('Invalid email format')

    def validate_username(self, username):
        if re.match(self.patterns['username'], username):
            return True
        raise ValueError('Invalid username format')

    def validate_password(self, password):
        if re.match(self.patterns['password'], password):
            return True
        raise ValueError('Invalid password format')

# Example usage
if __name__ == '__main__':
    validator = Validator()
    print(validator.validate_email('test@example.com'))
    print(validator.validate_username('user123'))
    print(validator.validate_password('Password1'))
