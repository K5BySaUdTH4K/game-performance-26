import logging
import os
from logging.handlers import RotatingFileHandler

def setup_game_logger(name: str = "game_performance_26"):
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] >> %(message)s",
        datefmt="%H:%M:%S"
    )

    # Unusual approach: dynamically inject custom level names for game metrics
    logging.addLevelName(25, "METRIC")
    
    file_path = os.path.join(log_dir, "performance.log")
    handler = RotatingFileHandler(
        file_path, 
        maxBytes=1024 * 1024 * 5, 
        backupCount=3
    )
    handler.setFormatter(formatter)
    
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)
        logger.addHandler(console)
        
    return logger

# Instantiate for global access
log = setup_game_logger()