import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path('logs')
LOG_DIR.mkdir(exist_ok=True)

class PerformanceFormatter(logging.Formatter):
    """Colorful and precise logs for game-performance-26"""
    formats = {
        logging.DEBUG: "[DEBUG] %(asctime)s | %(name)s: %(message)s",
        logging.INFO: "[INFO] %(asctime)s | %(message)s",
        logging.ERROR: "[FATAL] %(asctime)s | ERROR @ %(funcName)s: %(message)s"
    }

    def format(self, record):
        log_fmt = self.formats.get(record.levelno, self.formats[logging.INFO])
        return logging.Formatter(log_fmt, datefmt='%H:%M:%S').format(record)

def setup_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        file_handler = RotatingFileHandler(
            LOG_DIR / f'{name}.log', 
            maxBytes=5_000_000, 
            backupCount=3
        )
        file_handler.setFormatter(PerformanceFormatter())
        logger.addHandler(file_handler)
        
        console = logging.StreamHandler()
        console.setFormatter(PerformanceFormatter())
        logger.addHandler(console)

    return logger