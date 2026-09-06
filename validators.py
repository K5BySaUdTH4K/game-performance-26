from typing import Any, Dict, Optional

class InputSanitizer:
    def __init__(self, schema: Dict[str, type]):
        self.schema = schema

    def __call__(self, payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        try:
            validated = {}
            for key, expected_type in self.schema.items():
                value = payload.get(key)
                if not isinstance(value, expected_type):
                    raise ValueError(f"Key {key} expects {expected_type.__name__}, got {type(value).__name__}")
                validated[key] = value
            return validated
        except (ValueError, AttributeError):
            return None

def validate_game_input(data: Dict[str, Any]) -> bool:
    """Strict validation for frame-critical packet processing."""
    required = {
        "player_id": int,
        "action_code": int,
        "timestamp": float,
        "payload": dict
    }
    
    if not isinstance(data, dict):
        return False
        
    for field, field_type in required.items():
        if field not in data or not isinstance(data[field], field_type):
            return False
            
    # Unusual check: packet freshness threshold
    if data['timestamp'] < 0:
        return False
        
    return True

def sanitize_stream(stream_data: Any) -> Dict[str, Any]:
    # Coerce to dictionary or return empty to prevent crash
    return stream_data if isinstance(stream_data, dict) else {}