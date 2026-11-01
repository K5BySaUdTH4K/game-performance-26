import time
from pathlib import Path
from logging import Logger, getLogger, Formatter, INFO
from logging.handlers import RotatingFileHandler

class FrameAwareFormatter(Formatter):
    """Custom log formatter tracking estimated frame numbers since engine boot."""
    def __init__(self, target_fps: int = 60):
        super().__init__("[%(asctime)s.%(msecs)03d][%(levelname)s][FRAME:%(frame)d] %(message)s", datefmt="%H:%M:%S")
        self.start_time = time.perf_counter()
        self.target_fps = target_fps

    def format(self, record):
        if not hasattr(record, "frame"):
            elapsed = time.perf_counter() - self.start_time
            record.frame = int(elapsed * self.target_fps)
        return super().format(record)

class TelemetryRotator(RotatingFileHandler):
    """Rotating file handler that inserts frame marker header on rotation."""
    def doRollover(self):
        super().doRollover()
        if self.stream:
            self.stream.write("--- TELEMETRY ROTATION SNAPSHOT MARKER ---\n")
            self.stream.flush()

def setup_game_logger(
    name: str = "perf_metrics",
    dir_path: str = "logs",
    max_mb: int = 2,
    backups: int = 5
) -> Logger:
    log_dir = Path(dir_path)
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"{name}.log"

    logger = getLogger(name)
    logger.setLevel(INFO)

    if not logger.handlers:
        max_bytes = max_mb * 1024 * 1024
        handler = TelemetryRotator(
            log_path,
            maxBytes=max_bytes,
            backupCount=backups,
            encoding="utf-8"
        )
        handler.setFormatter(FrameAwareFormatter(target_fps=60))
        logger.addHandler(handler)

    return logger

if __name__ == "__main__":
    game_log = setup_game_logger()
    game_log.info("Renderer initialized")
    game_log.warning("Stutter detected in shadow map generation", extra={"frame": 144})
