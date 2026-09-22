import json
import os
from typing import Any, Dict


class DynamicGameConfig:
    """Dynamic performance configuration loader with environment overrides and defaults."""

    DEFAULT_SPECS: Dict[str, Dict[str, Any]] = {
        "target_fps": {"default": 60, "type": int},
        "resolution_scale": {"default": 1.0, "type": float},
        "ray_tracing": {"default": False, "type": bool},
        "max_render_distance": {"default": 1024, "type": int},
        "asset_cache_mb": {"default": 512, "type": int},
    }

    def __init__(self, file_path: str = "perf_settings.json"):
        self._file_path = file_path
        self._values: Dict[str, Any] = {}
        self.load()

    def load(self) -> None:
        file_data = {}
        if os.path.exists(self._file_path):
            try:
                with open(self._file_path, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                file_data = {}

        for key, spec in self.DEFAULT_SPECS.items():
            env_key = f"GAME_PERF_{key.upper()}"
            val = file_data.get(key, os.environ.get(env_key, spec["default"]))
            self._values[key] = self._cast(val, spec["type"], spec["default"])

    def _cast(self, val: Any, target_type: type, fallback: Any) -> Any:
        try:
            if target_type is bool and isinstance(val, str):
                return val.lower() in ("true", "1", "yes", "on")
            return target_type(val)
        except (ValueError, TypeError):
            return fallback

    def __getattr__(self, name: str) -> Any:
        if name in self._values:
            return self._values[name]
        raise AttributeError(f"Configuration key '{name}' is not defined")

    def __getitem__(self, item: str) -> Any:
        return getattr(self, item)

    def as_dict(self) -> Dict[str, Any]:
        return dict(self._values)
