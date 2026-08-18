class GameError(Exception):
    """Base class for exceptions in this module."""
    pass

class PlayerNotFoundError(GameError):
    """Raised when a player is not found."""
    def __init__(self, player_id):
        self.player_id = player_id
        super().__init__(f'Player with ID {player_id} not found.')

class InvalidMoveError(GameError):
    """Raised when a move is invalid."""
    def __init__(self, move, reason):
        self.move = move
        self.reason = reason
        super().__init__(f'Invalid move: {move}. Reason: {reason}')

class GameStateError(GameError):
    """Raised when an unexpected game state is encountered."""
    def __init__(self, message):
        super().__init__(message)

# Example usage in a game context
if __name__ == '__main__':
    try:
        raise PlayerNotFoundError(42)
    except GameError as e:
        print(e)