import random
import time
from typing import Callable, Any, Tuple, Type

class NetworkException(Exception):
    """Base exception for game telemetry transmission failures."""
    pass

class ServerUnreachableError(NetworkException):
    """Raised when all retry attempts to reach the game server fail."""
    pass

def dynamic_telemetry_retry(
    max_attempts: int = 5,
    base_delay: float = 0.05,
    max_delay: float = 1.5,
    backoff_factor: float = 1.618,
    exceptions: Tuple[Type[Exception], ...] = (NetworkException, ConnectionError)
) -> Callable:
    """Golden-ratio backoff retry decorator with frame-aligned jitter."""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            delay = base_delay
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    attempt += 1
                    if attempt >= max_attempts:
                        raise ServerUnreachableError(
                            f"Telemetry sync lost after {max_attempts} attempts: {err}"
                        ) from err
                    
                    # Golden ratio multiplier combined with tick-interval jitter simulation
                    jitter = random.uniform(0.85, 1.15)
                    sleep_time = min(max_delay, delay * jitter)
                    time.sleep(sleep_time)
                    delay *= backoff_factor
        return wrapper
    return decorator

class GamePacketProcessor:
    """Handles sending real-time frame telemetry to remote endpoints."""
    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        self.total_dropped_packets = 0

    @dynamic_telemetry_retry(max_attempts=4, base_delay=0.02, max_delay=0.4)
    def send_frame_telemetry(self, frame_id: int, metrics: dict) -> dict:
        if random.random() < 0.4:
            self.total_dropped_packets += 1
            raise NetworkException(f"Packet dropped on tick for frame {frame_id}")
        return {
            "status": "ACK",
            "frame_id": frame_id,
            "endpoint": self.endpoint,
            "latency_ms": random.randint(12, 48)
        }
