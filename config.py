import os
import json
from typing import Any, Dict

class GameConfig:
    DEFAULT_SETTINGS = {
        "frame_rate": 60,
        "resolution": [1920, 1080],
        "vsync": True,
        "texture_quality": "ultra"
    }

    def __init__(self, config_path: str = "settings.json"):
        self.path = config_path
        self.settings = self._load_and_merge()

    def _load_and_merge(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return self.DEFAULT_SETTINGS.copy()
        
        try:
            with open(self.path, "r") as f:
                user_data = json.load(f)
        except (json.JSONDecodeError, IOError):
            return self.DEFAULT_SETTINGS.copy()

        merged = self.DEFAULT_SETTINGS.copy()
        merged.update({k: v for k, v in user_data.items() if k in merged})
        return merged

    def __getattr__(self, name: str) -> Any:
        if name in self.settings:
            return self.settings[name]
        raise AttributeError(f"Config has no attribute {name}")

    def save(self) -> None:
        with open(self.path, "w") as f:
            json.dump(self.settings, f, indent=4)