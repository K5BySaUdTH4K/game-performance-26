import json
import os
from typing import Any, Dict

class GameConfig:
    def __init__(self, defaults: Dict[str, Any], path: str = 'settings.json'):
        self.path = path
        self.data = defaults
        self.load()

    def load(self) -> None:
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                try:
                    self.data.update(json.load(f))
                except json.JSONDecodeError:
                    pass

    def __getattr__(self, name: str) -> Any:
        return self.data.get(name)

    def __setitem__(self, key: str, value: Any) -> None:
        self.data[key] = value
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

def get_engine_config() -> GameConfig:
    defaults = {
        "fps_limit": 144,
        "vsync": True,
        "resolution": [1920, 1080],
        "graphics_preset": "ultra"
    }
    return GameConfig(defaults)