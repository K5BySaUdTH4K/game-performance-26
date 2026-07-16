import time
import requests

class NetworkError(Exception):
    pass

def retry_on_failure(max_retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (requests.ConnectionError, requests.Timeout) as e:
                    if attempt < max_retries - 1:
                        print(f'Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...')
                        time.sleep(delay)
                    else:
                        raise NetworkError(f'Operation failed after {max_retries} attempts.') from e
        return wrapper
    return decorator

@retry_on_failure(max_retries=5, delay=3)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()