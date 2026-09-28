import time
from typing import Generator

class PrecisionPacer:
    """Adaptive hybrid spin-lock frame rate controller with drift correction."""
    def __init__(self, target_fps: float):
        self.target_frame_time = 1.0 / target_fps
        self.spin_threshold = 0.0015
        self.accumulated_drift = 0.0
        self.last_tick = time.perf_counter()

    def tick(self) -> Generator[float, None, None]:
        """Generates precise frame delta times while maintaining target pace."""
        while True:
            now = time.perf_counter()
            adjusted_target = self.target_frame_time - self.accumulated_drift
            elapsed = now - self.last_tick
            remaining = adjusted_target - elapsed

            if remaining > 0:
                if remaining > self.spin_threshold:
                    time.sleep(remaining - self.spin_threshold)
                
                while time.perf_counter() - self.last_tick < adjusted_target:
                    pass

            actual_now = time.perf_counter()
            dt = actual_now - self.last_tick
            self.accumulated_drift = dt - self.target_frame_time
            self.last_tick = actual_now
            yield dt