import time
import threading
from typing import Dict, Any

class PerformanceEngine:
    def __init__(self, target_fps: int = 60):
        self.target_frame_time = 1.0 / target_fps
        self.metrics: Dict[str, Any] = {}
        self._lock = threading.Lock()

    def monitor_tick(self, func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            with self._lock:
                self.metrics[func.__name__] = duration
            return result
        return wrapper

    def cleanup_resources(self):
        with self._lock:
            self.metrics.clear()

class FrameManager:
    @staticmethod
    def sync_frame_rate(start_time: float, engine: PerformanceEngine):
        elapsed = time.perf_counter() - start_time
        sleep_time = engine.target_frame_time - elapsed
        if sleep_time > 0:
            time.sleep(sleep_time)

def initialize_game_core():
    engine = PerformanceEngine()
    return engine

if __name__ == '__main__':
    engine = initialize_game_core()
    print(f'Game engine initialized with target: {1/engine.target_frame_time}fps')