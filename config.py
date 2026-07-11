import json
from pathlib import Path

def load_config(config_file, default_file='default_config.json'):
    config_path = Path(config_file)
    default_path = Path(default_file)
    
    if not config_path.is_file():
        print(f'Custom config not found, loading defaults from {default_file}')
        return load_json(default_path)
    
    return load_json(config_path)


def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def save_config(config, config_file):
    with open(config_file, 'w') as file:
        json.dump(config, file, indent=4)


def merge_configs(custom_config, default_config):
    merged = default_config.copy()
    merged.update(custom_config)
    return merged

if __name__ == '__main__':
    merged_config = merge_configs(load_config('custom_config.json'), load_config('default_config.json'))
    print(json.dumps(merged_config, indent=4))