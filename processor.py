import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Dynamic configuration loader with fallback defaults."""
    def __init__(self, defaults: Dict[str, Any]):
        self.config = defaults

    def load(self, path: str) -> 'ConfigLoader':
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    loaded = json.load(f)
                    self.config.update(loaded)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Config parse failure: {e}")
        return self

    def __getitem__(self, key: str) -> Any:
        return self.config.get(key)

    def __getattr__(self, item: str) -> Any:
        return self.config.get(item)

def get_game_config(path: str = "config.json") -> ConfigLoader:
    defaults = {
        "resolution": [1920, 1080],
        "vsync": True,
        "target_fps": 144,
        "cache_size_mb": 512
    }
    return ConfigLoader(defaults).load(path)

if __name__ == "__main__":
    cfg = get_game_config()
    print(f"Active resolution: {cfg.resolution}")