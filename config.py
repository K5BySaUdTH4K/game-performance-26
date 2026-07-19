import json
import os

class ConfigLoader:
    def __init__(self, default_config=None):
        self.default_config = default_config or {}
        self.config = self.load_config()

    def load_config(self):
        config_path = os.getenv('CONFIG_PATH', 'config.json')
        if os.path.exists(config_path):
            with open(config_path, 'r') as file:
                user_config = json.load(file)
            return self.merge_configs(self.default_config, user_config)
        return self.default_config

    def merge_configs(self, default, user):
        for key, value in user.items():
            if isinstance(value, dict) and key in default:
                default[key] = self.merge_configs(default[key], value)
            else:
                default[key] = value
        return default

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example of default configuration
DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'volume': {'music': 50, 'effects': 75},
    'controls': {'jump': 'space', 'shoot': 'ctrl'}
}

# ConfigLoader usage
config_loader = ConfigLoader(DEFAULT_CONFIG)
resolution = config_loader.get('resolution')
