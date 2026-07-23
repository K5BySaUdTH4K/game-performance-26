class GameError(Exception):
    """Base class for exceptions in the game."""
    pass

class InvalidInputError(GameError):
    """Exception raised for invalid input."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ConnectionError(GameError):
    """Exception raised for connection issues."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ConfigurationError(GameError):
    """Exception raised for configuration issues."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Example usage:
# try:
#     raise InvalidInputError('Input must be a non-negative integer')
# except GameError as e:
#     print(f'Error: {e}')