import functools
import time
import logging
from typing import Callable, Any

def frame_throttle(ms: int = 16):
    def decorator(func: Callable):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            if (now - last_called[0]) * 1000 >= ms:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def memoize_lru_with_ttl(ttl_seconds: int = 60):
    def decorator(func: Callable):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
            now = time.time()
            if args in cache:
                val, ts = cache[args]
                if now - ts < ttl_seconds:
                    return val
            result = func(*args)
            cache[args] = (result, now)
            return result
        return wrapper
    return decorator

def safe_execute(func: Callable, default: Any = None, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logging.error(f"execution failure in {func.__name__}: {e}")
        return default

def batch_process(iterable: list, size: int):
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]