class PerformanceError(Exception):
    """Base exception for all game-performance-26 engine errors."""

class FrameDropWarning(PerformanceError):
    """Raised when frame latency exceeds acceptable thresholds."""

class ResourceOverloadError(PerformanceError):
    """Raised when memory or GPU utilization hits critical peaks."""

class HardwareAbstractionError(PerformanceError):
    """Raised when low-level hardware communication fails."""

def monitor_performance(func):
    """Decorator for tracking execution drift in game loops."""
    import time
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        if elapsed > 0.016:  # 60 FPS threshold
            raise FrameDropWarning(f"Latency spike detected: {elapsed:.4f}s")
        return result
    return wrapper

def graceful_panic(reason: str):
    """Custom exit sequence for irrecoverable engine state."""
    import sys
    print(f"CRITICAL ENGINE FAILURE: {reason}")
    sys.exit(1)