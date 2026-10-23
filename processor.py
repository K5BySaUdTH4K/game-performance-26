import math
from typing import Dict, Any, Generator

class InvalidFrameError(Exception):
    """Raised when telemetry input fails validation constraints."""
    pass

class GameTelemetryProcessor:
    def __init__(self) -> None:
        self.processed_frames: int = 0
        self.health_score: float = 100.0

    def _validate_frame_sample(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        required_keys = {"frame_id", "fps", "frame_time_ms", "gpu_temp_c\