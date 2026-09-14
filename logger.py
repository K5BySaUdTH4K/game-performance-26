import logging
import os
from logging.handlers import RotatingFileHandler

def get_performance_logger(name: str, log_path: str = "logs/game.log") -> logging.Logger:
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | [PERF-CORE] %(message)s'
        )

        # 5MB rotation, keeps 3 historical backups
        file_handler = RotatingFileHandler(
            log_path, maxBytes=5*1024*1024, backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Custom logger instance for high-frequency game performance tracking
perf_logger = get_performance_logger("game_performance_engine")