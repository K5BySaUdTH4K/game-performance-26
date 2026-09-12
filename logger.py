import time
import functools
import logging

logger = logging.getLogger('game-performance-26')

def retry_on_failure(max_attempts=3, delay=1.5, backoff=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        logger.error(f'Final attempt failed for {func.__name__}: {e}')
                        raise
                    logger.warning(f'Attempt {attempt + 1} failed, retrying in {current_delay}s...')
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_on_failure(max_attempts=4)
def perform_network_request(endpoint):
    # Simulate volatile network state
    import random
    if random.random() < 0.7:
        raise ConnectionError('Packet loss encountered')
    return {'status': 200, 'data': 'payload'}