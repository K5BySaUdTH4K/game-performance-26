import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.config = self.load_default_config()

    def load_default_config(self):
        if not os.path.isfile(self.default_config_path):
            raise FileNotFoundError(f"Config file not found: {self.default_config_path}")
        with open(self.default_config_path, 'r') as json_file:
            return json.load(json_file)

    def get_value(self, key, default=None):
        return self.config.get(key, default)

    def load_additional_config(self, additional_config_path):
        if os.path.isfile(additional_config_path):
            with open(additional_config_path, 'r') as json_file:
                additional_config = json.load(json_file)
                self.config.update(additional_config)

# Usage
if __name__ == '__main__':
    loader = ConfigLoader('default_config.json')
    loader.load_additional_config('user_config.json')
    print(loader.get_value('some_key', 'default_value'))