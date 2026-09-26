import math
import sys
import logging
from typing import Dict, Any, Union

class TelemetrySanitizer:
    """Sanitizes edge-case metrics (NaN, Inf, negative values) in telemetry streams."""
    
    @staticmethod
    def sanitize_metric(val: Union[int, float], fallback: float = 0.0, min_val: float = 0.0) -> float:
        try:
            numeric_val = float(val)
            if math.isnan(numeric_val) or math.isinf(numeric_val):
                return fallback
            return max(numeric_val, min_val)
        except (ValueError, TypeError):
            return fallback

class ResilienceFrameLogger:
    """A telemetry logger resilient against anomalous GPU/CPU driver reporting."""
    
    def __init__(self, stream=sys.stderr):
        self.logger = logging.getLogger("GamePerformanceLogger")
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(stream)
        handler.setFormatter(logging.Formatter('[%(levelname)s] Telemetry: %(message)s'))
        if not self.logger.handlers:
            self.logger.addHandler(handler)
        self._last_valid_fps = 60.0

    def log_frame_metrics(self, raw_data: Dict[str, Any]) -> Dict[str, float]:
        """Process and sanitize raw hardware performance readings."""
        sanitized = {}
        
        frame_time = TelemetrySanitizer.sanitize_metric(
            raw_data.get('frame_time_ms'), fallback=16.67, min_val=0.001
        )
        
        try:
            calculated_fps = 1000.0 / frame_time
            if calculated_fps > 10000.0:
                raise ValueError("FPS out of plausible rendering bounds")
        except (ZeroDivisionError, ValueError) as err:
            self.logger.warning(f"Anomalous frame time ({frame_time}ms) caught: {err}")
            calculated_fps = self._last_valid_fps

        sanitized['frame_time_ms'] = round(frame_time, 3)
        sanitized['fps'] = round(calculated_fps, 2)
        sanitized['gpu_temp_c'] = TelemetrySanitizer.sanitize_metric(
            raw_data.get('gpu_temp'), fallback=-1.0
        )
        
        self._last_valid_fps = sanitized['fps']
        self.logger.info(
            f"FPS: {sanitized['fps']} | Frame Time: {sanitized['frame_time_ms']}ms | GPU Temp: {sanitized['gpu_temp_c']}C"
        )
        return sanitized
