import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, method='GET', retries=3, delay=2, **kwargs):
    for attempt in range(retries):
        try:
            if method == 'GET':
                response = requests.get(url, **kwargs)
            elif method == 'POST':
                response = requests.post(url, **kwargs)
            else:
                raise ValueError('Unsupported method: {}'.format(method))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Attempt {attempt + 1} failed: {e}')
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise NetworkError(f'All {retries} attempts failed.')