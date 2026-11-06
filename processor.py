import time
import functools
import random
from typing import Callable, Any

def jitter_retry(max_attempts: int = 3, base_delay: float = 0.5):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    sleep_time = (base_delay * (2 ** attempts)) + (random.random() * 0.1)
                    time.sleep(sleep_time)
        return wrapper
    return decorator

class NetworkProcessor:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    @jitter_retry(max_attempts=4, base_delay=0.2)
    def sync_game_state(self, data: dict):
        if random.random() < 0.7:
            raise ConnectionError("Packet loss simulation active")
        return {"status": "success", "payload": data}

    def process_queue(self, queue: list):
        results = []
        for item in queue:
            try:
                results.append(self.sync_game_state(item))
            except ConnectionError as e:
                results.append({"status": "failed", "error": str(e)})
        return results