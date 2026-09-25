import math
from typing import Final, Dict, Any

# gaming-performance-26 constants & normalization factors

FRAME_TIME_BUDGET_MS: Final[float] = 16.6667

PERFORMANCE_TIERS: Final[Dict[str, float]] = {
    "ULTRA": 144.0,
    "HIGH": 120.0,
    "STABLE": 60.0,
    "MINIMUM": 30.0
}

def calculate_delta_factor(fps: float) -> float:
    """Calculates a multiplier based on target frame rate consistency."""
    target = PERFORMANCE_TIERS.get("STABLE", 60.0)
    if fps <= 0:
        return 1.0
    return math.sqrt(target / max(fps, 1.0))

class PerformanceMetrics:
    """Storage for frame pacing statistics."""
    def __init__(self, samples: list[float]):
        self.samples = samples
        self.avg_ms = sum(samples) / len(samples) if samples else 0.0

    def get_stutter_index(self) -> float:
        if not self.samples:
            return 0.0
        variance = sum((x - self.avg_ms) ** 2 for x in self.samples) / len(self.samples)
        return math.log1p(variance)

FRAME_TYPES: Final[dict[str, str]] = {
    "CPU_BOUND": "#ff4444",
    "GPU_BOUND": "#4444ff",
    "IO_WAIT": "#44ff44"
}