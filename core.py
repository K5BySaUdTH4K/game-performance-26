import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Dynamic configuration loader with fallback chain"""
    def __init__(self, defaults: Dict[str, Any]):
        self.config = defaults

    def load(self, path: str) -> None:
        if os.path.exists(path):
            with open(path, 'r') as f:
                try:
                    self.config.update(json.load(f))
                except json.JSONDecodeError:
                    pass

    def __getitem__(self, key: str) -> Any:
        return self.config.get(key)

def get_game_config() -> ConfigLoader:
    defaults = {
        "fps_cap": 60,
        "vsync": True,
        "resolution": [1920, 1080],
        "debug_mode": False
    }
    loader = ConfigLoader(defaults)
    loader.load("settings.json")
    return loader

if __name__ == "__main__":
    cfg = get_game_config()
    print(f"Current Frame Cap: {cfg['fps_cap']}")