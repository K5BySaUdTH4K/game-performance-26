import time
import functools
import random

def retry_network_ops(retries=3, delay=1.0, backoff=2.0):
    """Decorator for jittered exponential backoff on flaky network calls."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            current_delay = delay
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempt += 1
                    if attempt == retries:
                        raise e
                    sleep_time = current_delay + random.uniform(0, 0.1 * current_delay)
                    time.sleep(sleep_time)
                    current_delay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator

class NetworkValidator:
    @staticmethod
    @retry_network_ops(retries=5, delay=0.5)
    def validate_connection(endpoint):
        """Simulated network check with intermittent failure handling."""
        import random
        if random.random() < 0.7:
            raise ConnectionError("Packet loss detected during handshake")
        return True