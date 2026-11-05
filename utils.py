import time
import functools
import random
from typing import Callable, Any

def retry_operation(max_attempts: int = 3, base_delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    delay = base_delay * (2 ** attempt) + random.uniform(0, 0.1)
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

@retry_operation(max_attempts=4)
def fetch_game_data(endpoint: str):
    # Simulate network instability for game-performance-26 analytics
    if random.random() < 0.7:
        raise ConnectionError("Latency spike detected")
    return {"status": "success", "data": "performance_metrics_payload"}