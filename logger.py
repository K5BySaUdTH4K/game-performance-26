import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game_performance.log', max_bytes=5*(1024**2), backup_count=3):
    logger = logging.getLogger('GamePerformanceLogger')
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Usage example
if __name__ == '__main__':
    logger = setup_logger()
    logger.debug('This is a debug message')
    logger.info('Logger setup complete')
    logger.warning('Warning message for performance issue')
    logger.error('An error occurred')
    logger.critical('Critical issue encountered')