import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.config_data = self.load_defaults() 

    def load_defaults(self):
        with open(self.default_config_path, 'r') as file:
            return json.load(file)

    def override_with_env(self):
        for key, value in os.environ.items():
            if key.startswith('GAME_'):
                self.set_config_value(key[5:], value)

    def set_config_value(self, key, value):
        keys = key.split('__')
        data = self.config_data
        for k in keys[:-1]:
            data = data.setdefault(k, {})
        data[keys[-1]] = value

    def get(self, key, default=None):
        keys = key.split('__')
        data = self.config_data
        for k in keys:
            data = data.get(k, {})
        return data if data else default

# Usage
if __name__ == '__main__':
    config_loader = ConfigLoader('default_config.json')
    config_loader.override_with_env()
    print(config_loader.get('resolution', '1920x1080'))