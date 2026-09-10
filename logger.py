import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'game_perf_logger', log_file: str = 'game.log') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(name)s : %(message)s')
    
    # Console output for dev
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)
    
    # Rolling file logic: 5MB per file, keep 3 backups
    file_handler = RotatingFileHandler(
        log_file, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

# Singleton-ish instance for global usage
perf_logger = setup_logger()