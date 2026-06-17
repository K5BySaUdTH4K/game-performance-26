from typing import Final

# Game constants

# The dimensions of the game window
WIDTH: Final[int] = 800
HEIGHT: Final[int] = 600

# Colors in RGB format
WHITE: Final[tuple[int, int, int]] = (255, 255, 255)
BLACK: Final[tuple[int, int, int]] = (0, 0, 0)
RED: Final[tuple[int, int, int]] = (255, 0, 0)
GREEN: Final[tuple[int, int, int]] = (0, 255, 0)
BLUE: Final[tuple[int, int, int]] = (0, 0, 255)

# Game settings
FPS: Final[int] = 60

def get_dimensions() -> tuple[int, int]:
    """
    Returns the dimensions of the game window.

    Returns:
        tuple[int, int]: Width and height of the window.
    """
    return WIDTH, HEIGHT


def get_colors() -> dict[str, tuple[int, int, int]]:
    """
    Returns a dictionary of defined colors.

    Returns:
        dict[str, tuple[int, int, int]]: Color names and their RGB values.
    """
    return {
        'white': WHITE,
        'black': BLACK,
        'red': RED,
        'green': GREEN,
        'blue': BLUE,
    }