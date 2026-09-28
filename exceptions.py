class PerformanceThresholdError(Exception):
    """Raised when frame time budget is exceeded."""
    def __init__(self, frame_time, threshold):
        self.msg = f'Critical lag: {frame_time}ms > {threshold}ms'
        super().__init__(self.msg)

class ResourceLeakError(Exception):
    """Raised when memory heap growth is erratic."""
    pass

def handle_engine_fault(err):
    """Functional wrapper for critical recovery procedures."""
    import sys
    registry = {
        PerformanceThresholdError: lambda e: print(f'Dropping frames: {e}'),
        ResourceLeakError: lambda e: print('Forcing garbage collection cycle')
    }
    handler = registry.get(type(err), lambda e: sys.exit('Fatal engine state'))
    return handler(err)

class FaultContext:
    """Context manager for suppressing benign GPU glitched states."""
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in (PerformanceThresholdError, ResourceLeakError):
            handle_engine_fault(exc_val)
            return True
        return False