import os
import json
from pathlib import Path
from typing import Any, Dict, Union

DEFAULT_CONFIG: Dict[str, Any] = {
    "target_fps": 144,
    "resolution_scale": 1.0,
    "enable_vsync": False,
    "shadow_quality": "medium",
    "telemetry": {
        "sample_rate_hz": 60,
        "buffer_size_mb": 128,
        "log_draw_calls": True
    },
    "engine_flags": ["NO_THREAD_SYNC", "ASYNC_SHADERS"]
}

class CascadeConfig:
    """Cascade configuration loader merging defaults with local files and env vars."""

    def __init__(self, config_path: Union[str, Path, None] = None, env_prefix: str = "GPERF_"):
        self._prefix = env_prefix
        self._store = json.loads(json.dumps(DEFAULT_CONFIG))
        if config_path and Path(config_path).exists():
            self._merge_file(Path(config_path))
        self._apply_env_overrides()

    def _merge_file(self, path: Path) -> None:
        try:
            with open(path, "r", encoding="utf-8") as f:
                user_data = json.load(f)
                self._recursive_update(self._store, user_data)
        except (json.JSONDecodeError, OSError):
            pass

    def _recursive_update(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        for k, v in source.items():
            if isinstance(v, dict) and k in target and isinstance(target[k], dict):
                self._recursive_update(target[k], v)
            else:
                target[k] = v

    def _apply_env_overrides(self) -> None:
        for env_key, env_val in os.environ.items():
            if env_key.startswith(self._prefix):
                clean_key = env_key[len(self._prefix):].lower()
                self._inject_env_key(clean_key, env_val)

    def _inject_env_key(self, key_path: str, raw_val: str) -> None:
        parts = key_path.split("__")
        curr = self._store
        for part in parts[:-1]:
            if part not in curr or not isinstance(curr[part], dict):
                curr[part] = {}
            curr = curr[part]
        try:
            curr[parts[-1]] = json.loads(raw_val)
        except (json.JSONDecodeError, TypeError):
            curr[parts[-1]] = raw_val

    def get(self, path: str, default: Any = None) -> Any:
        curr = self._store
        for k in path.split("."):
            if isinstance(curr, dict) and k in curr:
                curr = curr[k]
            else:
                return default
        return curr

    def __getattr__(self, name: str) -> Any:
        if name in self._store:
            return self._store[name]
        raise AttributeError(f"No configuration key named '{name}'")
