import time
import functools
import random
import logging

logger = logging.getLogger('game-performance-26')

def backoff_retry(retries=3, base_delay=0.5, max_delay=5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f'Critical network failure after {retries} attempts: {e}')
                        raise
                    
                    sleep_time = min(max_delay, base_delay * (2 ** (attempt - 1))) + (random.uniform(0, 0.1))
                    logger.warning(f'Retrying {func.__name__} in {sleep_time:.2f}s... (attempt {attempt})')
                    time.sleep(sleep_time)
        return wrapper
    return decorator

@backoff_retry(retries=5)
def sync_game_state(payload):
    # Simulate volatile network state in game-performance-26
    if random.random() < 0.7:
        raise ConnectionError('Packet drop detected')
    return {'status': 'synced', 'timestamp': time.time()}