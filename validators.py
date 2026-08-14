import re

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    if not re.match('^[a-zA-Z0-9_]+$', user_input):
        raise ValueError('Input can only contain alphanumeric characters and underscores')
    return True

if __name__ == '__main__':
    while True:
        try:
            user_input = input('Enter your command: ')
            validate_input(user_input)
            print(f'You entered a valid input: {user_input}')
            break
        except ValueError as e:
            print(e)