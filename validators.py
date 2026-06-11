def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string.')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty.')
    if len(user_input) > 100:
        raise ValueError('Input must be less than 100 characters.')
    return True

def main_loop():
    while True:
        try:
            user_input = input('Enter your command: ')
            validate_input(user_input)
            process_command(user_input)
        except ValueError as ve:
            print(f'Error: {ve}')
        except KeyboardInterrupt:
            print('\nExiting the game.')
            break


def process_command(command):
    print(f'Processing command: {command}')