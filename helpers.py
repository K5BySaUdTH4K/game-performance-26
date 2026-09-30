import time
import functools
import logging

logger = logging.getLogger('game-performance-26')

def frame_rate_throttle(target_fps: float):
    interval = 1.0 / target_fps
    def decorator(func):
        last_call = 0.0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_call
            elapsed = time.perf_counter() - last_call
            if elapsed < interval:
                time.sleep(interval - elapsed)
            result = func(*args, **kwargs)
            last_call = time.perf_counter()
            return result
        return wrapper
    return decorator

def profile_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        if duration > 0.016:
            logger.warning(f'{func.__name__} stutter detected: {duration:.4f}s')
        return result
    return wrapper

class ResourceRegistry:
    _storage = {}

    @classmethod
    def register(cls, key: str, resource):
        cls._storage[key] = resource

    @classmethod
    def clear_stale(cls, threshold: float):
        current_time = time.time()
        cls._storage = {k: v for k, v in cls._storage.items() if current_time - v.last_accessed < threshold}