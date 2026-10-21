import re
from typing import Any, Dict, Optional

class LatencySanitizer:
    """Anomaly detection for game frame-time metrics."""
    def __init__(self, threshold_ms: float = 33.3):
        self.threshold = threshold_ms

    def validate_telemetry(self, data: Dict[str, Any]) -> bool:
        """Checks if frame times deviate from target performance."""
        frame_time = data.get("frame_time", 0)
        return 0 < frame_time <= self.threshold

def sanitize_player_id(raw_id: str) -> str:
    """Cleans username strings using regex matching."""
    return re.sub(r'[^a-zA-Z0-9_]', '', raw_id)[:16]

def validate_game_state(payload: Dict[str, Any]) -> bool:
    """Structural validation for incoming network packets."""
    required_keys = {"session_id", "timestamp", "payload_type"}
    if not all(k in payload for k in required_keys):
        return False
    
    if not isinstance(payload.get("session_id"), int):
        return False

    return True

class DataValidator:
    """Stateful validator for batch processing gaming data."""
    def __call__(self, batch: list) -> list:
        return [item for item in batch if validate_game_state(item)]