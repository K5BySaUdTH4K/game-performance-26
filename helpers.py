import functools
import logging
from typing import Callable, Any

logger = logging.getLogger('performance-logger')

class PerformanceError(Exception):
    """Custom exception for edge cases in gaming loop."""
    pass

def robust_execution(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except (ValueError, ZeroDivisionError, TypeError) as e:
            logger.error(f'Edge case trigger in {func.__name__}: {e}')
            return None
        except Exception as e:
            raise PerformanceError(f'Critical game engine failure: {e}') from e
    return wrapper

@robust_execution
def calculate_fps(frame_times: list) -> float:
    if not frame_times:
        raise ValueError('Empty frame buffer')
    return 1000.0 / (sum(frame_times) / len(frame_times))

def sanitize_input(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        logger.warning('Invalid input, defaulting to zero')
        return 0.0