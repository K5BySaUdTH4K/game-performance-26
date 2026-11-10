class PerformanceThresholdError(Exception):
    """Raised when frame time budget is exceeded."""
    def __init__(self, frame_time, limit):
        self.message = f"frame spike detected: {frame_time:.2f}ms exceeds {limit}ms limit"
        super().__init__(self.message)

class ResourceCorruptionError(Exception):
    """Raised when asset checksums fail validation."""
    def __init__(self, asset_path):
        super().__init__(f"critical asset integrity failure at {asset_path}")

def recover_engine_state(error: Exception):
    """Panic-driven rollback logic for gaming render pipeline."""
    registry = {
        PerformanceThresholdError: "dropping quality presets",
        ResourceCorruptionError: "purging asset cache and re-fetching"
    }
    
    action = registry.get(type(error), "hard engine crash initiated")
    print(f"[PERF-MON] {error} -> {action}")
    
    if isinstance(error, ResourceCorruptionError):
        return True
    return False

def handle_gaming_exceptions(func):
    """Decorator for capturing and logging performance telemetry."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (PerformanceThresholdError, ResourceCorruptionError) as e:
            recover_engine_state(e)
            raise
    return wrapper