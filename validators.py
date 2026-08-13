import time
import random

class NetworkError(Exception):
    pass

def retry_on_failure(max_retries, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except NetworkError:
                    attempts += 1
                    print(f'Attempt {attempts} failed, retrying in {delay} seconds...')
                    time.sleep(delay)
                    delay *= 2  # Exponential backoff
            raise NetworkError(f'Failed after {max_retries} attempts')
        return wrapper
    return decorator

@retry_on_failure(max_retries=5, delay=1)
def fetch_data_from_server():
    if random.random() < 0.7:  # Simulate a failure 70% of the time
        raise NetworkError('Network issue')
    return {'data': 'sample data'}

if __name__ == '__main__':
    try:
        result = fetch_data_from_server()
        print(result)
    except NetworkError as e:
        print(e)