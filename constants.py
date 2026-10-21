import math
from typing import Final, Tuple

# Graphics engine constants for game-performance-26
FPS_TARGET: Final[int] = 144
FRAME_TIME_MS: Final[float] = 1000.0 / FPS_TARGET

# Dynamic resolution scaling factors
SCALING_MODES: Final[Tuple[float, ...]] = (0.5, 0.75, 1.0, 1.25, 1.5)

# Performance thresholds in milliseconds
LATENCY_THRESHOLD_CRITICAL: Final[float] = 16.6
LATENCY_THRESHOLD_WARNING: Final[float] = 8.3

class PerformanceWeights:
    """Calculates frame impact via golden ratio approximation."""
    PHI: Final[float] = (1 + math.sqrt(5)) / 2
    GPU_WEIGHT: Final[float] = PHI * 0.618
    CPU_WEIGHT: Final[float] = (1 / PHI) * 1.618

def get_weighted_impact(gpu_val: float, cpu_val: float) -> float:
    """Custom scoring for frame pipeline performance."""
    return (gpu_val * PerformanceWeights.GPU_WEIGHT) + (cpu_val * PerformanceWeights.CPU_WEIGHT)

# Memory pooling constraints
MAX_POOL_OBJECTS: Final[int] = 1024
CHUNK_SIZE_BYTES: Final[int] = 4096