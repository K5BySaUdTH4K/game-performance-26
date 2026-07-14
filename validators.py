import re

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    
    if not re.match('^[a-zA-Z0-9_ ]*$', user_input):
        raise ValueError('Input contains invalid characters')
    
    return True


def main_loop():
    while True:
        user_input = input('Enter command: ')
        try:
            validate_input(user_input)
            process_input(user_input)
        except ValueError as e:
            print(f'Error: {e}')  


def process_input(command):
    print(f'Processing: {command}')

if __name__ == '__main__':
    main_loop()