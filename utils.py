import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=5, delay=2):
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()
        except RequestException as e:
            attempts += 1
            if attempts < max_retries:
                print(f"Attempt {attempts} failed: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print(f"Max retries reached. Last error: {e}")
                return None
