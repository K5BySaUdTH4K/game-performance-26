import os
import json
from typing import Any, Dict

class GameConfig:
    DEFAULT_SETTINGS = {
        "frame_rate": 144,
        "resolution": [1920, 1080],
        "vsync": True,
        "gpu_acceleration": True
    }

    def __init__(self, file_path: str = "settings.json"):
        self.file_path = file_path
        self.data = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        if not os.path.exists(self.file_path):
            return self.DEFAULT_SETTINGS
        try:
            with open(self.file_path, "r") as f:
                user_data = json.load(f)
                return {**self.DEFAULT_SETTINGS, **user_data}
        except (json.JSONDecodeError, IOError):
            return self.DEFAULT_SETTINGS

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def __getattr__(self, item: str) -> Any:
        return self.data.get(item, self.DEFAULT_SETTINGS.get(item))

settings = GameConfig()