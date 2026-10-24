from typing import List, Dict, Optional, Union
import time

class FrameTracker:
    """Calculates performance metrics for game frames."""

    def __init__(self, buffer_size: int = 60) -> None:
        self.buffer_size: int = buffer_size
        self.times: List[float] = []

    def record_frame(self) -> None:
        """Registers current execution timestamp to buffer."""
        self.times.append(time.perf_counter())
        if len(self.times) > self.buffer_size:
            self.times.pop(0)

    def get_fps(self) -> float:
        """Calculates smoothed frames per second."""
        if len(self.times) < 2:
            return 0.0
        duration: float = self.times[-1] - self.times[0]
        return (len(self.times) - 1) / duration if duration > 0 else 0.0

def aggregate_stats(data: Dict[str, Union[int, float]]) -> Optional[str]:
    """Converts performance dictionary into a formatted string."""
    if not data:
        return None
    return " | ".join([f"{k.upper()}: {v:.2f}" for k, v in data.items()])

if __name__ == "__main__":
    tracker = FrameTracker()
    for _ in range(10):
        tracker.record_frame()
        time.sleep(0.016)
    print(f"current metrics: {tracker.get_fps()} fps")