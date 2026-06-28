import time
import random

class NetworkError(Exception):
    pass


def retry(max_attempts=3, delay=2, backoff=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except NetworkError:
                    attempts += 1
                    wait_time = delay * (backoff ** (attempts - 1))
                    print(f'Attempt {attempts} failed. Retrying in {wait_time} seconds...')
                    time.sleep(wait_time)
                    if attempts == max_attempts:
                        print('Max attempts reached. Operation failed.')
                        raise
        return wrapper
    return decorator

@retry(max_attempts=5, delay=1)
def network_operation():
    if random.random() < 0.7:
        raise NetworkError('Network failure!')
    return 'Success!'

if __name__ == '__main__':
    try:
        result = network_operation()
        print(result)
    except NetworkError:
        print('Final failure. All retries exhausted.')