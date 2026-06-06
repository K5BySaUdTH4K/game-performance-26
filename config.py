import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.user_config = {}

    def load(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                self.user_config = json.load(f)

    def get(self, key, default=None):
        return self.user_config.get(key, self.default_config.get(key, default))

    def get_all(self):
        combined_config = self.default_config.copy()
        combined_config.update(self.user_config)
        return combined_config

if __name__ == '__main__':
    default_config = {'resolution': '1920x1080', 'fullscreen': True, 'volume': 50}
    config_loader = ConfigLoader(default_config)
    config_loader.load('config.json')
    print(config_loader.get_all())
