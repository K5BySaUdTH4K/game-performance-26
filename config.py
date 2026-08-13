import logging
from logging.handlers import RotatingFileHandler
import os

LOG_FILE = 'game_performance.log'
LOG_LEVEL = logging.DEBUG

def setup_logger():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w'): pass

    logger = logging.getLogger('game_logger')
    logger.setLevel(LOG_LEVEL)
    handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=5)  # 5 MB each
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()