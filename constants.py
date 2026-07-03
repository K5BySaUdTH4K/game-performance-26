SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
PLAYER_SPEED = 5
ENEMY_SPEED = 3
BULLET_SPEED = 10
POWER_UP_DURATION = 5000
COLORS = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255)
}

LEVELS = {
    1: {'enemy_count': 5, 'difficulty': 'easy'},
    2: {'enemy_count': 10, 'difficulty': 'medium'},
    3: {'enemy_count': 15, 'difficulty': 'hard'}
}

ITEMS = {
    'HEALTH_PACK': 10,
    'SPEED_BOOST': 5,
    'DAMAGE_BOOST': 3
}

KEYBINDS = {
    'UP': 'w',
    'DOWN': 's',
    'LEFT': 'a',
    'RIGHT': 'd',
    'FIRE': 'space'
}