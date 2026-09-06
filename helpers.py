import time
import functools
from typing import Callable, Any

def throttle(seconds: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        last_called = 0
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            nonlocal last_called
            elapsed = time.perf_counter() - last_called
            if elapsed > seconds:
                last_called = time.perf_counter()
                return func(*args, **kwargs)
        return wrapper
    return decorator

def byte_formatter(size_bytes: int) -> str:
    if size_bytes == 0: return "0B"
    units = ("B", "KB", "MB", "GB", "TB")
    i = int(size_bytes.bit_length() / 10)
    val = round(size_bytes / (1024 ** i), 2)
    return f"{val}{units[i]}"

def fps_limiter(target_fps: int) -> None:
    frame_duration = 1.0 / target_fps
    start_time = getattr(fps_limiter, "last_time", time.perf_counter())
    sleep_time = frame_duration - (time.perf_counter() - start_time)
    if sleep_time > 0:
        time.sleep(sleep_time)
    fps_limiter.last_time = time.perf_counter()

def unpack_vec(data: tuple) -> dict:
    keys = ('x', 'y', 'z', 'w')
    return {keys[i]: val for i, val in enumerate(data)}

def identity_hash(obj: Any) -> str:
    return hex(id(obj))[-6:]