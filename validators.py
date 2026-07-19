import re

def validate_username(username):
    if not isinstance(username, str) or len(username) < 3:
        raise ValueError("Username must be a string with at least 3 characters.")
    if not re.match('^[a-zA-Z0-9_]+$', username):
        raise ValueError("Username can only contain letters, numbers, and underscores.")
    return True


def validate_score(score):
    if not isinstance(score, int) or score < 0:
        raise ValueError("Score must be a non-negative integer.")
    return True


def validate_game_input(user_input):
    validate_username(user_input.get('username'))
    validate_score(user_input.get('score'))


if __name__ == '__main__':
    # Example usage in a game
    user_data = {'username': 'Player1', 'score': 100}
    try:
        validate_game_input(user_data)
        print('Input is valid.')
    except ValueError as e:
        print(f'Input validation error: {e}')