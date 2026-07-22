import math

# Constants for game performance optimization
FRAME_RATE = 60
MAX_FPS = 120
MIN_FPS = 30

# Graphics settings
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
FULLSCREEN_MODE = False

# Physics constants
GRAVITY = 9.8
TERMINAL_VELOCITY = 53.0

# Animation constants
ANIMATION_FPS = 30
FRAME_DURATION = 1.0 / FRAME_RATE

# Load values that don't change
def load_constants():
    return {
        'frame_rate': FRAME_RATE,
        'max_fps': MAX_FPS,
        'min_fps': MIN_FPS,
        'screen_width': SCREEN_WIDTH,
        'screen_height': SCREEN_HEIGHT,
        'gravity': GRAVITY,
    }

# Caching for improved constant access
CONSTANTS_CACHE = load_constants()

# Function to retrieve constants
def get_constant(key):
    return CONSTANTS_CACHE.get(key, None)

# Function to refresh constants if needed
def refresh_constants():
    global CONSTANTS_CACHE
    CONSTANTS_CACHE = load_constants()