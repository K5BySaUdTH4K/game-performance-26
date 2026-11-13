import os
import json

class GameConfig:
    _DEFAULTS = {
        "fps_cap": 144,
        "graphics_preset": "ultra",
        "enable_raytracing": False,
        "resolution": [1920, 1080],
        "network_tickrate": 64
    }

    def __init__(self, config_path="settings.json"):
        self.path = config_path
        self.data = self._load_and_merge()

    def _load_and_merge(self):
        base = self._DEFAULTS.copy()
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                try:
                    user_data = json.load(f)
                    base.update(user_data)
                except json.JSONDecodeError:
                    pass
        return base

    def __getattr__(self, name):
        return self.data.get(name)

    def __getitem__(self, key):
        return self.data.get(key)

    def persist(self):
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)

def get_game_config():
    return GameConfig()