import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Magic-carpet configuration loader with deep-default merging."""
    def __init__(self, defaults: Dict[str, Any]):
        self._defaults = defaults
        self._data = defaults.copy()

    def load(self, path: str) -> None:
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    loaded = json.load(f)
                    self._deep_merge(self._data, loaded)
            except (json.JSONDecodeError, IOError):
                pass

    def _deep_merge(self, base: Dict[str, Any], overrides: Dict[str, Any]) -> None:
        for key, value in overrides.items():
            if isinstance(value, dict) and key in base and isinstance(base[key], dict):
                self._deep_merge(base[key], value)
            else:
                base[key] = value

    def get(self, key: str, fallback: Any = None) -> Any:
        return self._data.get(key, fallback)

    def __getattr__(self, name: str) -> Any:
        return self._data.get(name)

def initialize_config(file_path: str = "settings.json") -> ConfigLoader:
    defaults = {"fps": 60, "vsync": True, "graphics": {"preset": "high"}}
    loader = ConfigLoader(defaults)
    loader.load(file_path)
    return loader