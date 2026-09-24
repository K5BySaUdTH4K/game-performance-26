import logging
from logging.handlers import RotatingFileHandler
import os

def get_performance_logger(name='game-perf'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    log_path = os.path.join('logs', 'perf_metrics.log')
    os.makedirs('logs', exist_ok=True)
    
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | [%(name)s] | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    file_handler = RotatingFileHandler(
        log_path,
        maxBytes=1024 * 1024 * 5,
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger

perf_logger = get_performance_logger()