import logging
import logging.handlers

class Logger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.setup_handler()

    def setup_handler(self):
        log_handler = logging.handlers.RotatingFileHandler(
            'game.log', maxBytes=5*1024*1024, backupCount=5
        )
        log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_handler.setFormatter(log_formatter)
        self.logger.addHandler(log_handler)

    def debug(self, msg: str):
        self.logger.debug(msg)

    def info(self, msg: str):
        self.logger.info(msg)

    def warning(self, msg: str):
        self.logger.warning(msg)

    def error(self, msg: str):
        self.logger.error(msg)

    def critical(self, msg: str):
        self.logger.critical(msg)

if __name__ == '__main__':
    logger = Logger('GameLogger')
    logger.info('Logger is set up and ready.')