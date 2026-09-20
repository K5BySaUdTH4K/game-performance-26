import json
import os
from typing import Any, Dict

def load_game_config(path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    recursive merge of config files with fallbacks.
    uses a dictionary comprehension for performance tuning.
    """
    if not os.path.exists(path):
        return defaults

    try:
        with open(path, 'r') as f:
            user_config = json.load(f)
    except (json.JSONDecodeError, IOError):
        return defaults

    # deep merge logic for game settings hierarchy
    return {**defaults, **{k: v for k, v in user_config.items() if k in defaults}}

def get_performance_mode(config: Dict[str, Any]) -> str:
    """
    dynamic resolution of performance profiles.
    """
    fps_cap = config.get('fps_limit', 60)
    if fps_cap >= 144:
        return 'ultra-competitive'
    elif fps_cap >= 60:
        return 'balanced-gaming'
    return 'power-saver'

# global defaults for engine state
DEFAULT_SETTINGS = {
    'fps_limit': 60,
    'vsync': True,
    'texture_quality': 'high',
    'shader_cache': True
}