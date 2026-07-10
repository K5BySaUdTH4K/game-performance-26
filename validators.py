import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


def validate_username(username):
    if len(username) < 3 or len(username) > 20:
        return False
    if not username.isalnum():
        return False
    return True


def validate_password(password):
    return (len(password) >= 8 and 
            any(c.isdigit() for c in password) and 
            any(c.islower() for c in password) and 
            any(c.isupper() for c in password))


def validate_game_score(score):
    return isinstance(score, int) and score >= 0


def validate_file_extension(filename, allowed_extensions):
    return filename.lower().endswith(tuple(allowed_extensions))
