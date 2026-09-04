from typing import List, Union, Callable, Any
import time

Metric = Union[int, float]

def throttle_frame_rate(fps_limit: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator to artificially cap function execution speed.
    Ensures game logic loops don't melt the GPU.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        interval: float = 1.0 / fps_limit
        last_call: float = 0.0

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal last_call
            elapsed = time.perf_counter() - last_call
            if elapsed < interval:
                time.sleep(interval - elapsed)
            last_call = time.perf_counter()
            return func(*args, **kwargs)
        return wrapper
    return decorator

def calculate_delta_time(frame_times: List[Metric]) -> float:
    """
    Calculates moving average of frame processing time.
    Returns the average in seconds for engine synchronization.
    """
    if not frame_times:
        return 0.016
    return float(sum(frame_times) / len(frame_times))

def lerp_position(start: float, end: float, alpha: float) -> float:
    """
    Linear interpolation for smooth object transitions.
    Standard implementation for frame-independent movement.
    """
    return float(start + (end - start) * alpha)