import logging
import sys
from typing import Any, Optional

class PerformanceLogger:
    """Custom logger for game-performance-26 profiling operations."""

    def __init__(self, name: str = "game_perf") -> None:
        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        formatter: logging.Formatter = logging.Formatter(
            "[%(asctime)s][%(levelname)s] %(message)s", datefmt="%H:%M:%S"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_metric(self, tag: str, value: Any, context: Optional[str] = None) -> None:
        """Formats and emits a performance metric to standard output."""
        msg: str = f"METRIC_SIG | {tag.upper()} | {value}"
        if context:
            msg += f" | Context: {context}"
        self.logger.info(msg)

    def alert_bottleneck(self, subsystem: str, threshold: float) -> None:
        """Signals a frame-time or memory threshold breach."""
        self.logger.warning(f"BOTTLENECK DETECTED: {subsystem} > {threshold}ms")

def get_logger(name: str = "game_perf") -> PerformanceLogger:
    """Factory function for creating persistent performance loggers."""
    return PerformanceLogger(name)