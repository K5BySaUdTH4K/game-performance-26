import logging
import time
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional


class GameTelemetryFormatter(logging.Formatter):
    """Custom log formatter injecting high-resolution game timestamps and FPS metrics."""

    def __init__(self, fmt: Optional[str] = None):
        super().__init__(
            fmt or "[%(asctime)s.%(msecs)03d][%(levelname)s][FPS:%(fps).1f] %(message)s",
            datefmt="%H:%M:%S",
        )
        self.start_time = time.perf_counter()

    def format(self, record: logging.LogRecord) -> str:
        if not hasattr(record, "fps"):
            record.fps = getattr(record, "custom_fps", 60.0)
        record.game_uptime = f"{time.perf_counter() - self.start_time:.2f}s"
        return super().format(record)


def setup_game_logger(
    name: str = "telemetry",
    log_dir: str = "logs",
    max_bytes: int = 2 * 1024 * 1024,
    backup_count: int = 5,
    min_level: int = logging.INFO,
) -> logging.Logger:
    """Configures a rotating logger tuned for high-frequency game performance telemetry."""
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(f"game.perf.{name}")
    logger.setLevel(min_level)
    logger.propagate = False

    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = RotatingFileHandler(
        filename=log_path / f"{name}_perf.log",
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(GameTelemetryFormatter())
    file_handler.setLevel(min_level)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("%(levelname)s - [%(name)s] - %(message)s")
    )
    console_handler.setLevel(logging.WARNING)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info(f"Initialized rotating telemetry log file at {file_handler.baseFilename}")
    return logger


def log_frame_spike(logger: logging.Logger, frame_time_ms: float, target_fps: float = 60.0) -> None:
    """Helper to log frame latency spikes directly with custom frame rate calculation."""
    current_fps = 1000.0 / frame_time_ms if frame_time_ms > 0 else 0.0
    budget_ms = 1000.0 / target_fps
    if frame_time_ms > budget_ms * 1.5:
        logger.warning(
            f"Frame time spike detected: {frame_time_ms:.2f}ms (Budget: {budget_ms:.2f}ms)",
            extra={"custom_fps": current_fps},
        )
    else:
        logger.debug(
            f"Frame latency frame: {frame_time_ms:.2f}ms",
            extra={"custom_fps": current_fps},
        )
