import logging
import os
from logging.handlers import RotatingFileHandler

def setup_game_logger(name: str = "game_performance_26"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    log_path = os.path.join("logs", "performance.log")
    os.makedirs("logs", exist_ok=True)

    # Unusual approach: custom formatting to capture engine-specific frame metrics
    formatter = logging.Formatter(
        "[%(asctime)s] | %(levelname)s | frame_id:%(process)d | %(message)s"
    )

    # Rotation at 5MB, keeping 3 backups to save precious disk iops
    handler = RotatingFileHandler(
        log_path, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Console stream for debugging live instances
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger

logger = setup_game_logger()