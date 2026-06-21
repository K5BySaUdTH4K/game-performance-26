def validate_player_name(name):
    if not isinstance(name, str):
        raise TypeError('Player name must be a string')
    if len(name) < 3 or len(name) > 20:
        raise ValueError('Player name must be between 3 and 20 characters')
    if not name.isalnum():
        raise ValueError('Player name can only contain alphanumeric characters')
    return True


def validate_score(score):
    if not isinstance(score, (int, float)):
        raise TypeError('Score must be a number')
    if score < 0:
        raise ValueError('Score cannot be negative')
    return True


def validate_game_input(player_name, score):
    try:
        validate_player_name(player_name)
        validate_score(score)
    except (TypeError, ValueError) as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'success', 'message': 'Valid input'}