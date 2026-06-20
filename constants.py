from typing import Final

# Game constants
GRAVITY: Final[float] = 9.8  # Gravity constant in m/s²
SPEED_LIMIT: Final[int] = 120  # Speed limit in units
MAX_HEALTH: Final[int] = 100  # Maximum health of a player
MIN_HEALTH: Final[int] = 0  # Minimum health of a player
# Game stages
class GameStage:
    MENU: str = 'menu'
    PLAYING: str = 'playing'
    PAUSED: str = 'paused'
    GAME_OVER: str = 'game_over'

class GameSettings:
    MAX_PLAYERS: Final[int] = 4  # Maximum number of players
    RESOLUTION: Final[tuple[int, int]] = (1920, 1080)  # Screen resolution
    VOLUME: Final[float] = 0.5  # Default volume level (0.0 to 1.0)

