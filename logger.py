import logging
from logging.handlers import RotatingFileHandler
import os

def get_game_logger(name='game_performance_26', log_file='game.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
            datefmt='%H:%M:%S'
        )

        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=1024 * 1024 * 5,
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

log = get_game_logger()