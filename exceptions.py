class PerformanceThresholdError(Exception):
    """Raised when game frame budget is exceeded."""
    def __init__(self, frame_time, threshold):
        self.message = f"Frame time {frame_time:.4f}ms exceeds {threshold}ms limit"
        super().__init__(self.message)

class ResourcePoolExhaustion(Exception):
    """Raised when object pooling mechanism is depleted."""
    def __init__(self, resource_type):
        self.message = f"No available instances for {resource_type} in pool"
        super().__init__(self.message)

class CacheInvalidationFault(Exception):
    """Raised when cache state becomes inconsistent during hot-path."""
    def __init__(self, key):
        self.message = f"Atomic write failure for cache key: {key}"
        super().__init__(self.message)

class OptimizationFault(Exception):
    """Base exception for high-performance sub-system failures."""
    def __init__(self, code, context):
        self.code = code
        self.context = context
        super().__init__(f"Optimization fault [{code}]: {context}")

def raise_if_lagging(current_time, threshold):
    if current_time > threshold:
        raise PerformanceThresholdError(current_time, threshold)

def validate_resource_availability(count, limit, name):
    if count >= limit:
        raise ResourcePoolExhaustion(name)