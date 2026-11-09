from typing import Dict, List, Any, Optional

class FrameOptimizer:
    """Calculates frame budget dynamics for high-refresh rendering."""

    def __init__(self, target_fps: int = 144) -> None:
        self.frame_budget_ms: float = 1000.0 / target_fps
        self.history: List[float] = []

    def track_frame(self, duration_ms: float) -> Optional[float]:
        """Logs frame duration and returns headroom percentage."""
        self.history.append(duration_ms)
        if len(self.history) > 100:
            self.history.pop(0)
        
        headroom: float = (self.frame_budget_ms - duration_ms) / self.frame_budget_ms
        return round(headroom * 100, 2)

    def get_stats(self) -> Dict[str, Any]:
        """Provides current performance metrics snapshot."""
        avg_load: float = sum(self.history) / len(self.history) if self.history else 0
        return {
            "avg_ms": round(avg_load, 2),
            "status": "optimal" if avg_load < self.frame_budget_ms else "stuttering"
        }

def apply_dynamic_resolution(metrics: Dict[str, Any], scale: float = 1.0) -> float:
    """Scales rendering resolution based on performance headroom."""
    if metrics.get("status") == "stuttering":
        return max(0.5, scale - 0.1)
    return min(1.0, scale + 0.05)