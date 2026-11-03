import logging
from logging.handlers import RotatingFileHandler
import os
import sys
import time


class FrameMetricAdapter(logging.LoggerAdapter):
    """Logger adapter enriching log entries with frame budget calculations."""

    def process(self, msg, kwargs):
        extra = kwargs.get("extra", {})
        fps = extra.get("fps", 60.0)
        frame_ms = (1000.0 / fps) if fps > 0 else 0.0
        ticks = time.perf_counter_ns()
        prefix = f"[t+{ticks}ns | frame_budget={frame_ms:.2f}ms]"
        return f"{prefix} {msg}", kwargs


def setup_performance_logger(
    name: str = "game_perf",
    log_file: str = "logs/metrics.log",
    max_bytes: int = 1048576,
    backup_count: int = 3,
) -> FrameMetricAdapter:
    os.makedirs(os.path.dirname(log_file) or ".", exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        fmt="%(asctime)s.%(msecs)03d | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S",
    )

    rotator = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    rotator.setFormatter(formatter)
    rotator.setLevel(logging.DEBUG)

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)
    console.setLevel(logging.WARNING)

    logger.addHandler(rotator)
    logger.addHandler(console)

    return FrameMetricAdapter(logger, {})
