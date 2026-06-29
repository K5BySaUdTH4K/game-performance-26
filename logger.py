import logging

class GameLogger:
    def __init__(self, name='GameLogger'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler('game_log.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_debug(self, message):
        self.logger.debug(message)

# Example usage:
# game_logger = GameLogger()
# game_logger.log_info('Game started successfully!')
# game_logger.log_warning('Low health warning!')
# game_logger.log_error('Game crashed unexpectedly!')
# game_logger.log_debug('Player position updated to (10, 20)')
