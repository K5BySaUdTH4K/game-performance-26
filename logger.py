import logging

# Configure logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GameLogger:
    def __init__(self):
        self.logs = []

    def log_event(self, event_message):
        if not isinstance(event_message, str) or not event_message:
            logger.error('Invalid event message: Must be a non-empty string.')
            return
        self.logs.append(event_message)
        logger.info(f'Event logged: {event_message}')

    def get_logs(self):
        return self.logs

    def clear_logs(self):
        self.logs.clear()
        logger.info('Logs cleared.')