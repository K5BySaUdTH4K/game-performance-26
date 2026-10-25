import time
import functools
from typing import Callable, Any, Dict

def frame_throttle(ms: int = 16):
    """Decorator to enforce frame budget constraints on functions."""
    def decorator(func: Callable):
        last_call = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = (time.perf_counter() - last_call[0]) * 1000
            if elapsed < ms:
                time.sleep((ms - elapsed) / 1000)
            result = func(*args, **kwargs)
            last_call[0] = time.perf_counter()
            return result
        return wrapper
    return decorator

class TelemetryBuffer:
    """Circular buffer for game telemetry events."""
    def __init__(self, size: int = 100):
        self.size = size
        self.buffer = []

    def push(self, event: Dict[str, Any]) -> None:
        if len(self.buffer) >= self.size:
            self.buffer.pop(0)
        event.update({'timestamp': time.time()})
        self.buffer.append(event)

    def export_batch(self) -> list:
        return self.buffer.copy()

def normalize_latency(value: float, min_val: float = 0.0, max_val: float = 200.0) -> float:
    """Linear normalization for network jitter analysis."""
    return max(0.0, min(1.0, (value - min_val) / (max_val - min_val)))