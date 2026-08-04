import json
import os

def load_config(config_file='config.json'):
    if not os.path.exists(config_file):
        raise FileNotFoundError(f'Config file {config_file} does not exist')
    with open(config_file, 'r') as file:
        return json.load(file)

def save_config(config_data, config_file='config.json'):
    with open(config_file, 'w') as file:
        json.dump(config_data, file, indent=4)

def get_default_config():
    return {
        'resolution': '1920x1080',
        'fullscreen': True,
        'volume': 70,
        'controls': {
            'up': 'W',
            'down': 'S',
            'left': 'A',
            'right': 'D',
            'attack': 'SPACE',
        }
    }