import time
import random

def compute_intensive_task(data):
    return sum(x**2 for x in data)

class GameProcessor:
    def __init__(self, data):
        self.data = data
        self.results = []

    def run(self):
        start_time = time.time()
        print('Starting computation...')
        self.results = [self.enhanced_compute(chunk) for chunk in self.chunk_data()]
        end_time = time.time()
        print(f'Computation completed in {end_time - start_time:.2f} seconds')

    def enhanced_compute(self, chunk):
        # Using list comprehension for efficiency
        return compute_intensive_task(chunk)

    def chunk_data(self):
        chunk_size = 1000  # Define chunk size
        for i in range(0, len(self.data), chunk_size):
            yield self.data[i:i + chunk_size]

if __name__ == '__main__':
    data = [random.randint(1, 100) for _ in range(10000)]
    processor = GameProcessor(data)
    processor.run()