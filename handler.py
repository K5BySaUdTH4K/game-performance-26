import time
import collections
from typing import Dict, List, Callable

class EventStreamHandler:
    def __init__(self, buffer_limit: int = 100):
        self.queue = collections.deque(maxlen=buffer_limit)
        self.registry: Dict[str, List[Callable]] = collections.defaultdict(list)

    def subscribe(self, event_type: str, callback: Callable):
        self.registry[event_type].append(callback)

    def process_frame(self, frame_data: dict):
        self.queue.append({'ts': time.perf_counter(), 'data': frame_data})
        event = frame_data.get('type')
        if event in self.registry:
            for callback in self.registry[event]:
                try:
                    callback(frame_data)
                except Exception as e:
                    print(f'handler error: {e}')

    def get_latency_stats(self) -> float:
        if len(self.queue) < 2:
            return 0.0
        times = [entry['ts'] for entry in self.queue]
        return (times[-1] - times[0]) / len(times)

    def flush(self):
        self.queue.clear()
        self.registry.clear()

class PerformanceHandler(EventStreamHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.metrics = collections.Counter()

    def track(self, key: str):
        self.metrics[key] += 1

    def summary(self):
        return dict(self.metrics)