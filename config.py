import json
from pathlib import Path
from typing import Any, Dict

class GameConfig:
    DEFAULT_SETTINGS = {
        "resolution": [1920, 1080],
        "vsync": True,
        "target_fps": 144,
        "anisotropic_filtering": 16
    }

    def __init__(self, config_path: str = "settings.json"):
        self.path = Path(config_path)
        self._data = self.DEFAULT_SETTINGS.copy()
        self._load()

    def _load(self) -> None:
        if self.path.exists():
            try:
                with open(self.path, "r") as f:
                    loaded = json.load(f)
                    self._data.update({k: v for k, v in loaded.items() if k in self.DEFAULT_SETTINGS})
            except (json.JSONDecodeError, OSError):
                pass

    def get(self, key: str) -> Any:
        return self._data.get(key, self.DEFAULT_SETTINGS.get(key))

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def save(self) -> None:
        with open(self.path, "w") as f:
            json.dump(self._data, f, indent=4)

def get_config() -> GameConfig:
    if not hasattr(get_config, "_instance"):
        get_config._instance = GameConfig()
    return get_config._instance