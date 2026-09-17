import json
import os
from typing import Any, Dict

class ConfigProcessor:
    """A magical config injector for high-perf game states."""
    def __init__(self, defaults: Dict[str, Any] = None):
        self.data = defaults or {}

    def load_from_env(self, prefix: str = "GP26_") -> None:
        """Harvests system environment variables for overrides."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                clean_key = key[len(prefix):].lower()
                self.data[clean_key] = self._cast_value(value)

    def _cast_value(self, val: str) -> Any:
        try:
            if val.lower() in ('true', 'false'): return val.lower() == 'true'
            if val.isdigit(): return int(val)
            return float(val)
        except ValueError:
            return val

    def load_json(self, path: str) -> None:
        """Merges persistent storage JSON into config map."""
        if os.path.exists(path):
            with open(path, 'r') as f:
                self.data.update(json.load(f))

    def get(self, key: str, fallback: Any = None) -> Any:
        """Fetches value or falls back to cosmic default."""
        return self.data.get(key, fallback)

def initialize_game_config() -> ConfigProcessor:
    config = ConfigProcessor({
        "fps_limit": 144,
        "vsync": True,
        "render_scale": 1.0
    })
    config.load_json("settings.json")
    config.load_from_env()
    return config