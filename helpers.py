import time
import functools
from typing import Callable, Any

def throttle(seconds: float):
    """Delay execution to prevent engine frame spikes."""
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

def memoize_lru(limit: int = 128):
    """Persistent cache for expensive lookup operations."""
    cache = {}
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args):
            if args not in cache:
                if len(cache) >= limit:
                    cache.pop(next(iter(cache)))
                cache[args] = func(*args)
            return cache[args]
        return wrapper
    return decorator

def batch_process(items: list, chunk_size: int):
    """Generator for processing entities in manageable chunks."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def benchmark(func: Callable):
    """Instrumentation wrapper for performance profiling."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"[perf] {func.__name__} took {time.perf_counter() - start:.6f}s")
        return result
    return wrapper