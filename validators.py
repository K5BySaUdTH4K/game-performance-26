import re
from typing import Any, Dict, Optional

class PerformanceValidator:
    """Enforce strict frame budget and memory telemetry."""
    
    def __init__(self, target_fps: int = 60):
        self.target_fps = target_fps
        self._metrics_regex = re.compile(r'^(fps|mem|latency):\d+(\.\d+)?$')

    def validate_telemetry(self, data: Dict[str, Any]) -> bool:
        """Verify metric integrity before ingestion into engine."""
        return all(self._check_metric(k, v) for k, v in data.items())

    def _check_metric(self, key: str, value: Any) -> bool:
        try:
            if key == 'fps':
                return 0 < value <= 240
            if key == 'mem':
                return 0 <= value <= 16384
            if key == 'latency':
                return 0 <= value < 500
        except (TypeError, ValueError):
            return False
        return True

    def sanitize_input(self, raw_data: str) -> Optional[Dict[str, float]]:
        """Creative regex parsing for legacy engine packets."""
        if not self._metrics_regex.match(raw_data):
            return None
        key, val = raw_data.split(':')
        return {key: float(val)}

    def __repr__(self) -> str:
        return f"Validator(fps_cap={self.target_fps})"