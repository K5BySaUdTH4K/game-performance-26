from typing import Dict, Generator, List


class FrameTimeBuffer:
    """Ring buffer for gaming telemetry with dynamic window ordering."""

    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self._buffer: List[float] = []
        self._ptr: int = 0

    def push(self, frame_time_ms: float) -> None:
        if len(self._buffer) < self.capacity:
            self._buffer.append(frame_time_ms)
        else:
            self._buffer[self._ptr] = frame_time_ms
            self._ptr = (self._ptr + 1) % self.capacity

    def __len__(self) -> int:
        return len(self._buffer)

    @property
    def ordered_frames(self) -> List[float]:
        return self._buffer[self._ptr :] + self._buffer[: self._ptr]


def compute_performance_stats(frame_times: List[float]) -> Dict[str, float]:
    """Calculates FPS averages, 1% low, 0.1% low, and stutter severity."""
    if not frame_times:
        return {"avg_fps": 0.0, "low_1pct": 0.0, "low_01pct": 0.0, "stutter_rate": 0.0}

    sorted_times = sorted(frame_times)
    count = len(sorted_times)

    avg_ft = sum(sorted_times) / count
    avg_fps = 1000.0 / avg_ft if avg_ft > 0 else 0.0

    idx_1pct = max(0, int(count * 0.99) - 1)
    idx_01pct = max(0, int(count * 0.999) - 1)

    ft_1pct = sorted_times[idx_1pct]
    ft_01pct = sorted_times[idx_01pct]

    low_1pct = 1000.0 / ft_1pct if ft_1pct > 0 else 0.0
    low_01pct = 1000.0 / ft_01pct if ft_01pct > 0 else 0.0

    median_ft = sorted_times[count // 2]
    stutters = sum(1 for ft in frame_times if ft > median_ft * 1.8)
    stutter_rate = (stutters / count) * 100.0

    return {
        "avg_fps": round(avg_fps, 2),
        "low_1pct": round(low_1pct, 2),
        "low_01pct": round(low_01pct, 2),
        "stutter_rate": round(stutter_rate, 2),
    }


def analyze_frame_stream(stream: Generator[float, None, None], window: int = 120):
    """Processes streaming frame telemetry using windowed metrics."""
    buf = FrameTimeBuffer(capacity=window)
    for sample in stream:
        buf.push(sample)
        if len(buf) == window:
            yield compute_performance_stats(buf.ordered_frames)
