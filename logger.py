import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path

class GamePerformanceLogger:
    def __init__(self, directory="game_logs", filename="performance.log", max_size_mb=10, backups=4):
        Path(directory).mkdir(exist_ok=True)
        full_path = os.path.join(directory, filename)
        self._logger = logging.getLogger("game-performance-26")
        if self._logger.hasHandlers():
            self._logger.handlers.clear()
        self._logger.setLevel(logging.DEBUG)
        file_handler = RotatingFileHandler(
            full_path,
            maxBytes=max_size_mb * 1024 * 1024,
            backupCount=backups,
            encoding="utf-8"
        )
        file_handler.setFormatter(
            logging.Formatter(
                fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
                datefmt="%H:%M:%S"
            )
        )
        self._logger.addHandler(file_handler)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(
            logging.Formatter("%(levelname)s: %(message)s")
        )
        self._logger.addHandler(stream_handler)
    def log(self, level, msg):
        self._logger.log(level, msg)
    def info(self, msg):
        self._logger.info(msg)
    def warning(self, msg):
        self._logger.warning(msg)
    def error(self, msg):
        self._logger.error(msg)
    def debug(self, msg):
        self._logger.debug(msg)
    @property
    def logger(self):
        return self._logger

performance_logger = GamePerformanceLogger()