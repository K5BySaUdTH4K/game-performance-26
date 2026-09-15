import time
import json
from datetime import datetime

class PerformanceTracker:
    def __init__(self, buffer_size=10):
        self.buffer = []
        self.buffer_size = buffer_size

    def log_frame(self, frame_time: float, gpu_temp: float, fps: int):
        timestamp = datetime.utcnow().isoformat()
        entry = {
            "ts": timestamp,
            "ms": round(frame_time, 4),
            "gpu": gpu_temp,
            "fps": fps
        }
        self.buffer.append(entry)
        if len(self.buffer) >= self.buffer_size:
            self.flush()

    def flush(self):
        if not self.buffer:
            return
        try:
            with open('metrics.jsonl', 'a') as f:
                for entry in self.buffer:
                    f.write(json.dumps(entry) + '\n')
            self.buffer.clear()
        except IOError as e:
            print(f"Critical performance logging failure: {e}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flush()