import time
import functools
from collections import deque

class FrameProcessor:
    def __init__(self, capacity=60):
        self.history = deque(maxlen=capacity)
        self._enabled = True

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not self._enabled:
                return func(*args, **kwargs)
            start = time.perf_counter()
            result = func(*args, **kwargs)
            self.history.append(time.perf_counter() - start)
            return result
        return wrapper

    @property
    def average_latency(self):
        return sum(self.history) / len(self.history) if self.history else 0

    def toggle_telemetry(self, state: bool):
        self._enabled = state

def batch_process(data, chunk_size=1024):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def sanitize_frame_data(payload: dict) -> dict:
    return {k: v for k, v in payload.items() if v is not None}

class PerformanceEngine:
    def __init__(self):
        self.telemetry = FrameProcessor()
        self.pipeline = []

    def execute(self, task, *args):
        try:
            return task(*args)
        except Exception as e:
            print(f'Engine failure: {e}')
            return None