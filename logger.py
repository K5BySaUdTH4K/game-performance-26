import logging
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, name, level=logging.INFO, max_bytes=10 * 1024 * 1024, backup_count=5):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.handler = RotatingFileHandler('game.log', maxBytes=max_bytes, backupCount=backup_count)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

logger = Logger('GameLogger')
logger.info('Logger initialized with rotation')