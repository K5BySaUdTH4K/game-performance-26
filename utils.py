import time
import random

class NetworkError(Exception):
    pass

def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except NetworkError as e:
                    attempts += 1
                    print(f'Attempt {attempts} failed: {e}')
                    if attempts < retries:
                        time.sleep(delay)
            raise NetworkError(f'Failed after {retries} attempts')
        return wrapper
    return decorator

@retry_on_failure(retries=5, delay=1)
def fetch_data():
    if random.choice([True, False]):  # Simulate network failure
        raise NetworkError('Simulated network failure')
    return 'Data fetched successfully!'

if __name__ == '__main__':
    print(fetch_data())