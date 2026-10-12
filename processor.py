import struct
from collections import deque
from typing import Generator, Dict, Any

class FrameTelemetryProcessor:
    """Processes packed binary frame telemetry streams to detect micro-stutters and calculate frame metrics."""
    
    def __init__(self, frame_budget_ms: float = 16.67, window_size: int = 100):
        self.target_frame_time = frame_budget_ms
        self.window_size = window_size
        self._fmt = "<I f H B"  # frame_id (uint32), frame_time (float), draw_calls (uint16), flags (uint8)
        self._struct_size = struct.calcsize(self._fmt)

    def unpack_stream(self, raw_bytes: bytes) -> Generator[Dict[str, Any], None, None]:
        """Decodes raw byte streams using zero-copy memoryviews."""
        view = memoryview(raw_bytes)
        for offset in range(0, len(view) - self._struct_size + 1, self._struct_size):
            frame_id, ft, draw_calls, flags = struct.unpack_from(self._fmt, view, offset)
            yield {
                "frame_id": frame_id,
                "frame_time_ms": round(ft, 3),
                "draw_calls": draw_calls,
                "gpu_bound": bool(flags & 0x01),
                "cpu_bound": bool(flags & 0x02),
            }

    def compute_performance_metrics(self, raw_bytes: bytes) -> Dict[str, Any]:
        """Calculates 1% lows, average FPS, and micro-stutter frequency from packed telemetry."""
        history: deque = deque(maxlen=self.window_size)
        stutter_count = 0
        total_frames = 0
        
        for frame in self.unpack_stream(raw_bytes):
            ft = frame["frame_time_ms"]
            history.append(ft)
            total_frames += 1
            if ft > self.target_frame_time * 1.5:
                stutter_count += 1
                
        if not history:
            return {"avg_fps": 0.0, "p99_low_fps": 0.0, "stutter_rate": 0.0, "total_frames": 0}
            
        sorted_history = sorted(history)
        p99_idx = max(0, int(len(sorted_history) * 0.01))
        p99_frame_time = sorted_history[-1 - p99_idx] if p99_idx < len(sorted_history) else sorted_history[0]
        avg_ft = sum(history) / len(history)
        
        return {
            "avg_fps": round(1000.0 / avg_ft, 1) if avg_ft > 0 else 0.0,
            "p99_low_fps": round(1000.0 / p99_frame_time, 1) if p99_frame_time > 0 else 0.0,
            "stutter_rate": round(stutter_count / total_frames, 4) if total_frames else 0.0,
            "total_frames": total_frames,
            "max_frame_time_ms": max(sorted_history),
        }
