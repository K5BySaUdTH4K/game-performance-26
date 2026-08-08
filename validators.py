def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    if any(char.isdigit() for char in user_input):
        raise ValueError('Input cannot contain numbers')
    return True

def main_processing_loop():
    while True:
        user_input = input('Enter your command: ')
        try:
            validate_input(user_input)
            process_command(user_input)
        except ValueError as e:
            print(f'Invalid input: {e}')
        except KeyboardInterrupt:
            print('\nExiting...')
            break

if __name__ == '__main__':
    main_processing_loop()