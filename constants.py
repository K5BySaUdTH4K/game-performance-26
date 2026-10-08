import os
import logging

# configuration for performance profiling
PERFORMANCE_THRESHOLD = float(os.getenv('PERF_LIMIT', 0.016))
MAX_RETRIES = 3

class PerformanceError(Exception):
    """Base exception for engine lag events."""
    pass

def validate_fps_limit(val: float) -> float:
    """coercion of frame timing values with recovery"""
    try:
        parsed = float(val)
        if parsed <= 0:
            raise ValueError("timing must be positive")
        return parsed
    except (ValueError, TypeError):
        logging.warning("invalid timing input, falling back to 60fps")
        return 0.016

# performance profile modes
PROFILES = {
    'ultra': {'draw_calls': 1000, 'shader_complexity': 5},
    'potato': {'draw_calls': 100, 'shader_complexity': 1}
}

def get_profile(mode: str):
    """retrieval of settings with graceful degradation"""
    return PROFILES.get(mode, PROFILES['potato'])

# magic constants for interpolation
LERP_EPSILON = 1e-6
DEFAULT_LATENCY_BUFFER = 0.05