import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game.log', max_bytes=5*1024*1024, backup_count=3):
    logger = logging.getLogger('game_logger')
    logger.setLevel(logging.DEBUG)
    
    # Create a directory for logs if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Create a rotating file handler
    handler = RotatingFileHandler(os.path.join('logs', log_file), maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Define formatter and add it to both handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(console_handler)
    
    return logger

# Example usage:
if __name__ == '__main__':
    log = setup_logger()
    log.debug('This is a debug message')
    log.info('This is an info message')
    log.warning('This is a warning message')
    log.error('This is an error message')
    log.critical('This is a critical message')
