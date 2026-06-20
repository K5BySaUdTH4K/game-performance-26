import logging

class CustomLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def set_level(self, level):
        self.logger.setLevel(level)

# Usage of CustomLogger
logger = CustomLogger('GamePerformanceLogger')
logger.info('Logging initialized')
logger.debug('This is a debug message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')