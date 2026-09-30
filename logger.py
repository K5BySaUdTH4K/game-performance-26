import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

class PerformanceLogger:
    def __init__(self, log_file: str = 'game_perf.log'):
        self.path = Path(log_file)
        self.logger = logging.getLogger('game_performance_26')
        self.logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter(
            '%(asctime)s | [%(levelname)s] | %(message)s',
            datefmt='%H:%M:%S'
        )
        
        handler = RotatingFileHandler(
            self.path, 
            maxBytes=1024 * 1024 * 5, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
        # Add a console stream for dev visibility
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        self.logger.addHandler(console)

    def get(self):
        return self.logger

def setup_logger(name: str = 'perf_log'):
    return PerformanceLogger(f'{name}.log').get()