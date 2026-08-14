import logging

class CustomLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_info(self, message):
        try:
            self.logger.info(message)
        except Exception as e:
            self.logger.error(f'Error logging info: {e}')  

    def log_warning(self, message):
        try:
            self.logger.warning(message)
        except Exception as e:
            self.logger.error(f'Error logging warning: {e}')

    def log_error(self, message):
        try:
            self.logger.error(message)
        except Exception as e:
            self.logger.error(f'Error logging error: {e}')

# Usage Example
if __name__ == '__main__':
    logger = CustomLogger('GameLogger')
    logger.log_info('Game started')
    logger.log_warning('Low health warning')
    logger.log_error('Game crashed unexpectedly')