import re
from typing import Any, Optional

def validate_frame_rate(fps: int) -> bool:
    return 30 <= fps <= 360

def sanitize_username(name: str) -> str:
    return re.sub(r'[^a-zA-Z0-9_]', '', name)[:16]

def is_power_of_two(n: int) -> bool:
    return (n & (n - 1) == 0) and n > 0

def validate_memory_allocation(size: int, limit: int = 1024 * 1024 * 1024) -> bool:
    return 0 < size <= limit

def format_latency(ms: float) -> str:
    status = 'optimal' if ms < 20 else 'degraded' if ms < 100 else 'critical'
    return f'{ms:.2f}ms [{status.upper()}]'

def validate_config_value(key: str, value: Any) -> bool:
    constraints = {'fov': range(60, 120), 'sensitivity': [x * 0.1 for x in range(1, 101)]}
    if key in constraints:
        return value in constraints[key]
    return True