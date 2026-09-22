import time
import functools

class PerformanceHandler:
    def __init__(self, threshold=0.016):
        self.threshold = threshold
        self.registry = {}

    def monitor(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            if elapsed > self.threshold:
                self.registry[func.__name__] = elapsed
            return result
        return wrapper

    def flush_metrics(self):
        report = {k: f"{v:.4f}s" for k, v in self.registry.items()}
        self.registry.clear()
        return report

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def heavy_load_simulation():
    return sum(i * i for i in range(1000000))

handler = PerformanceHandler()

@handler.monitor
def execute_game_tick():
    return heavy_load_simulation()

if __name__ == "__main__":
    execute_game_tick()
    print(f"Performance bottlenecks: {handler.flush_metrics()}")