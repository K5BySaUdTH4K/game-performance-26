import json
import os

class ConfigLoader:
    def __init__(self, defaults):
        self.defaults = defaults
        self.config = defaults.copy()

    def load(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                file_config = json.load(file)
                self.config.update(file_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage:
if __name__ == '__main__':
    default_config = {
        'resolution': '1920x1080',
        'fullscreen': True,
        'volume': 75
    }
    config_loader = ConfigLoader(defaults=default_config)
    config_loader.load('config.json')

    print(config_loader.get('resolution'))
    print(config_loader.get('volume', 50))
    