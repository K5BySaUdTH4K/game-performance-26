from typing import Dict, List, Optional, Union
import time

class FrameLatencyHandler:
    def __init__(self, threshold_ms: float = 16.67) -> None:
        self.threshold: float = threshold_ms
        self.history: List[float] = []

    def process_frame(self, frame_time: float) -> Dict[str, Union[bool, float]]:
        """
        Analyzes frame timing and detects potential performance stutters.
        Returns a dict containing flag status and current delta.
        """
        is_stutter: bool = frame_time > self.threshold
        self.history.append(frame_time)
        
        return {
            "is_stutter": is_stutter,
            "delta": frame_time - self.threshold,
            "avg": sum(self.history) / len(self.history)
        }

    def clear_metrics(self) -> None:
        """
        Resets the latency history cache to free memory.
        """
        self.history.clear()

def get_performance_snapshot(data: Optional[Dict[str, float]]) -> str:
    """
    Generates a human-readable performance string from raw frame data.
    """
    if not data:
        return "idle"
    return f"active: {data.get('fps', 0)} fps"