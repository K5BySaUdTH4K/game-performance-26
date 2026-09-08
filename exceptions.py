import time
import functools
import random

class NetworkGlitch(Exception):
    pass

def retry_with_jitter(max_attempts=3, backoff=0.5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except NetworkGlitch as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
                    sleep_time = (backoff * (2 ** attempts)) + (random.random() * 0.1)
                    time.sleep(sleep_time)
        return wrapper
    return decorator

def resilient_request(endpoint, payload=None):
    """Simulates a volatile gaming network call."""
    if random.random() < 0.7:
        raise NetworkGlitch(f"Packet drop at {endpoint}")
    return {"status": 200, "data": "success"}