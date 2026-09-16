import time
import functools
from typing import Callable, Any, Dict

class FrameRateGovernor:
    def __init__(self, target_fps: int = 60):
        self.frame_time = 1.0 / target_fps
        self.last_frame = 0.0

    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start_time
            sleep_time = self.frame_time - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)
            return result
        return wrapper

def aggregate_player_metrics(session_data: list[Dict[str, float]]) -> Dict[str, float]:
    """Compresses telemetry bursts into optimized average vectors."""
    if not session_data:
        return {}
    keys = session_data[0].keys()
    return {k: sum(d[k] for d in session_data) / len(session_data) for k in keys}

def bitwise_status_check(flags: int, mask: int) -> bool:
    """Fast bitmask check for engine-level status flags."""
    return (flags & mask) == mask

# Usage example for performance-critical systems
if __name__ == '__main__':
    governor = FrameRateGovernor(144)
    @governor
    def tick_simulation():
        return True