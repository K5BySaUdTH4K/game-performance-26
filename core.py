import time
import numpy as np

def optimize_performance(data):
    start_time = time.time()
    # Using numpy for optimized calculations
    array_data = np.array(data)
    result = np.mean(array_data)  # Calculate mean efficiently
    execution_time = time.time() - start_time
    print(f"Execution Time: {execution_time:.4f} seconds")
    return result

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Mean: {optimize_performance(sample_data)}")