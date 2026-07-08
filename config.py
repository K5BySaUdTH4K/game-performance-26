import json
import os

DEFAULT_CONFIG = {
    'screen_width': 800,
    'screen_height': 600,
    'fullscreen': False,
    'volume': 0.5,
    'language': 'en'
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                file_config = json.load(file)
                self.config.update(file_config)

    def get(self, key):
        return self.config.get(key, DEFAULT_CONFIG[key])

    def set(self, key, value):
        self.config[key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

# Example usage:
if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader.get('fullscreen'))
    loader.set('volume', 0.8)
