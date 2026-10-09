import json
import os
from typing import Any, Dict

class GameConfig:
    """dynamic configuration loader with fallback chain"""
    DEFAULTS = {
        "fps_cap": 144,
        "vsync": True,
        "resolution": [1920, 1080],
        "graphics_preset": "ultra"
    }

    def __init__(self, config_path: str = "settings.json"):
        self.path = config_path
        self.settings = self.DEFAULTS.copy()
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, "r") as f:
                    loaded = json.load(f)
                    self.settings.update({k: v for k, v in loaded.items() if k in self.DEFAULTS})
            except (json.JSONDecodeError, IOError):
                pass

    def __getitem__(self, key: str) -> Any:
        return self.settings.get(key)

    def save(self) -> None:
        with open(self.path, "w") as f:
            json.dump(self.settings, f, indent=4)

    @property
    def raw(self) -> Dict[str, Any]:
        return self.settings

    def __repr__(self) -> str:
        return f"<GameConfig settings={self.settings}>"