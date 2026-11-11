import json
import os
from collections import ChainMap
from typing import Any, Dict


class ConfigCascade:
    """Dynamic configuration loader with hardware-aware fallbacks for engine tuning."""

    DEFAULT_PROFILES: Dict[str, Any] = {
        "target_fps": 60,
        "render_scale": 1.0,
        "shadow_quality": "medium",
        "max_worker_threads": max(1, (os.cpu_count() or 4) - 1),
        "dynamic_resolution": True,
        "v_sync": False,
        "particle_limit": 2048,
    }

    def __init__(self, override_path: str | None = None):
        self._overrides = self._load_file(override_path) if override_path else {}
        self._env_overrides = self._extract_env_configs()
        self._merged = ChainMap(self._env_overrides, self._overrides, self.DEFAULT_PROFILES)

    def _load_file(self, path: str) -> Dict[str, Any]:
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def _extract_env_configs(self) -> Dict[str, Any]:
        prefix = "GAME_PERF_"
        extracted = {}
        for key, val in os.environ.items():
            if key.startswith(prefix):
                clean_key = key[len(prefix):].lower()
                extracted[clean_key] = self._parse_val(val)
        return extracted

    @staticmethod
    def _parse_val(val: str) -> Any:
        val_lower = val.lower()
        if val_lower in ("true", "false"):
            return val_lower == "true"
        try:
            return float(val) if "." in val else int(val)
        except ValueError:
            return val

    def __getattr__(self, name: str) -> Any:
        if name in self._merged:
            return self._merged[name]
        raise AttributeError(f"Configuration option '{name}' is invalid")

    def __getitem__(self, key: str) -> Any:
        return getattr(self, key)

    def dump_active_profile(self) -> Dict[str, Any]:
        return dict(self._merged)