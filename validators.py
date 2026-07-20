import re

def validate_username(username):
    if not isinstance(username, str):
        raise ValueError('Username must be a string')
    if len(username) < 3 or len(username) > 20:
        raise ValueError('Username must be between 3 and 20 characters')
    if not re.match('^[a-zA-Z0-9_]+$', username):
        raise ValueError('Username can only contain letters, numbers, and underscores')
    return True


def validate_email(email):
    if not isinstance(email, str):
        raise ValueError('Email must be a string')
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        raise ValueError('Email format is invalid')
    return True


def validate_password(password):
    if not isinstance(password, str):
        raise ValueError('Password must be a string')
    if len(password) < 8:
        raise ValueError('Password must be at least 8 characters')
    if not re.search('[a-z]', password):
        raise ValueError('Password must contain at least one lowercase letter')
    if not re.search('[A-Z]', password):
        raise ValueError('Password must contain at least one uppercase letter')
    if not re.search('[0-9]', password):
        raise ValueError('Password must contain at least one number')
    return True

