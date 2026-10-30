import collections
import statistics
from typing import Any, Callable, Dict, Iterable, List


class FrameStreamProcessor:
    """Stream processor for game frame timings and telemetry analysis."""

    def __init__(self, window_size: int = 120):
        self.window_size = window_size
        self._pipeline: List[Callable[[Dict[str, Any]], Dict[str, Any]]] = []
        self._bind_pipeline_stages()

    def _bind_pipeline_stages(self) -> None:
        self._pipeline = [
            self._calculate_fps,
            self._analyze_stutter,
            self._calculate_jitter,
        ]

    def _calculate_fps(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        ms = payload["delta_ms"]
        payload["fps"] = round(1000.0 / ms, 2) if ms > 0 else 0.0
        return payload

    def _analyze_stutter(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        ms = payload["delta_ms"]
        payload["is_stutter"] = ms > 26.67
        payload["stutter_factor"] = max(0.0, (ms - 16.67) / 16.67)
        return payload

    def _calculate_jitter(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        payload["jitter_ms"] = round(abs(payload["delta_ms"] - 16.67), 3)
        return payload

    def process_telemetry(self, raw_frames: Iterable[float]) -> Iterable[Dict[str, Any]]:
        history = collections.deque(maxlen=self.window_size)
        for frame_time in raw_frames:
            payload = {"delta_ms": frame_time}
            for stage in self._pipeline:
                payload = stage(payload)

            history.append(frame_time)
            if len(history) >= 10:
                sorted_buf = sorted(history)
                idx = int(len(sorted_buf) * 0.99)
                payload["p99_ms"] = round(sorted_buf[idx], 2)
            else:
                payload["p99_ms"] = frame_time

            yield payload
