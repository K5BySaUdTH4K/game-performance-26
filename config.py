import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = self.default_config.copy()

    def load_config(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                file_config = json.load(file)
                self.config.update(file_config)
        return self.config

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example of default configuration
DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 75,
    'controls': {'move_up': 'W', 'move_down': 'S', 'shoot': 'SPACE'}
}

# Usage:
# loader = ConfigLoader(DEFAULT_CONFIG)
# config = loader.load_config('config.json')
# print(config)