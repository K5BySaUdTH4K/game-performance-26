import math
from collections import deque
from typing import Dict, Generator, Any, Optional


class TelemetryFrameHandler:
    """Processes real-time frame timing data to detect micro-stutters and 1% lows."""

    def __init__(self, window_size: int = 120, stutter_threshold_ms: float = 25.0):
        self.window_size = window_size
        self.stutter_threshold_ms = stutter_threshold_ms
        self._frame_times: deque[float] = deque(maxlen=window_size)
        self._stutter_count: int = 0
        self._total_frames: int = 0

    def __call__(self, frame_delta_ms: float) -> Dict[str, Any]:
        """Ingest frame duration and calculate rolling window telemetry."""
        self._total_frames += 1
        self._frame_times.append(frame_delta_ms)

        if frame_delta_ms > self.stutter_threshold_ms:
            self._stutter_count += 1

        sorted_frames = sorted(self._frame_times)
        p99_idx = max(0, math.ceil(len(sorted_frames) * 0.99) - 1)
        p99_frame_time = sorted_frames[p99_idx]

        avg_time = sum(self._frame_times) / len(self._frame_times)
        avg_fps = 1000.0 / avg_time if avg_time > 0 else 0.0
        one_percent_low = 1000.0 / p99_frame_time if p99_frame_time > 0 else 0.0

        variance = sum((x - avg_time) ** 2 for x in self._frame_times) / len(self._frame_times)
        jitter = math.sqrt(variance)

        return {
            "current_fps": round(1000.0 / frame_delta_ms, 2) if frame_delta_ms > 0 else 0.0,
            "avg_fps": round(avg_fps, 2),
            "one_percent_low": round(one_percent_low, 2),
            "jitter_ms": round(jitter, 3),
            "stutter_rate": round(self._stutter_count / self._total_frames, 4),
        }


def frame_stream_processor() -> Generator[Optional[Dict[str, Any]], float, None]:
    """Stateful coroutine pipeline for non-blocking telemetry frame stream processing."""
    handler = TelemetryFrameHandler()
    metrics: Optional[Dict[str, Any]] = None
    while True:
        frame_time_ms = yield metrics
        if frame_time_ms is None or frame_time_ms <= 0:
            continue
        metrics = handler(frame_time_ms)
