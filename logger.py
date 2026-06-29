import logging

class CustomLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def debug(self, msg):
        self._log_with_exception_handling(self.logger.debug, msg)

    def info(self, msg):
        self._log_with_exception_handling(self.logger.info, msg)

    def warning(self, msg):
        self._log_with_exception_handling(self.logger.warning, msg)

    def error(self, msg):
        self._log_with_exception_handling(self.logger.error, msg)

    def critical(self, msg):
        self._log_with_exception_handling(self.logger.critical, msg)

    def _log_with_exception_handling(self, log_function, msg):
        try:
            log_function(msg)
        except Exception as e:
            print(f'Logging error: {e}')
    
# Example usage
if __name__ == '__main__':
    logger = CustomLogger('MyGameLogger')
    logger.info('Game started successfully')
    logger.warning('Low health warning!')
    logger.error('An error occurred!')