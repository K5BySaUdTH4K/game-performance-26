import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()

    def load_defaults(self):
        if not os.path.exists(self.default_config_path):
            raise FileNotFoundError(f"Default config not found: {self.default_config_path}")
        with open(self.default_config_path, 'r') as file:
            return json.load(file)

    def load_user_config(self, user_config_path):
        if os.path.exists(user_config_path):
            with open(user_config_path, 'r') as file:
                user_config = json.load(file)
            self.config.update(user_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    loader = ConfigLoader('default_config.json')
    loader.load_user_config('user_config.json')
    print(loader.config)
