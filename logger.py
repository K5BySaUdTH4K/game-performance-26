import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=5 * 1024 * 1024, backup_count=5, level=logging.INFO):
    logger = logging.getLogger('game_logger')
    logger.setLevel(level)
    if not logger.handlers:
        handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

# Example of usage
if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger has been set up successfully.')
    log.warning('This is a warning message.')