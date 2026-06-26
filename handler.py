import sys

class GameInputError(Exception):
    pass

def validate_input(user_input):
    if not user_input.isdigit() or int(user_input) < 0:
        raise GameInputError('Input must be a non-negative integer')
    return int(user_input)

def main_loop():
    while True:
        user_input = input('Enter a score (or type "exit" to quit): ')
        if user_input.lower() == 'exit':
            print('Exiting the game...')
            sys.exit(0)
        try:
            score = validate_input(user_input)
            print(f'Score accepted: {score}')
        except GameInputError as e:
            print(e)

if __name__ == '__main__':
    main_loop()