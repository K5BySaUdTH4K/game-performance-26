class GameError(Exception):
    """
    Custom exception for game-related errors.
    """
    pass

class InvalidMoveError(GameError):
    """
    Exception raised for invalid moves in the game.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)

class OutOfBoundsError(InvalidMoveError):
    """
    Exception raised when a move is out of game bounds.
    """
    def __init__(self, x: int, y: int) -> None:
        message = f'Move to ({x}, {y}) is out of bounds.'
        super().__init__(message)

class GameNotStartedError(GameError):
    """
    Exception raised when an action is attempted before the game starts.
    """
    def __init__(self, message: str = 'Game has not started yet.') -> None:
        super().__init__(message)