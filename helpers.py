import random
import re

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if not re.match('^[a-zA-Z0-9_]+$', user_input):
        raise ValueError('Input can only contain alphanumeric characters or underscores')
    return True

def main_loop():
    while True:
        user_input = input('Enter a command: ')
        try:
            validate_input(user_input)
            process_command(user_input)
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print('\nExiting...')
            break


def process_command(command):
    if command == 'roll':
        result = random.randint(1, 6)
        print(f'You rolled a {result}')
    else:
        print('Unknown command')

if __name__ == '__main__':
    main_loop()