class InvalidInputError(Exception):
    def __init__(self, message):
        super().__init__(message)


def validate_input(user_input):
    if not isinstance(user_input, str):
        raise InvalidInputError('Input must be a string')
    if len(user_input) < 3:
        raise InvalidInputError('Input must be at least 3 characters long')


def main_loop():
    while True:
        try:
            user_input = input('Enter command: ')
            validate_input(user_input)
            print(f'Processing command: {user_input}')
            # Here goes the rest of the command processing
        except InvalidInputError as e:
            print(f'Error: {e}')
        except KeyboardInterrupt:
            print('\nExiting...')
            break

if __name__ == '__main__':
    main_loop()