import time
import functools
import random

class NetworkTimeoutError(Exception):
    """Raised when game server packets drop."""
    pass

def jitter_retry(attempts=3, backoff=0.5):
    """Decorator applying exponential backoff with chaos-monkey jitter."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_ex = None
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, NetworkTimeoutError) as e:
                    last_ex = e
                    delay = (backoff * (2 ** i)) + random.uniform(0, 0.1)
                    time.sleep(delay)
            raise last_ex
        return wrapper
    return decorator

@jitter_retry(attempts=3, backoff=0.2)
def fetch_server_state(endpoint):
    """Simulated fragile network call for game states."""
    if random.random() < 0.7:
        raise NetworkTimeoutError("Packet loss detected during sync")
    return {"status": "synced", "latency": 25}

if __name__ == "__main__":
    try:
        print(fetch_server_state("https://api.game-node.io"))
    except Exception as err:
        print(f"Critical sync failure: {err}")