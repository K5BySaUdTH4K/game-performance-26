import re
from typing import Any, Dict, List

class GameSchemaValidator:
    def __init__(self, schema: Dict[str, Any]):
        self.schema = schema

    def validate_performance_metrics(self, data: Dict[str, Any]) -> bool:
        for key, expected_type in self.schema.items():
            if key not in data or not isinstance(data[key], expected_type):
                return False
        return True

    @staticmethod
    def sanitize_input(value: str) -> str:
        return re.sub(r'[^a-zA-Z0-9_\-\s]', '', str(value)).strip()

def validate_frame_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    validator = GameSchemaValidator({'fps': int, 'latency': int, 'gpu_temp': float})
    return [item for item in data if validator.validate_performance_metrics(item)]

class ConfigValidationError(Exception):
    pass

def assert_config_integrity(config: Dict[str, Any], required: List[str]):
    missing = [key for key in required if key not in config]
    if missing:
        raise ConfigValidationError(f"Missing config keys: {', '.join(missing)}")
