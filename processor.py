import math
from collections import deque
from typing import Dict, List, Tuple, Generator, Any


class TelemetryProcessor:
    """Stream processor for game frame metrics using generator coroutines."""

    FLAG_GPU_BOUND = 1 << 0
    FLAG_CPU_BOUND = 1 << 1
    FLAG_MICRO_STUTTER = 1 << 2
    FLAG_VRAM_PRESSURE = 1 << 3

    def __init__(self, target_fps: float = 60.0, history_seconds: int = 3):
        self.target_frame_ms = 1000.0 / max(1.0, target_fps)
        self.capacity = int(target_fps * history_seconds)
        self._samples: deque = deque(maxlen=self.capacity)
        self._vram_usage: deque = deque(maxlen=self.capacity)

    def frame_ingestor(self) -> Generator[Dict[str, Any], Tuple[float, float, float], None]:
        """Coroutine pipeline yielding frame performance metrics on each send."""
        while True:
            frame_ms, cpu_ms, vram_ratio = yield  # type: ignore
            self._samples.append(frame_ms)
            self._vram_usage.append(vram_ratio)

            gpu_ms = max(0.0, frame_ms - cpu_ms)
            p99_threshold = self._calc_percentile(99.0)
            flags = 0

            if frame_ms > self.target_frame_ms:
                flags |= self.FLAG_GPU_BOUND if gpu_ms > cpu_ms else self.FLAG_CPU_BOUND

            if len(self._samples) > 10 and frame_ms >= p99_threshold and frame_ms > self.target_frame_ms * 1.2:
                flags |= self.FLAG_MICRO_STUTTER

            if vram_ratio > 0.90:
                flags |= self.FLAG_VRAM_PRESSURE

            avg_ms = sum(self._samples) / len(self._samples)
            yield {
                "fps_current": round(1000.0 / max(0.001, frame_ms), 1),
                "fps_avg": round(1000.0 / max(0.001, avg_ms), 1),
                "frame_budget_used": round((frame_ms / self.target_frame_ms) * 100, 2),
                "bottleneck_flags": flags,
                "is_stuttering": bool(flags & self.FLAG_MICRO_STUTTER)
            }

    def _calc_percentile(self, pct: float) -> float:
        if not self._samples:
            return 0.0
        sorted_s = sorted(self._samples)
        k = (len(sorted_s) - 1) * (pct / 100.0)
        f, c = math.floor(k), math.ceil(k)
        if f == c:
            return sorted_s[int(k)]
        return sorted_s[int(f)] * (c - k) + sorted_s[int(c)] * (k - f)


def process_telemetry_batch(raw_frames: List[Tuple[float, float, float]], target_fps: float = 60.0) -> List[Dict[str, Any]]:
    """Helper function executing a batch of raw telemetry inputs through the ingestor coroutine."""
    proc = TelemetryProcessor(target_fps=target_fps)
    ingestor = proc.frame_ingestor()
    results = []

    for sample in raw_frames:
        next(ingestor)
        metrics = ingestor.send(sample)
        results.append(metrics)

    return results
