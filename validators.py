def validate_player_score(score):
    if not isinstance(score, (int, float)):
        raise ValueError("Score must be a number.")
    if score < 0:
        raise ValueError("Score cannot be negative.")
    return True


def validate_player_name(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")
    if len(name) < 3 or len(name) > 20:
        raise ValueError("Name must be between 3 and 20 characters.")
    if not name.isalnum():
        raise ValueError("Name must contain only alphanumeric characters.")
    return True


def validate_game_level(level):
    if not isinstance(level, int):
        raise TypeError("Level must be an integer.")
    if level < 1 or level > 100:
        raise ValueError("Level must be between 1 and 100.")
    return True


def validate_player_data(player_data):
    try:
        validate_player_name(player_data['name'])
        validate_player_score(player_data['score'])
        validate_game_level(player_data['level'])
    except (TypeError, ValueError) as e:
        print(f"Validation error: {e}")
        return False
    return True