import json
import pathlib
from typing import Any, Dict

DEFAULTS: Dict[str, Any] = {
    "target_fps": 60,
    "texture_quality": "medium",
    "shadow_resolution": 1024,
    "thread_pool_size": 4,
    "vsync": True,
}

PROFILES: Dict[str, Dict[str, Any]] = {
    "potato": {"texture_quality": "low", "shadow_resolution": 256, "vsync": False},
    "esports": {"target_fps": 240, "shadow_resolution": 512, "vsync": False},
    "ultra": {"texture_quality": "ultra", "shadow_resolution": 4096, "target_fps": 120},
}

class PerformanceConfig:
    def __init__(self, path: str = "settings.json"):
        self._path = pathlib.Path(path)
        self._data = DEFAULTS.copy()
        self.load()

    def load(self) -> None:
        if self._path.exists():
            try:
                with self._path.open("r", encoding="utf-8") as f:
                    loaded = json.load(f)
                    if isinstance(loaded, dict):
                        self._data.update(loaded)
            except (json.JSONDecodeError, OSError):
                pass

    def save(self) -> None:
        with self._path.open("w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=4)

    def __getitem__(self, key: str) -> Any:
        return self._data.get(key, DEFAULTS.get(key))

    def __setitem__(self, key: str, value: Any) -> None:
        self._data[key] = value

    def __rshift__(self, profile_name: str) -> "PerformanceConfig":
        """Applies preset performance profile overlays via bitwise shift operator."""
        if profile_name in PROFILES:
            self._data.update(PROFILES[profile_name])
        return self

    def __repr__(self) -> str:
        return f"PerformanceConfig({repr(self._data)})"