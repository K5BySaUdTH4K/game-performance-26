import time
import functools
from typing import Callable, Any

class PerformanceLogger:
    def __init__(self, threshold_ms: float = 16.67):
        self.threshold = threshold_ms

    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = (time.perf_counter() - start) * 1000
            if elapsed > self.threshold:
                print(f'[FRAME_SPIKE] {func.__name__} took {elapsed:.2f}ms')
            return result
        return wrapper

    @staticmethod
    def log_state(state_name: str, data: dict):
        """Snapshot telemetry for game state debugging."""
        ts = time.time()
        payload = {'ts': ts, 'state': state_name, **data}
        with open('performance.log', 'a') as f:
            f.write(str(payload) + '\n')

def track_perf(func: Callable) -> Callable:
    decorator = PerformanceLogger()
    return decorator(func)