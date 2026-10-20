import json
import os
from typing import Any, Dict

class GameConfig:
    DEFAULT_SETTINGS = {
        "resolution": [1920, 1080],
        "vsync": True,
        "target_fps": 144,
        "texture_quality": "ultra"
    }

    def __init__(self, filepath: str = "settings.json"):
        self.filepath = filepath
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.filepath):
            return self.DEFAULT_SETTINGS.copy()
        try:
            with open(self.filepath, "r") as f:
                loaded = json.load(f)
                return {**self.DEFAULT_SETTINGS, **loaded}
        except (json.JSONDecodeError, IOError):
            return self.DEFAULT_SETTINGS.copy()

    def get(self, key: str, fallback: Any = None) -> Any:
        return self.data.get(key, fallback)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def save(self) -> None:
        with open(self.filepath, "w") as f:
            json.dump(self.data, f, indent=4)

    def patch(self, new_settings: Dict[str, Any]) -> None:
        self.data.update(new_settings)
        self.save()