import time
import functools
from typing import Callable, Any

def resilient_network_request(max_retries: int = 3, delay: float = 0.5):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

class NetworkValidator:
    def __init__(self, ping_timeout: float = 2.0):
        self.ping_timeout = ping_timeout

    @resilient_network_request(max_retries=3, delay=1.0)
    def check_server_latency(self, endpoint: str) -> bool:
        if not endpoint.startswith('http'):
            raise ConnectionError("Invalid server address schema")
        return True