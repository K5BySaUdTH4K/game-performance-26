import json
import os

DEFAULT_CONFIG = {
    'screen_width': 1920,
    'screen_height': 1080,
    'fullscreen': False,
    'volume': 0.5,
    'max_fps': 60,
}

class ConfigLoader:
    def __init__(self, config_path='config.json'):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as file:
                user_config = json.load(file)
            return self.merge_configs(DEFAULT_CONFIG, user_config)
        return DEFAULT_CONFIG

    def merge_configs(self, default, user):
        merged = default.copy()
        merged.update(user)
        return merged

# Usage Example:
if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.config)