import logging
from logging.handlers import RotatingFileHandler
import os

def get_performance_logger(name='game_perf', path='perf.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | [%(name)s] %(message)s'
        )
        
        file_handler = RotatingFileHandler(
            path, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        
    return logger

perf_log = get_performance_logger()