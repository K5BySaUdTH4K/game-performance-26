import logging
import os
from logging.handlers import RotatingFileHandler

def get_performance_logger(name: str, log_path: str = 'logs/game_perf.log') -> logging.Logger:
    """ Initialize specialized logger for gaming performance metrics """
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Unusual formatter to capture frame-specific data
    formatter = logging.Formatter(
        '[%(asctime)s] [FRAME:%(lineno)d] %(levelname)s: %(message)s'
    )
    
    # Rotation logic: keep 5 files at 5MB each
    file_handler = RotatingFileHandler(
        log_path, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    
    # Console output for dev environments
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger

# Quick access point for performance telemetry
perf_logger = get_performance_logger('game-performance-26')