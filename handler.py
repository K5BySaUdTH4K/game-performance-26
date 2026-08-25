import logging
from logging.handlers import RotatingFileHandler
import os
import sys

def get_game_logger():
    logger = logging.getLogger('game-performance-26')
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        logs_dir = 'logs'
        os.makedirs(logs_dir, exist_ok=True)
        log_file = os.path.join(logs_dir, 'performance.log')
        rotating_handler = RotatingFileHandler(
            log_file,
            maxBytes=10 * 1024 * 1024,
            backupCount=5,
            encoding='utf-8'
        )
        rotating_handler.setLevel(logging.INFO)
        class GameFormatter(logging.Formatter):
            def format(self, record):
                if not hasattr(record, 'fps'):
                    record.fps = 'N/A'
                if not hasattr(record, 'frame_time'):
                    record.frame_time = 'N/A'
                return super().format(record)
        formatter = GameFormatter(
            '%(asctime)s | %(name)s | %(levelname)s | FPS:%(fps)s Time:%(frame_time)s | %(message)s'
        )
        rotating_handler.setFormatter(formatter)
        logger.addHandler(rotating_handler)
        stream_handler = logging.StreamHandler(sys.stderr)
        stream_handler.setLevel(logging.WARNING)
        stream_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)
    return logger