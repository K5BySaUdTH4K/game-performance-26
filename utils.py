import time
import random
import functools
from typing import Callable, Any, Type, Tuple

class GameOverException(Exception):
    """Raised when all retries (lives) are exhausted."""
    pass

def respawn_retry(
    lives: int = 3,
    base_cooldown: float = 0.5,
    backoff_multiplier: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (ConnectionError, TimeoutError)
) -> Callable:
    """
    Decorator that retries network actions using a gaming 'respawn' metaphor.
    Includes exponential cooldown with random jitter to mimic network packet recovery.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            cooldown = base_cooldown
            for life in range(1, lives + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if life == lives:
                        raise GameOverException(
                            f"Failed '{func.__name__}' after {lives} attempts. Connection lost."
                        ) from err
                    
                    # Apply exponential backoff with a bit of jitter (chaos)
                    jitter = random.uniform(0.8, 1.2)
                    sleep_time = cooldown * jitter
                    time.sleep(sleep_time)
                    cooldown *= backoff_multiplier
        return wrapper
    return decorator
