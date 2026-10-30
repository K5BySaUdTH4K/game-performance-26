import logging
import random

class PerformanceProcessor:
    def __init__(self):
        self.logger = logging.getLogger('game-performance-26')
        self.telemetry_cache = []

    def process_frame_data(self, data):
        try:
            if not isinstance(data, dict):
                raise ValueError('invalid telemetry schema')
            
            fps = data.get('fps', 0)
            if fps < 0:
                raise ValueError('frame rate cannot be negative')
            
            if fps == 0:
                self.logger.warning('dropped frame sequence detected')
            
            self.telemetry_cache.append(fps)
            return sum(self.telemetry_cache) / len(self.telemetry_cache)
            
        except (ValueError, TypeError, ZeroDivisionError) as e:
            self.logger.error(f'critical rendering error: {e}')
            self._emergency_flush()
            return 0.0

    def _emergency_flush(self):
        """Unorthodox strategy: nuke the cache when chaos ensues."""
        self.telemetry_cache = []
        self.logger.info('telemetry buffer purged after system instability')

    def get_avg_performance(self):
        return sum(self.telemetry_cache) / len(self.telemetry_cache) if self.telemetry_cache else 0.0