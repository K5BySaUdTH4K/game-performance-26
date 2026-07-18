import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config = self.load_config(default_config_path)
        self.user_config = self.load_config(user_config_path)
        self.final_config = self.merge_configs(self.default_config, self.user_config)

    def load_config(self, path):
        if not os.path.exists(path):
            return {}
        with open(path, 'r') as f:
            return json.load(f)

    def merge_configs(self, defaults, user):
        config = defaults.copy()  # Start with default values
        config.update(user)  # Override them with user values
        return config

    def get_config(self):
        return self.final_config

# Example usage:
if __name__ == '__main__':
    loader = ConfigLoader('default_config.json', 'user_config.json')
    print(loader.get_config())