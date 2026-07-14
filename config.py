import json
from pathlib import Path

def load_config(file_path='config.json', defaults=None):
    defaults = defaults or {}  # Fallback to empty dict if none provided
    config_path = Path(file_path)
    if not config_path.is_file():
        return defaults
    try:
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
        return {**defaults, **config}  # Merge defaults with loaded config
    except json.JSONDecodeError:
        raise ValueError('Invalid JSON in config file')

if __name__ == '__main__':
    config = load_config()  # Example loading
    print(config)  # Print loaded config for verification
