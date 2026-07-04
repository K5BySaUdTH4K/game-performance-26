import re

def is_valid_username(username):
    return bool(re.match('^[a-zA-Z0-9_]{3,16}$', username))

def is_valid_email(email):
    return bool(re.match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

def is_valid_password(password):
    return (len(password) >= 8 and 
            any(char.isdigit() for char in password) and 
            any(char.islower() for char in password) and 
            any(char.isupper() for char in password) and 
            any(char in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for char in password))

def is_valid_score(score):
    return isinstance(score, (int, float)) and 0 <= score <= 100

if __name__ == '__main__':
    print(is_valid_username('Player_1'))  # True
    print(is_valid_email('user@example.com'))  # True
    print(is_valid_password('Passw0rd!'))  # True
    print(is_valid_score(85))  # True
    print(is_valid_score(-10))  # False
