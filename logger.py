import logging
from logging.handlers import RotatingFileHandler
import sys

def get_performance_logger(name: str = 'game-perf-logger'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(process)d | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Console output for real-time debugging
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Rotation logic for disk preservation (5MB per file, 3 backups)
    file_handler = RotatingFileHandler(
        'perf_metrics.log', 
        maxBytes=5*1024*1024, 
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# Quick access factory instance
perf_logger = get_performance_logger()