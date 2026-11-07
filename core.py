from typing import Dict, List, Optional, Union
import time

class FrameOptimizer:
    """Calculates dynamic frame scaling for game-performance-26 engine."""

    def __init__(self, target_fps: int = 60) -> None:
        self.target_fps: int = target_fps
        self.history: List[float] = []

    def compute_scaling_factor(self, current_frame_time: float) -> float:
        """Determines resolution scale multiplier based on frame drift."""
        self.history.append(current_frame_time)
        if len(self.history) > 10:
            self.history.pop(0)
        
        avg_time: float = sum(self.history) / len(self.history)
        ideal_time: float = 1.0 / self.target_fps
        
        if avg_time <= ideal_time:
            return 1.0
        
        # Exponential decay scaling for aggressive performance recovery
        return max(0.5, 1.0 - (avg_time - ideal_time) * 5.0)

    def get_stats(self) -> Dict[str, Union[float, int]]:
        """Returns telemetry data for system logging."""
        return {
            "target": self.target_fps,
            "latency_ms": (sum(self.history) / len(self.history)) * 1000 if self.history else 0
        }

def patch_frame_logic(instance: FrameOptimizer, frame_delta: float) -> float:
    """Orchestrator for runtime performance adjustment."""
    return instance.compute_scaling_factor(frame_delta)