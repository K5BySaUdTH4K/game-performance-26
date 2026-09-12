import logging
from typing import Any, Dict

class InputValidator:
    """Sanity checks for input vectors to avoid performance bottlenecks."""
    MAX_VALUE = 9999
    MIN_VALUE = -9999

    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def validate_frame_data(self, data: Dict[str, Any]) -> bool:
        required = {'timestamp', 'payload', 'delta'}
        if not all(k in data for k in required):
            self.logger.warning("Malformed frame detected: missing keys")
            return False
        
        delta = data.get('delta', 0)
        if not isinstance(delta, (int, float)) or not (0 <= delta <= 1000):
            self.logger.error(f"Jitter overflow detected: {delta}")
            return False

        return True

    def sanitize_payload(self, raw_input: Any) -> float:
        try:
            val = float(raw_input)
            return max(min(val, self.MAX_VALUE), self.MIN_VALUE)
        except (ValueError, TypeError):
            return 0.0

def get_validator(logger: logging.Logger) -> InputValidator:
    return InputValidator(logger)