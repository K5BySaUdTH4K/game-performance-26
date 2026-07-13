FPS_LIMIT = 60

# Game resolution constants
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Color constants in RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player constants
PLAYER_SPEED = 5
PLAYER_JUMP_HEIGHT = 10

# Game physics constants
GRAVITY = 9.81
FRICTION = 0.1

# Sound constants
MUSIC_VOLUME = 0.5
SFX_VOLUME = 0.7

# Timing constants
FRAME_TIME = 1 / FPS_LIMIT
MIN_FRAME_TIME = 0.001

# Prefetching thresholds
DATA_PREFETCH_THRESHOLD = 2

# Spawn point offsets
def spawn_offset(forward=True):
    return (0, PLAYER_JUMP_HEIGHT) if forward else (0, -PLAYER_JUMP_HEIGHT)
