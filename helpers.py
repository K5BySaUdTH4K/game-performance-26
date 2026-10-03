import time
import functools
from typing import Callable, Any

def throttle(seconds: float):
    def decorator(func: Callable):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.perf_counter() - last_called[0]
            if elapsed >= seconds:
                last_called[0] = time.perf_counter()
                return func(*args, **kwargs)
        return wrapper
    return decorator

def clamp(value: float, min_val: float, max_val: float) -> float:
    return max(min_val, min(value, max_val))

def memoize_ttl(ttl: int):
    def decorator(func: Callable):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
            now = time.time()
            if args in cache:
                val, timestamp = cache[args]
                if now - timestamp < ttl:
                    return val
            result = func(*args)
            cache[args] = (result, now)
            return result
        return wrapper
    return decorator

def format_latency(ms: float) -> str:
    color = "\033[92m" if ms < 50 else "\033[93m" if ms < 100 else "\033[91m"
    return f"{color}{ms:.2f}ms\033[0m"