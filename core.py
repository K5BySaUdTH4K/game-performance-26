from dataclasses import dataclass
from collections import deque
from typing import Generator, List, Tuple

@dataclass
class FrameSample:
    """Represents a single telemetry snapshot for frame timing metrics."""
    frame_id: int
    delta_ms: float
    gpu_load: float

class FramePacerEngine:
    """Adaptive frame-rate pacing engine using a dynamic rolling window.
    
    Calculates dynamic render scaling adjustments and target target sleep
    intervals based on real-time variance in GPU frame spikes.
    """
    def __init__(self, target_fps: float = 60.0, history_depth: int = 120) -> None:
        self.target_delta_ms: float = 1000.0 / target_fps
        self._history: deque = deque(maxlen=history_depth)
        self._scale_factor: float = 1.0

    def ingest_telemetry(self, frame_id: int, delta_ms: float, gpu_load: float) -> FrameSample:
        """Records frame telemetry and appends it to the rolling window."""
        sample = FrameSample(frame_id, delta_ms, gpu_load)
        self._history.append(sample)
        return sample

    def compute_adjustments(self) -> Tuple[float, float]:
        """Calculates dynamic resolution scale and frame sleep duration.
        
        Returns:
            Tuple[float, float]: Dynamic resolution multiplier (0.5 to 1.5)
            and recommended frame pacing delay in milliseconds.
        """
        if not self._history:
            return 1.0, 0.0

        avg_delta = sum(s.delta_ms for s in self._history) / len(self._history)
        avg_load = sum(s.gpu_load for s in self._history) / len(self._history)
        
        variance = abs(avg_delta - self.target_delta_ms)
        if avg_load > 90.0 or variance > 4.0:
            self._scale_factor = max(0.5, self._scale_factor - 0.05)
        elif avg_load < 70.0 and variance < 1.0:
            self._scale_factor = min(1.5, self._scale_factor + 0.02)
            
        pacing_delay = max(0.0, self.target_delta_ms - avg_delta)
        return round(self._scale_factor, 3), round(pacing_delay, 2)

    def stream_optimizations(self, raw_frames: List[Tuple[int, float, float]]) -> Generator[Tuple[int, float, float], None, None]:
        """Streams processed optimization signals for a sequence of frame metrics."""
        for fid, d_ms, load in raw_frames:
            self.ingest_telemetry(fid, d_ms, load)
            scale, delay = self.compute_adjustments()
            yield (fid, scale, delay)
