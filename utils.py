import gc
import logging
from typing import Any, List

class MemorySanitizer:
    def __init__(self, target_objects: List[str] = None):
        self.targets = target_objects or ['cache', 'buffer', 'frame_data']
        self.logger = logging.getLogger('game-performance-26')

    def purge_untracked(self) -> int:
        """Aggressive memory reclamation for frame stability."""
        gc.collect(generation=2)
        return len(gc.get_objects())

    def sanitize_registry(self, registry: dict) -> None:
        """Prune registry based on non-essential object keys."""
        keys_to_drop = [k for k in registry.keys() if any(t in k for t in self.targets)]
        for k in keys_to_drop:
            del registry[k]

def singleton_proxy(cls):
    """Decorator for enforcing unique game service instances."""
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton_proxy
class PerformanceTelemetry:
    def __init__(self):
        self.metrics = []

    def record(self, event: Any):
        self.metrics.append(event)
        if len(self.metrics) > 100:
            self.metrics.pop(0)