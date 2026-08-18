import time
import numpy as np

class GameProcessor:
    def __init__(self):
        self.data = np.zeros((1000, 1000))
        self.last_process_time = 0

    def simulate_action(self, x, y):
        # Simulating some heavy computation
        value = (x ** 2 + y ** 2) ** 0.5
        return value

    def process(self):
        start_time = time.time()
        for x in range(self.data.shape[0]):
            for y in range(self.data.shape[1]):
                self.data[x][y] = self.simulate_action(x, y)
        self.last_process_time = time.time() - start_time

    def get_last_process_time(self):
        return self.last_process_time

    def optimize_processing(self):
        # Optimized using vectorization
        coordinates = np.indices(self.data.shape)
        x, y = coordinates
        self.data = np.sqrt(x**2 + y**2)
        self.last_process_time = time.time() - self.last_process_time

# Example usage
if __name__ == '__main__':
    processor = GameProcessor()
    processor.process()
    print(processor.get_last_process_time())
    processor.optimize_processing()
    print(processor.get_last_process_time())