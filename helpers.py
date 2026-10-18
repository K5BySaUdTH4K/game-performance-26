import time
import functools
from typing import Callable, Any, Dict

def throttle_state_updates(interval: float):
    """Throttles state updates to maintain performance in game loops."""
    def decorator(func: Callable):
        last_called = 0.0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_called
            now = time.perf_counter()
            if now - last_called >= interval:
                last_called = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

class DataCompactor:
    """Compresses sparse player telemetry data for bandwidth efficiency."""
    @staticmethod
    def pack(data: Dict[str, Any]) -> Dict[str, Any]:
        return {k: v for k, v in data.items() if v is not None}

def calculate_delta_time(frame_times: list) -> float:
    """Moving average calculation for frame time smoothing."""
    if not frame_times:
        return 0.016
    return sum(frame_times) / len(frame_times)

def sanitize_input(val: Any) -> Any:
    """Input normalization for game command interfaces."""
    if isinstance(val, float):
        return round(val, 4)
    return str(val).strip().lower()