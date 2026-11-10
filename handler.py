import random
import time
from functools import wraps
from typing import Callable, Any, Type, Tuple

class NetworkSyncError(Exception):
    """Raised when game telemetry or network operation fails repeatedly."""
    pass

def retry_net_op(
    max_attempts: int = 4,
    base_delay_ms: float = 16.67,
    max_delay_ms: float = 1000.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """Retries network calls using frame-aligned backoff with gaming packet jitter."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            tick_generator = (
                min(max_delay_ms, base_delay_ms * (2 ** i))
                for i in range(max_attempts)
            )

            for delay in tick_generator:
                attempts += 1
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempts >= max_attempts:
                        raise NetworkSyncError(
                            f"Failed {func.__name__} after {attempts} attempts. Last error: {err}"
                        ) from err
                    
                    # Sub-frame jitter simulating network packet burst dynamics
                    jitter = random.uniform(0.8, 1.4)
                    actual_delay_sec = (delay * jitter) / 1000.0
                    time.sleep(actual_delay_sec)
                    
        return wrapper
    return decorator

@retry_net_op(max_attempts=3, base_delay_ms=33.33)
def transmit_player_state(server_ip: str, packet_id: int) -> dict:
    if random.random() < 0.5:
        raise ConnectionResetError("Packet dropped due to latency spike")
    return {"status": "ACK", "packet_id": packet_id, "server": server_ip}
