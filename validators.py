from typing import Union, Callable, Any

def validate_frame_rate(fps: int) -> bool:
    """Ensures the frame rate stays within the bounds of a playable gaming experience."""
    return 30 <= fps <= 240

def validate_latency(ms: float) -> bool:
    """Checks if network latency allows for competitive play without excessive lag."""
    return 0 <= ms < 150.0

def enforce_schema(data: dict, schema: dict[str, type]) -> bool:
    """Dynamic validation of game state packets using a quick duck-typing lookup strategy."""
    for key, expected_type in schema.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False
    return True

def create_validator(condition: Callable[[Any], bool], error_msg: str) -> Callable[[Any], None]:
    """Higher-order factory for generating specialized game-state validation routines."""
    def validator(value: Any) -> None:
        if not condition(value):
            raise ValueError(f"Validation failure: {error_msg} (Value: {value})")
    return validator

frame_rate_validator = create_validator(validate_frame_rate, "FPS outside of operational bounds")
latency_validator = create_validator(validate_latency, "Network latency exceeds threshold for real-time sync")