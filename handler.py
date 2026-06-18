import time
import random
import requests

def retry_request(url, retries=3, backoff_factor=0.5):
    for i in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f'HTTP error: {e}')
        except requests.exceptions.RequestException as e:
            print(f'Request failed: {e}')
        time.sleep(backoff_factor * (2 ** i))  # Exponential backoff
    raise Exception('Max retries exceeded')

# Example usage
if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print('Data:', data)
    except Exception as e:
        print('Failed to retrieve data:', e)