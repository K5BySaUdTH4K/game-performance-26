import logging

class GameLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log(self, level, message):
        log_func = {
            'debug': self.logger.debug,
            'info': self.logger.info,
            'warning': self.logger.warning,
            'error': self.logger.error,
            'critical': self.logger.critical,
        }
        log_func.get(level, self.logger.info)(message)

if __name__ == '__main__':
    logger = GameLogger('GamePerformanceLogger')
    logger.log('info', 'Game started')
    logger.log('warning', 'Low memory warning')
    logger.log('error', 'Game crashed!')
    logger.log('debug', 'Debugging information')
    logger.log('critical', 'Critical error encountered')