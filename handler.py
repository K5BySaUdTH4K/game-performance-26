import time
import random
from functools import wraps

def resilient_network_call(max_attempts=3, backoff=0.5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    sleep_time = backoff * (2 ** (attempts - 1)) + (random.random() * 0.1)
                    time.sleep(sleep_time)
            return None
        return wrapper
    return decorator

class NetworkHandler:
    @resilient_network_call(max_attempts=4)
    def sync_game_state(self, payload):
        # Simulate unstable network in gaming environment
        if random.random() < 0.7:
            raise ConnectionError("Packet loss detected")
        return {"status": "synced", "data": payload}