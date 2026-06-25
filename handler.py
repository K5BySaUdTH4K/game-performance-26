import requests
import time

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=2, backoff=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError) as e:
            if attempt < retries - 1:
                time.sleep(delay)
                delay *= backoff  # Exponential backoff
            else:
                raise NetworkError(f'Failed to fetch {url}: {str(e)}') from e

# Example usage:
# result = retry_request('https://api.example.com/data')