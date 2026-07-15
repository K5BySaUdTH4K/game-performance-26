class GameError(Exception):
    """Base class for exceptions in the game."""
    pass

class PlayerNotFoundError(GameError):
    """Raised when a player is not found."""
    def __init__(self, player_id):
        super().__init__(f'Player with id {player_id} not found.')
        self.player_id = player_id

class InvalidMoveError(GameError):
    """Raised when a move is invalid."""
    def __init__(self, move):
        super().__init__(f'Invalid move attempted: {move}.')
        self.move = move

class GameNotStartedError(GameError):
    """Raised when an operation is attempted before the game starts."""
    def __init__(self):
        super().__init__('The game has not started yet.')

class GameAlreadyStartedError(GameError):
    """Raised when attempting to start an already started game."""
    def __init__(self):
        super().__init__('The game is already in progress.')
