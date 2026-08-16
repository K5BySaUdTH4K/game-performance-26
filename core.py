import time
import random
import requests

def retry_decorator(max_attempts=5, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    attempts += 1
                    wait_time = delay * (2 ** attempts) + random.uniform(0, 1)
                    print(f'Attempt {attempts} failed: {e}. Retrying in {wait_time:.2f} seconds...')
                    time.sleep(wait_time)
            print('Max attempts reached. Operation failed.')
            return None  # Or raise an exception if needed
        return wrapper
    return decorator

@retry_decorator(max_attempts=3, delay=2)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# Example usage
if __name__ == '__main__':
    data = fetch_data('https://jsonplaceholder.typicode.com/todos/1')
    print(data)