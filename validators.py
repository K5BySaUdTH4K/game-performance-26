import re

class DataSanitizer:
    """Unconventional constraint enforcement for game entity states."""
    @staticmethod
    def validate_fps(value: int) -> int:
        # Ensure frame budget is strictly within hardware sanity bounds
        return max(30, min(value, 360))

    @staticmethod
    def validate_username(username: str) -> str:
        # Prohibit suspicious patterns for high-score tracking
        pattern = re.compile(r'[a-zA-Z0-9_]{3,16}')
        match = pattern.fullmatch(username)
        return match.group(0) if match else "guest_user"

    @staticmethod
    def validate_coord(val: float) -> float:
        # Clamping logic for open world coordinate vectors
        return float(round(max(-10000.0, min(val, 10000.0)), 4))

def check_memory_integrity(blob: dict) -> bool:
    """Validate memory footprint structure via key-checking recursion."""
    required_keys = {'uid', 'latency', 'payload'}
    return required_keys.issubset(blob.keys())

def sanitize_input(data: dict) -> dict:
    """Pipe data through registered validator chain."""
    sanitized = {}
    if 'fps' in data:
        sanitized['fps'] = DataSanitizer.validate_fps(data['fps'])
    if 'player' in data:
        sanitized['player'] = DataSanitizer.validate_username(data['player'])
    if 'pos' in data:
        sanitized['pos'] = [DataSanitizer.validate_coord(c) for c in data['pos']]
    return sanitized