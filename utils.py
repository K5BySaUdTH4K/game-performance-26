import time
import random
import requests

def retry_on_failure(max_retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    attempts += 1
                    print(f'Attempt {attempts} failed: {e}')
                    time.sleep(delay + random.uniform(0, 1))  # Exponential backoff
            print('Max retries reached. Giving up.')
            return None
        return wrapper
    return decorator

@retry_on_failure(max_retries=5, delay=1)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for 4xx/5xx response
    return response.json()

if __name__ == '__main__':
    data = fetch_data('https://api.example.com/data')
    print(data)  
