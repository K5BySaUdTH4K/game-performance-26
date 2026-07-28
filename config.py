import json
import os

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = {}
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise ConfigError(f'Config file not found: {self.config_file}')
        try:
            with open(self.config_file, 'r') as f:
                self.config_data = json.load(f)
        except json.JSONDecodeError as e:
            raise ConfigError(f'Error decoding JSON: {e}')
        except Exception as e:
            raise ConfigError(f'Unexpected error: {e}')

    def get(self, key, default=None):
        if key in self.config_data:
            return self.config_data[key]
        if default:
            return default
        raise ConfigError(f'Key not found in config: {key}')

    def set(self, key, value):
        self.config_data[key] = value
        self.save_config()

    def save_config(self):
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config_data, f, indent=4)
        except Exception as e:
            raise ConfigError(f'Error saving config: {e}')