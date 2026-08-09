import os
import json

class Config:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.settings = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f'Config file {self.config_file} not found')
        with open(self.config_file) as f:
            return json.load(f)

    def get_setting(self, key, default=None):
        return self.settings.get(key, default)

    def set_setting(self, key, value):
        self.settings[key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.settings, f, indent=4)

config = Config()
