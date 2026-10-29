from collections import deque
from typing import Dict, Generator, List, Tuple, TypeAlias, Union
import time

Milliseconds: TypeAlias = float
FPS: TypeAlias = float
TelemetryFrame: TypeAlias = Tuple[float, Milliseconds]


class FrameBufferHandler:
    """A rolling telemetry buffer for tracking game engine frame metrics.

    Stores recent frame render durations and dynamically calculates frame pacing,
    stutter frequencies, and percentile performance thresholds.
    """

    def __init__(self, capacity: int = 120) -> None:
        self._capacity: int = max(10, capacity)
        self._frames: deque[TelemetryFrame] = deque(maxlen=self._capacity)
        self._jitter_accumulator: Milliseconds = 0.0

    def record_frame(self, frame_time_ms: Milliseconds) -> TelemetryFrame:
        """Appends a new frame duration measurement to the rolling buffer.

        Args:
            frame_time_ms: Render duration of the completed frame in milliseconds.

        Returns:
            A tuple containing (timestamp, frame_time_ms).
        """
        now = time.monotonic()
        entry: TelemetryFrame = (now, max(0.001, frame_time_ms))
        if self._frames:
            prev_delta = self._frames[-1][1]
            self._jitter_accumulator += abs(frame_time_ms - prev_delta)
        self._frames.append(entry)
        return entry

    @property
    def current_fps(self) -> FPS:
        """Computes the instantaneous FPS derived from the latest recorded frame."""
        if not self._frames:
            return 0.0
        latest_ms = self._frames[-1][1]
        return 1000.0 / latest_ms

    def analyze_pacing(self, percentile: float = 99.0) -> Dict[str, Union[float, int]]:
        """Calculates pacing statistics across the current telemetry window.

        Args:
            percentile: Target percentile latency boundary (e.g., 99.0 for 1% lows).

        Returns:
            Dictionary containing average FPS, frame time variance, jitter, and low percentiles.
        """
        if not self._frames:
            return {"avg_fps": 0.0, "jitter_ms": 0.0, "percentile_ms": 0.0, "frame_count": 0}

        times: List[Milliseconds] = sorted([f[1] for f in self._frames])
        total_time: Milliseconds = sum(times)
        avg_ms: float = total_time / len(times)
        
        idx = int(len(times) * (percentile / 100.0)) - 1
        percentile_val: Milliseconds = times[max(0, idx)]
        sample_count = len(self._frames)
        avg_jitter = self._jitter_accumulator / max(1, sample_count - 1)

        return {
            "avg_fps": 1000.0 / avg_ms if avg_ms > 0 else 0.0,
            "jitter_ms": round(avg_jitter, 3),
            "percentile_ms": round(percentile_val, 3),
            "frame_count": sample_count,
        }

    def render_lag_spike_stream(self, threshold_ms: Milliseconds) -> Generator[TelemetryFrame, None, None]:
        """Yields any frames from the buffer exceeding the lag spike threshold duration."""
        for timestamp, duration in list(self._frames):
            if duration >= threshold_ms:
                yield (timestamp, duration)
