import logging

class GameLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(f'{name}.log')
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log(self, message, level='info'):
        level = level.lower()
        if level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        else:
            self.logger.info(message)

# Example usage
if __name__ == '__main__':
    game_logger = GameLogger('game_log')
    game_logger.log('Game started', 'info')
    game_logger.log('A minor issue occurred', 'warning')
    game_logger.log('An error occurred in processing', 'error')
    game_logger.log('Debugging the issue', 'debug')