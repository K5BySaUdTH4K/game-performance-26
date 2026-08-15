import time
import random

class NetworkError(Exception):
    pass

class Retry:
    def __init__(self, retries=3, delay=1, backoff=2):
        self.retries = retries
        self.delay = delay
        self.backoff = backoff

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < self.retries:
                try:
                    return func(*args, **kwargs)
                except NetworkError as e:
                    attempts += 1
                    wait_time = self.delay * (self.backoff ** (attempts - 1))
                    print(f'Attempt {attempts} failed: {e}. Retrying in {wait_time} seconds...')
                    time.sleep(wait_time)
            raise NetworkError(f'Failed after {self.retries} attempts.')
        return wrapper

@Retry(retries=5, delay=2)
def fetch_data(url):
    if random.choice([True, False]):  # Simulate intermittent network failure
        raise NetworkError('Could not reach the server.')
    return {'data': 'response from ' + url}

# Example usage:
# print(fetch_data('http://example.com'))
