class GameError(Exception):
    """Base class for exceptions in the game."""
    pass

class ConnectionError(GameError):
    """Raised when the game connection fails."""
    def __init__(self, message: str) -> None:
        super().__init__(message)

class InvalidMoveError(GameError):
    """Raised when an invalid move is attempted."""
    def __init__(self, move: str) -> None:
        self.move = move
        message = f"Invalid move: {move}"  
        super().__init__(message)

class PlayerNotFoundError(GameError):
    """Raised when a player is not found in the game."""
    def __init__(self, player_id: int) -> None:
        self.player_id = player_id
        message = f"Player with ID {player_id} not found."  
        super().__init__(message)

# Example use case
if __name__ == '__main__':
    try:
        raise InvalidMoveError('jump')
    except InvalidMoveError as e:
        print(e)