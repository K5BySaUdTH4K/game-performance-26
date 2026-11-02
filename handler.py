import functools
import logging
from typing import Callable, Any

logger = logging.getLogger('game-performance-26')

class PerformanceAnomaly(Exception):
    """Raised when game metrics drift into weird territory."""
    pass

def fault_tolerant_execution(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            logger.warning("divide by zero in engine metrics, resetting to baseline")
            return 0.0
        except (MemoryError, OverflowError) as e:
            logger.critical(f"resource exhaustion detected: {e}")
            # Attempt an emergency garbage collection via memory dump-like action
            import gc
            gc.collect()
            raise PerformanceAnomaly("frame budget exceeded") from e
        except Exception as e:
            logger.error(f"unexpected glitch in {func.__name__}: {type(e).__name__}")
            return None
    return wrapper

class ErrorHandler:
    def __init__(self, recovery_threshold: int = 3):
        self.recovery_threshold = recovery_threshold
        self.failure_count = 0

    def monitor_stream(self, func: Callable) -> Callable:
        @fault_tolerant_execution
        def guarded(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except PerformanceAnomaly:
                self.failure_count += 1
                if self.failure_count >= self.recovery_threshold:
                    return self._emergency_reboot()
                raise
        return guarded

    def _emergency_reboot(self):
        logger.fatal("system state inconsistent, forcing engine flush")
        self.failure_count = 0
        return "SYSTEM_RESET"