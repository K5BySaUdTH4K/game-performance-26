import json
import os

def load_config(config_path='config.json', defaults=None):
    if defaults is None:
        defaults = {}
    
    if not os.path.isfile(config_path):
        return defaults
    
    with open(config_path, 'r') as config_file:
        try:
            user_config = json.load(config_file)
        except json.JSONDecodeError:
            return defaults
    
    return {**defaults, **user_config}

if __name__ == '__main__':
    default_settings = {'window_size': '800x600', 'fullscreen': False}
    config = load_config(defaults=default_settings)
    print(config)