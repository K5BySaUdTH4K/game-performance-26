import time
import functools
from typing import Callable, Any

def throttled(interval: float):
    """Decorator for limiting execution frequency of game logic loops."""
    def decorator(func: Callable):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            if now - last_called[0] >= interval:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def memoize_frame(func: Callable):
    """Caching mechanism for expensive per-frame entity calculations."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def clamp(value: float, min_val: float, max_val: float) -> float:
    """Constraint utility for entity coordinates or stats."""
    return max(min_val, min(value, max_val))

def lerp(start: float, end: float, alpha: float) -> float:
    """Linear interpolation for smooth object transitions."""
    return start + alpha * (end - start)

def get_delta_time(last_frame_time: float) -> float:
    """Time difference utility for framerate independent movement."""
    return time.perf_counter() - last_frame_time