import gc
import functools
import time

class ResourcePurge:
    """Context manager for high-frequency memory reclamation"""
    def __init__(self, threshold=5):
        self.threshold = threshold
        self.start_time = 0

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if time.perf_counter() - self.start_time > self.threshold:
            gc.collect()

def debounce_frame_updates(interval: float):
    """Decorator for rate-limiting performance-heavy game logic"""
    def decorator(func):
        last_call = 0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_call
            now = time.perf_counter()
            if now - last_call >= interval:
                last_call = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def batch_process_entities(data: list, chunk_size: int = 100):
    """Generator for splitting large entity states"""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def sanitize_frame_rate(fps: int) -> int:
    """Ensures frame stability within standard hardware limits"""
    return max(30, min(fps, 240))