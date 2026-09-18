import time
import functools
from typing import Callable, Any

class PerformanceTracker:
    def __init__(self, threshold_ms: float = 16.67):
        self.threshold = threshold_ms

    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = (time.perf_counter() - start) * 1000
            if elapsed > self.threshold:
                print(f'[WARN] {func.__name__} frame spike: {elapsed:.2f}ms')
            return result
        return wrapper

    @staticmethod
    def log_payload(data: dict):
        """Serializes telemetry into compact buffer format."""
        keys = sorted(data.keys())
        buffer = '|'.join(f'{k}:{data[k]}' for k in keys)
        print(f'[TELEMETRY] {buffer}')

def frame_metric(func: Callable) -> Callable:
    """Decorator for tracking logic execution time."""
    @functools.wraps(func)
    def timed(*args, **kwargs):
        t0 = time.perf_counter()
        res = func(*args, **kwargs)
        t1 = time.perf_counter()
        PerformanceTracker.log_payload({'func': func.__name__, 'ms': round((t1-t0)*1000, 3)})
        return res
    return timed