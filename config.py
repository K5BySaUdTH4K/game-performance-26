import json

class ConfigError(Exception):
    pass

class GameConfig:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config_data = self.load_config()

    def load_config(self):
        try:
            with open(self.config_path, 'r') as file:
                data = json.load(file)
            self.validate_config(data)
            return data
        except FileNotFoundError:
            raise ConfigError(f'Config file not found: {self.config_path}')
        except json.JSONDecodeError:
            raise ConfigError('Error parsing JSON from the config file')

    def validate_config(self, data):
        required_keys = ['screen_width', 'screen_height', 'fps']
        for key in required_keys:
            if key not in data:
                raise ConfigError(f'Missing required config key: {key}')
            elif not isinstance(data[key], int) or data[key] <= 0:
                raise ConfigError(f'Invalid value for {key}: must be a positive integer')

    def get(self, key):
        if key in self.config_data:
            return self.config_data[key]
        else:
            raise ConfigError(f'Config key {key} not found')