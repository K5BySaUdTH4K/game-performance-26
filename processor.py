import time
import random

class NetworkError(Exception):
    pass

def mock_network_call():
    if random.choice([True, False]):
        raise NetworkError("Network failure occurred.")
    return "Network operation successful."

def retry_with_backoff(retries, backoff_factor):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except NetworkError as e:
                    attempt += 1
                    delay = backoff_factor * (2 ** (attempt - 1))
                    print(f"Attempt {attempt} failed: {e}. Retrying in {delay} seconds.")
                    time.sleep(delay)
            raise NetworkError("All retries failed.")
        return wrapper
    return decorator

@retry_with_backoff(retries=5, backoff_factor=1)
def perform_network_operation():
    return mock_network_call()

if __name__ == '__main__':
    try:
        result = perform_network_operation()
        print(result)
    except NetworkError as e:
        print(f"Final error after retries: {e}")