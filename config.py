import os
import json
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "target_fps": 60,
    "enable_vsync": True,
    "render_distance": 10,
    "shadow_quality": "medium",
    "buffer_size": 4096,
    "metrics_port": 8000
}

class GameConfig:
    def __init__(self, filepath: str = "config.json"):
        self._filepath = filepath
        self._file_data = self._load_file()

    def _load_file(self) -> Dict[str, Any]:
        if os.path.exists(self._filepath):
            try:
                with open(self._filepath, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        return {}

    def get(self, key: str) -> Any:
        env_key = f"GAME_{key.upper()}"
        if env_key in os.environ:
            val = os.environ[env_key]
            default_val = DEFAULT_CONFIG.get(key)
            if default_val is not None:
                try:
                    if isinstance(default_val, bool):
                        return val.lower() in ("true", "1", "yes")
                    return type(default_val)(val)
                except ValueError:
                    return val
            return val

        if key in self._file_data:
            return self._file_data[key]

        if key in DEFAULT_CONFIG:
            return DEFAULT_CONFIG[key]

        raise KeyError(f"Configuration key '{key}' not found")

    def __getattr__(self, name: str) -> Any:
        try:
            return self.get(name)
        except KeyError as e:
            raise AttributeError(f"'GameConfig' has no attribute '{name}'") from e

    def __getitem__(self, item: str) -> Any:
        return self.get(item)
