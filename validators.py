import re

def validate_username(username):
    if not re.match('^[a-zA-Z0-9]{3,16}$', username):
        raise ValueError('Invalid username: must be 3-16 alphanumeric characters')
    return True

def validate_score(score):
    if not isinstance(score, int) or score < 0:
        raise ValueError('Invalid score: must be a non-negative integer')
    return True

def validate_move(move):
    valid_moves = ['up', 'down', 'left', 'right']
    if move not in valid_moves:
        raise ValueError('Invalid move: must be one of {}'.format(valid_moves))
    return True

if __name__ == '__main__':
    try:
        validate_username('player1')
        validate_score(150)
        validate_move('up')
    except ValueError as e:
        print(e)