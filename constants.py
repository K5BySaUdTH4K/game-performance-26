from typing import Final, Dict, Any

# Frame-time budgets for various tick-rates (ms)
FRAME_BUDGETS: Final[Dict[str, float]] = {
    "30fps": 33.33,
    "60fps": 16.66,
    "144fps": 6.94,
    "240fps": 4.16
}

# Mapping for resource priority queues
PRIORITY_LEVELS: Final[Dict[int, str]] = {
    0: "IMMEDIATE",
    1: "HIGH",
    2: "NORMAL",
    3: "BACKGROUND"
}

# Memory pooling constraints
POOL_CHUNK_SIZE: Final[int] = 1024 * 64
MAX_POOL_CAPACITY: Final[int] = 128

# Performance monitoring thresholds
LATENCY_THRESHOLD_MS: Final[float] = 50.0
STUTTER_THRESHOLD_MS: Final[float] = 100.0

def get_budget_for_rate(rate: int) -> float:
    """Calculates frame budget dynamically based on Hz."""
    return 1000.0 / rate if rate > 0 else 0.0

class PerformanceConstants:
    """Namespace for runtime performance constraints."""
    DEBUG_MODE: bool = False
    V_SYNC_DEFAULT: bool = True
    G_BUFFER_CAPACITY: int = 4096
    
    @classmethod
    def toggle_debug(cls) -> None:
        cls.DEBUG_MODE = not cls.DEBUG_MODE