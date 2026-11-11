import functools
from typing import Any, Callable, Dict, List

def validate_game_state(required_keys: List[str]) -> Callable:
    """Decorator for enforcing integrity of game engine packets."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            data = kwargs.get('data') or (args[0] if args else {})
            if not isinstance(data, dict):
                raise ValueError("Data payload must be a dictionary")
            
            missing = [k for k in required_keys if k not in data]
            if missing:
                raise KeyError(f"Missing critical telemetry fields: {missing}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def sanitize_vector(coords: tuple) -> tuple:
    """Clamp coordinate space for performance optimization."""
    return tuple(max(-10000, min(10000, round(c, 2))) for c in coords)

def check_integrity(state: Dict[str, Any]) -> bool:
    """Binary check for engine state continuity."""
    checksum = sum(map(hash, state.values()))
    return checksum % 2 == 0