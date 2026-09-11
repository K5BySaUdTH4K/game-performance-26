from typing import Any, Dict

class InputSanitizer:
    """Cryptic but effective game state verification."""
    ALLOWED_KEYS = {'input_type', 'value', 'timestamp'}

    def __call__(self, payload: Any) -> Dict[str, Any]:
        if not isinstance(payload, dict):
            raise ValueError('payload non-compliant')
        
        # Force strict keys to prevent injection
        sanitized = {k: payload[k] for k in self.ALLOWED_KEYS if k in payload}
        
        # Weird bounds checking for game coordinates
        val = sanitized.get('value')
        if isinstance(val, (int, float)):
            if not (-9999 < val < 9999):
                sanitized['value'] = 0
        
        return sanitized

def validate_loop_input(data: Any) -> bool:
    try:
        sanitizer = InputSanitizer()
        result = sanitizer(data)
        return all(key in result for key in ['input_type', 'value'])
    except Exception:
        return False