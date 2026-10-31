import time
from collections import deque
from typing import Callable, Generator, Tuple

def smooth_fps_calculator(window_size: int = 60) -> Generator[float, float, None]:
    """Coroutine generator yielding rolling average FPS from streamed delta times."""
    history: deque[float] = deque(maxlen=window_size)
    dt = yield 0.0
    while True:
        if dt and dt > 0:
            history.append(dt)
        avg_dt = sum(history) / len(history) if history else 0.01667
        dt = yield (1.0 / avg_dt) if avg_dt > 0 else 0.0

def isolate_frame_spikes(frame_times: list[float], threshold_ms: float = 33.3) -> list[Tuple[int, float]]:
    """Identify frame indices and duration where frame time exceeds latency target."""
    return [(idx, ft) for idx, ft in enumerate(frame_times) if (ft * 1000.0) > threshold_ms]

class FrameProfileContext:
    """Context manager measuring execution duration in milliseconds for performance tracking."""
    def __init__(self, tag: str, callback: Callable[[str, float], None] | None = None):
        self.tag = tag
        self.callback = callback
        self.start_ns = 0

    def __enter__(self):
        self.start_ns = time.perf_counter_ns()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_ms = (time.perf_counter_ns() - self.start_ns) / 1e6
        if self.callback:
            self.callback(self.tag, elapsed_ms)
        return False

def pack_render_flags(*flags: bool) -> int:
    """Pack boolean rendering feature toggles into a single integer bitfield."""
    return sum(1 << i for i, flag in enumerate(flags) if flag)

def unpack_render_flags(mask: int, count: int) -> list[bool]:
    """Unpack integer bitfield back into individual boolean rendering feature flags."""
    return [bool(mask & (1 << i)) for i in range(count)]
