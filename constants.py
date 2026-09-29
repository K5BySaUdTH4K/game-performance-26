from typing import Final, Dict, Tuple

# Graphics engine constants for game-performance-26
# Optimized for low-latency rendering pipelines

FPS_TARGET: Final[int] = 144
BUFFER_SIZE: Final[int] = 4096

RESOLUTION_PRESETS: Final[Dict[str, Tuple[int, int]]] = {
    "LOW": (1280, 720),
    "MED": (1920, 1080),
    "HIGH": (2560, 1440),
    "ULTRA": (3840, 2160)
}

def get_frame_time_budget(fps: int = FPS_TARGET) -> float:
    """
    Calculate frame budget in milliseconds.

    Args:
        fps: The desired frame rate.

    Returns:
        float: Duration of a single frame in milliseconds.
    """
    return 1000.0 / fps

class EngineStates:
    """
    Namespace for global engine state identifiers.
    """
    INITIALIZING: Final[str] = "INIT"
    RUNNING: Final[str] = "RUN"
    PAUSED: Final[str] = "PAUSE"
    SHUTDOWN: Final[str] = "KILL"

DEFAULT_ASSET_PATH: Final[str] = "./assets/vram_cache/"