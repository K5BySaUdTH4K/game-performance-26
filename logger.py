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
            if not isinstance(message, str):
                raise ValueError('Message must be a string')
            self.logger.info(message)
        except ValueError as ve:
            self.logger.error(f'Logging error: {ve}')

    def log_warning(self, message):
        try:
            if not isinstance(message, str):
                raise ValueError('Message must be a string')
            self.logger.warning(message)
        except ValueError as ve:
            self.logger.error(f'Logging error: {ve}')

    def log_error(self, message):
        try:
            if not isinstance(message, str):
                raise ValueError('Message must be a string')
            self.logger.error(message)
        except ValueError as ve:
            self.logger.error(f'Logging error: {ve}')

    def log_debug(self, message):
        try:
            if not isinstance(message, str):
                raise ValueError('Message must be a string')
            self.logger.debug(message)
        except ValueError as ve:
            self.logger.error(f'Logging error: {ve}')

# Example usage
if __name__ == '__main__':
    logger = CustomLogger('GameLogger')
    logger.log_info('Game started successfully!')
    logger.log_error(404)  # Intentional error for testing