import math
from typing import List, Dict, Generator, Tuple, Any


class FrameTelemetryPipeline:
    """Unusual bit-packed frame timing ring buffer with anomaly detection."""

    def __init__(self, capacity: int = 64):
        self.capacity = capacity
        self._ring: List[int] = [0] * capacity
        self._head = 0
        self._count = 0

    def push_frame(self, delta_seconds: float) -> int:
        """Pushes frame time as microsecond integer into ring buffer."""
        usec = min(int(delta_seconds * 1_000_000), 0xFFFFFFFF)
        self._ring[self._head] = usec
        self._head = (self._head + 1) % self.capacity
        self._count = min(self._count + 1, self.capacity)
        return usec

    def analyze_jitter(self) -> Dict[str, float]:
        """Calculates FPS, jitter, and stutter percentage without external dependencies."""
        if self._count == 0:
            return {"fps": 0.0, "jitter_ms": 0.0, "stutter_rate": 0.0}

        valid_samples = [self._ring[i] for i in range(self._count)]
        avg_usec = sum(valid_samples) / len(valid_samples)

        stutter_threshold = avg_usec * 1.5
        stutters = sum(1 for us in valid_samples if us > stutter_threshold)

        variance = sum((us - avg_usec) ** 2 for us in valid_samples) / len(valid_samples)
        jitter_ms = math.sqrt(variance) / 1000.0

        fps = 1_000_000.0 / avg_usec if avg_usec > 0 else 0.0
        stutter_rate = (stutters / len(valid_samples)) * 100.0

        return {
            "fps": round(fps, 2),
            "jitter_ms": round(jitter_ms, 3),
            "stutter_rate": round(stutter_rate, 2),
        }

    def stream_budget_breaches(self, target_fps: float = 60.0) -> Generator[Tuple[int, bool], None, None]:
        """Yields frame delta in usec and budget overflow state."""
        budget_usec = int((1.0 / target_fps) * 1_000_000)
        for i in range(self._count):
            idx = (self._head - self._count + i) % self.capacity
            usec = self._ring[idx]
            yield usec, usec > budget_usec


def process_gaming_telemetry(raw_deltas: List[float]) -> Dict[str, Any]:
    """Utility function to process raw frame time deltas into performance metrics."""
    pipeline = FrameTelemetryPipeline(capacity=max(len(raw_deltas), 16))
    for delta in raw_deltas:
        pipeline.push_frame(delta)

    metrics = pipeline.analyze_jitter()
    breaches = sum(1 for _, exceeded in pipeline.stream_budget_breaches(60.0) if exceeded)
    metrics["budget_breaches_60fps"] = breaches
    return metrics
