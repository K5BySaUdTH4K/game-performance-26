class GameError(Exception):
    """
    Custom exception for game-related errors.
    """
    def __init__(self, message: str, code: int = 500) -> None:
        super().__init__(message)
        self.code = code

class InvalidInputError(GameError):
    """
    Exception raised for invalid inputs in the game.
    """
    def __init__(self, input_value: str) -> None:
        message = f'Invalid input: {input_value}'
        super().__init__(message, code=400)

class ConnectionError(GameError):
    """
    Exception raised for connection issues.
    """
    def __init__(self, details: str) -> None:
        message = f'Connection error: {details}'
        super().__init__(message, code=503)

class ResourceNotFoundError(GameError):
    """
    Exception raised when a resource is not found.
    """
    def __init__(self, resource_name: str) -> None:
        message = f'Resource not found: {resource_name}'
        super().__init__(message, code=404)