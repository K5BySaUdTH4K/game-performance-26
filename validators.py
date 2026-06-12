import re

def validate_username(username):
    if not isinstance(username, str) or len(username) < 3:
        raise ValueError('Username must be a string of at least 3 characters.')
    if not re.match('^[a-zA-Z0-9_]+$', username):
        raise ValueError('Username can only contain alphanumeric characters and underscores.')
    return True

def validate_email(email):
    email_regex = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'  
    if not re.match(email_regex, email):
        raise ValueError('Invalid email address format.')
    return True

def validate_score(score):
    if not isinstance(score, (int, float)) or score < 0:
        raise ValueError('Score must be a non-negative number.')
    return True

if __name__ == '__main__':
    try:
        validate_username('user_01')
        validate_email('user@example.com')
        validate_score(100)
        print('All validations passed!')
    except ValueError as e:
        print(e)