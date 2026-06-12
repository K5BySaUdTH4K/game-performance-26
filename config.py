import json
import os

class ConfigError(Exception):
    pass

def load_config(file_path):
    if not os.path.exists(file_path):
        raise ConfigError(f"Configuration file '{file_path}' does not exist.")

    with open(file_path, 'r') as file:
        try:
            config = json.load(file)
        except json.JSONDecodeError as e:
            raise ConfigError(f"Error decoding JSON from '{file_path}': {str(e)}")

    required_keys = ['window_size', 'fullscreen', 'volume']
    for key in required_keys:
        if key not in config:
            raise ConfigError(f"Missing required config key: '{key}'")

    return config

if __name__ == '__main__':
    try:
        config = load_config('config.json')
        print('Configuration loaded successfully:', config)
    except ConfigError as e:
        print('Configuration error:', e)