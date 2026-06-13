class GameException(Exception):
    """Base class for all game exceptions."""
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code

class PlayerNotFoundException(GameException):
    """Raised when a player is not found."""
    def __init__(self, player_id):
        message = f"Player with ID {player_id} not found"
        super().__init__(message, code=404)

class InsufficientResourcesException(GameException):
    """Raised when a player has insufficient resources."""
    def __init__(self, resource, required, available):
        message = f"Insufficient {resource}: required {required}, available {available}"
        super().__init__(message, code=403)

class LevelUpException(GameException):
    """Raised when a player cannot level up."""
    def __init__(self, player_id, level):
        message = f"Player {player_id} cannot level up to level {level}"
        super().__init__(message, code=400)