FPS_LIMIT = 60
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
PLAYER_SPEED = 5
GRAVITY = 9.8
JUMP_HEIGHT = 15
ITEMS = {
    'health_potion': {'restore': 50, 'quantity': 10},
    'mana_potion': {'restore': 30, 'quantity': 5},
    'elixir': {'restore': 100, 'quantity': 3},
}

ENEMY_STATS = {
    'goblin': {'health': 30, 'damage': 5},
    'troll': {'health': 100, 'damage': 10},
}

WEAPON_STATS = {
    'sword': {'damage': 7, 'durability': 50},
    'axe': {'damage': 10, 'durability': 30},
}

LEVELS = 5
DIFFICULTY = 'medium'
MAX_PLAYERS = 4
POWER_UPS = ['speed_boost', 'invisibility', 'double_damage']
