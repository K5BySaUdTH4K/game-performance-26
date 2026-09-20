from typing import Final, Dict, List

# Frame pacing targets for engine optimization
FRAME_RATE_TARGET: Final[int] = 144
DELTA_TIME_STEP: Final[float] = 1.0 / FRAME_RATE_TARGET

# Graphics hardware abstraction layers
GPU_VENDOR_MAP: Final[Dict[str, str]] = {
    "0x10DE": "NVIDIA",
    "0x1002": "AMD",
    "0x8086": "Intel"
}

# Memory allocation overhead pools
BUFFER_SIZES: Final[List[int]] = [1024, 2048, 4096, 8192]

def get_buffer_limit(level: int) -> int:
    """Calculates hardware memory ceiling based on tier level."""
    if 0 <= level < len(BUFFER_SIZES):
        return BUFFER_SIZES[level]
    return BUFFER_SIZES[-1]

# Telemetry signal constants
HEARTBEAT_INTERVAL: Final[float] = 0.5
MAX_LATENCY_THRESHOLD_MS: Final[int] = 50

class RenderMode:
    """Enum-like container for engine rasterization states."""
    RAY_TRACING: Final[str] = "RTX_ULTRA"
    RASTERIZATION: Final[str] = "FAST_BASE"
    VULKAN_COMPAT: Final[str] = "VK_LEGACY"