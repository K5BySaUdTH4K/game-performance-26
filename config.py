import os
import json

class Config:
    def __init__(self, config_file='settings.json'):
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                self.settings = json.load(file)
        else:
            self.settings = {}  # Default settings

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def list_keys(self):
        return list(self.settings.keys())

# Example usage
if __name__ == '__main__':
    config = Config()
    config.set('volume', 75)
    print(config.get('volume'))  # Output: 75
    print(config.list_keys())  # Output: ['volume']
