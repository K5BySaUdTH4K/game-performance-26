import time
from typing import Callable, Generator, Optional


def frame_budget_tracker(target_fps: float = 60.0) -> Generator[float, float, None]:
    """Generator yielding remaining time budget (in ms) per frame given delta time inputs."""
    target_ms = 1000.0 / max(target_fps, 1.0)
    accumulated_variance = 0.0
    
    while True:
        delta_ms = yield accumulated_variance
        if delta_ms is None:
            delta_ms = target_ms
        
        frame_time_diff = target_ms - delta_ms
        # Dampen variance drift to prevent sudden rubber-banding
        accumulated_variance = (accumulated_variance * 0.8) + (frame_time_diff * 0.2)


def create_fps_smoother(alpha: float = 0.15) -> Callable[[float], float]:
    """Returns a stateful function calculating dynamic exponential moving average FPS."""
    last_fps: Optional[float] = None

    def update(raw_fps: float) -> float:
        nonlocal last_fps
        if last_fps is None:
            last_fps = raw_fps
        else:
            last_fps = (alpha * raw_fps) + ((1.0 - alpha) * last_fps)
        return round(last_fps, 2)

    return update


def evaluate_tier_scaling(fps: float, target: float = 60.0) -> str:
    """Uses bitwise performance buckets to determine render tier shifts."""
    ratio = min(max(fps / max(target, 1.0), 0.0), 2.0)
    # Convert ratio into a 3-bit status mask
    mask = (1 if ratio >= 0.95 else 0) | (2 if ratio >= 0.75 else 0) | (4 if ratio >= 0.50 else 0)
    
    tier_map = {
        0b111: "ULTRA_TIER",
        0b110: "HIGH_TIER",
        0b100: "MEDIUM_TIER",
        0b000: "LOW_TIER"
    }
    return tier_map.get(mask, "CRITICAL_TIER")
