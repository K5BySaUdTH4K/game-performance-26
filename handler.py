import time
import random
from typing import Callable, Any, Tuple, Type

class GameNetworkRetrier:
    """
    A tick-friendly network retry handler for live game loops.
    Instead of blocking blindly, it manages retries with golden-ratio backoff.
    """
    def __init__(
        self, 
        max_attempts: int = 4, 
        initial_delay: float = 0.016,  # roughly 1 frame at 60fps
        max_delay: float = 1.0
    ):
        self.max_attempts = max_attempts
        self.initial_delay = initial_delay
        self.max_delay = max_delay

    def execute(self, operation: Callable[[], Any], allowed_exceptions: Tuple[Type[Exception], ...]) -> Any:
        attempt = 0
        delay = self.initial_delay
        
        while True:
            try:
                return operation()
            except allowed_exceptions as exc:
                attempt += 1
                if attempt >= self.max_attempts:
                    raise exc
                
                # Golden-ratio escalation with game frame sync jitter
                golden_ratio = 1.618
                delay = min(delay * golden_ratio, self.max_delay)
                jitter = random.uniform(0.9, 1.1)
                actual_sleep = delay * jitter
                
                time.sleep(actual_sleep)

def gaming_retry(max_attempts: int = 5, initial_delay: float = 0.033) -> Callable:
    """Decorator wrapping the GameNetworkRetrier with network-specific errors."""
    retrier = GameNetworkRetrier(max_attempts=max_attempts, initial_delay=initial_delay)
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return retrier.execute(lambda: func(*args, **kwargs), (ConnectionError, TimeoutError))
        return wrapper
    return decorator