import sys
import math
import json
import time
from typing import Any, Dict, List, Optional


class PerformanceLogger:
    """Ring-buffer performance telemetry logger with dynamic edge-case resilience."""

    def __init__(self, capacity: int = 1000, fallback_stream=sys.stderr):
        self.capacity = max(10, capacity)
        self.fallback_stream = fallback_stream
        self.buffer: List[Dict[str, Any]] = []
        self.corrupt_entries_count = 0

    def sanitize_metric(self, name: str, value: Any) -> float:
        """Sanitizes volatile values like NaN, Inf, or malformed numerical types."""
        try:
            val = float(value)
            if math.isnan(val) or math.isinf(val):
                self.corrupt_entries_count += 1
                return 0.0 if math.isnan(val) else (9999.0 if val > 0 else -1.0)
            return max(0.0, val) if "time" in name or "fps" in name else val
        except (ValueError, TypeError):
            self.corrupt_entries_count += 1
            return -999.0

    def log_frame(self, frame_id: int, frame_time_ms: float, fps: float, extra: Optional[Dict] = None) -> bool:
        """Logs frame timing safely while catching non-serializable payload inputs."""
        safe_frame_id = frame_id if isinstance(frame_id, int) and frame_id >= 0 else -1
        safe_ft = self.sanitize_metric("frame_time", frame_time_ms)
        safe_fps = self.sanitize_metric("fps", fps)
        
        extra_data = {}
        if isinstance(extra, dict):
            for k, v in extra.items():
                try:
                    json.dumps(v)
                    extra_data[str(k)] = v
                except (TypeError, OverflowError):
                    extra_data[str(k)] = f"<Unserializable:{type(v).__name__}>"

        entry = {
            "timestamp": time.time(),
            "frame": safe_frame_id,
            "ft_ms": safe_ft,
            "fps": safe_fps,
            "metrics": extra_data
        }

        if len(self.buffer) >= self.capacity:
            self.buffer.pop(0)

        self.buffer.append(entry)
        return True

    def flush_to_file(self, filepath: str) -> bool:
        """Flushes buffered frame metrics to disk with emergency stream fallback."""
        try:
            with open(filepath, "a", encoding="utf-8") as f:
                for record in self.buffer:
                    f.write(json.dumps(record) + "\n")
            self.buffer.clear()
            return True
        except (OSError, PermissionError, TypeError) as err:
            self.fallback_stream.write(f"[EMERGENCY_LOG] Write failed ({err}). Dumping ring-buffer:\n")
            for record in self.buffer:
                self.fallback_stream.write(f"{record}\n")
            self.buffer.clear()
            return False
