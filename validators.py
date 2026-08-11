def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    if not user_input.isalnum():
        raise ValueError('Input must be alphanumeric')
    return True

def main_loop():
    while True:
        try:
            user_input = input('Enter command: ')
            validate_input(user_input)
            process_command(user_input)
        except ValueError as e:
            print(f'Input error: {e}')
        except KeyboardInterrupt:
            print('\nExiting game.')
            break

if __name__ == '__main__':
    main_loop()