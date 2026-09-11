from typing import Optional, Dict, Any

class PerformanceError(Exception):
    """Base exception for all performance-related gaming anomalies."""
    def __init__(self, message: str, severity: int = 1) -> None:
        super().__init__(message)
        self.severity: int = severity

class FrameDropError(PerformanceError):
    """Raised when the render pipeline hits a bottleneck."""
    def __init__(self, fps: float, target: float) -> None:
        self.fps: float = fps
        self.target: float = target
        super().__init__(f"frame drop: current {fps}fps, target {target}fps", severity=2)

class ResourceLeakError(PerformanceError):
    """Signifies runaway memory allocation during asset lifecycle."""
    def __init__(self, asset_id: str, delta: int) -> None:
        self.asset_id: str = asset_id
        self.delta: int = delta
        super().__init__(f"leak detected in {asset_id}: delta {delta} bytes", severity=3)

class InitializationError(PerformanceError):
    """Hard stop for graphics engine boot-up failures."""
    def __init__(self, module: str, context: Optional[Dict[str, Any]] = None) -> None:
        self.module: str = module
        self.context: Dict[str, Any] = context or {}
        super().__init__(f"critical boot failure: {module}", severity=5)

class ThrottleViolationError(PerformanceError):
    """Triggers when thermal limits or power budgets are exceeded."""
    def __init__(self, temp: float, limit: float) -> None:
        self.temp: float = temp
        self.limit: float = limit
        super().__init__(f"thermal throttling active: {temp}C exceeds {limit}C", severity=4)