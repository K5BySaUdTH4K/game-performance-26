import math
import statistics
from typing import List, Dict, Union, Any


class TelemetryAnomalousDataError(ValueError):
    """Raised when telemetry payload contains unrecoverable corruption."""
    pass


class FrameTimeProcessor:
    """Processes raw frame times and metrics with defensive edge-case mitigation."""

    def __init__(self, max_history: int = 120, fallback_fps: float = 60.0):
        self.max_history = max_history
        self.fallback_fps = fallback_fps
        self.history: List[float] = []

    def sanitize_frame_time(self, raw_ms: Any) -> float:
        """Sanitizes raw frame time values, handling NaN, Inf, and negative clock skews."""
        try:
            val = float(raw_ms)
            if math.isnan(val) or math.isinf(val):
                raise TelemetryAnomalousDataError(f"Non-finite frame time: {val}")
            if val <= 0.0:
                return 1000.0 / self.fallback_fps
            return min(val, 10000.0)
        except (TypeError, ValueError, TelemetryAnomalousDataError):
            if self.history:
                return statistics.median(self.history)
            return 1000.0 / self.fallback_fps

    def process_batch(self, raw_metrics: List[Dict[str, Any]]) -> Dict[str, Union[float, int]]:
        """Processes a batch of raw telemetry frame dicts, handling missing or corrupted keys."""
        valid_fps_list: List[float] = []
        corrupted_count = 0

        for sample in raw_metrics:
            if not isinstance(sample, dict):
                corrupted_count += 1
                continue

            raw_dt = sample.get("frame_time_ms", sample.get("dt", None))
            if raw_dt is None and "fps" in sample:
                try:
                    fps_val = float(sample["fps"])
                    raw_dt = 1000.0 / fps_val if fps_val > 0 else None
                except (ZeroDivisionError, ValueError, TypeError):
                    raw_dt = None

            safe_dt = self.sanitize_frame_time(raw_dt)
            self.history.append(safe_dt)
            if len(self.history) > self.max_history:
                self.history.pop(0)

            computed_fps = 1000.0 / safe_dt
            valid_fps_list.append(computed_fps)

        if not valid_fps_list:
            return {
                "avg_fps": self.fallback_fps,
                "p1_low_fps": self.fallback_fps,
                "corrupted_samples": corrupted_count
            }

        sorted_fps = sorted(valid_fps_list)
        p1_index = max(0, int(len(sorted_fps) * 0.01))

        return {
            "avg_fps": round(statistics.mean(valid_fps_list), 2),
            "p1_low_fps": round(sorted_fps[p1_index], 2),
            "corrupted_samples": corrupted_count
        }