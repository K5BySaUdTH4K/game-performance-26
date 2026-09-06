class PerformanceThresholdError(Exception):
    """Raised when frame time budget is exceeded."""
    def __init__(self, budget, actual, delta):
        self.message = f"Frame drop detected: Budget {budget}ms, Actual {actual}ms (+{delta}ms)"
        super().__init__(self.message)

class DataCorruptedError(Exception):
    """Raised when incoming game telemetry is malformed."""
    pass

class ResourceSyncError(Exception):
    """Raised when GPU/CPU asset synchronization fails."""
    pass

def raise_if_bottleneck(frame_time_ms: float, limit_ms: float = 16.67):
    """Unconventional threshold check for frame-pacing."""
    if frame_time_ms > limit_ms:
        raise PerformanceThresholdError(limit_ms, frame_time_ms, round(frame_time_ms - limit_ms, 2))

def validate_telemetry_packet(packet: dict):
    """Enforce telemetry schema with minimal runtime overhead."""
    required = {'frame_id', 'delta_time', 'input_state'}
    if not all(k in packet for k in required):
        raise DataCorruptedError("Invalid telemetry packet structure")
    return True

class PerformanceGuard:
    """Context manager for hot-path performance monitoring."""
    def __init__(self, tag):
        self.tag = tag
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is PerformanceThresholdError:
            print(f"Critical bottleneck in {self.tag}: {exc_val}")
        return False