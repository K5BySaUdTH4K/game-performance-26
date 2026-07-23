class GameError(Exception):  
    """Base class for other exceptions in the game."""
    pass  

class InvalidInputError(GameError):  
    def __init__(self, message='Invalid input provided.'):  
        self.message = message  
        super().__init__(self.message)  

class GameStateError(GameError):  
    def __init__(self, state, message='Invalid game state.'):  
        self.state = state  
        self.message = f'{message} Current state: {self.state}'  
        super().__init__(self.message)  

class AssetNotFoundError(GameError):  
    def __init__(self, asset_name):  
        self.asset_name = asset_name  
        self.message = f'Asset "{self.asset_name}" not found.'  
        super().__init__(self.message)  

# Example edge case handling  
def load_asset(asset_name):  
    assets = ['sword', 'shield', 'potion']  
    if asset_name not in assets:  
        raise AssetNotFoundError(asset_name)  
    return f'{asset_name} loaded successfully.'  

try:  
    print(load_asset('axe'))  
except GameError as e:  
    print(e)