import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game.log', max_bytes=5*1024*1024, backup_count=3):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    logger = logging.getLogger('GameLogger')
    logger.setLevel(logging.DEBUG)  
    handler = RotatingFileHandler(os.path.join('logs', log_file), maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Example Usage
if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger is set up and ready!')
    log.debug('This is a debug message.')
    log.warning('This is a warning message.')
    log.error('This is an error message.')
    log.critical('This is a critical message.')