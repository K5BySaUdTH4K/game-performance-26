class GameError(Exception):
    def __init__(self, message, code=500):
        self.message = message
        self.code = code
        super().__init__(self.message)

class DataNotFoundError(GameError):
    def __init__(self, data_id):
        message = f'No data found for ID: {data_id}'
        super().__init__(message, code=404)

class InvalidGameStateError(GameError):
    def __init__(self, state):
        message = f'Invalid game state: {state}'
        super().__init__(message, code=400)

class ResourceLimitExceededError(GameError):
    def __init__(self, resource):
        message = f'Resource limit exceeded: {resource}'
        super().__init__(message, code=429)