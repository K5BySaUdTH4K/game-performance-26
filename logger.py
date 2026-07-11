import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file, max_bytes=5*1024*1024, backup_count=2):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setFormatter(formatter)    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    logger = setup_logger('game_logger', 'game.log')
    logger.info('Game started')
    for i in range(100):
        logger.debug(f'Game loop iteration {i}')
    logger.warning('Game ended')
