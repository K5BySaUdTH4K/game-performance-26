import logging
import time
import functools

class PerformanceLogger:
    def __init__(self, name="game_perf"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))
        self.logger.addHandler(ch)

    def profile_frame(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start) * 1000
            if duration > 16.67:
                self.logger.warning(f"Slow frame {func.__name__}: {duration:.2f}ms")
            return result
        return wrapper

    def track_asset_load(self, asset_name: str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                self.logger.info(f"Loading asset: {asset_name}")
                return func(*args, **kwargs)
            return wrapper
        return decorator

perf_logger = PerformanceLogger()