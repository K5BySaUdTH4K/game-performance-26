import asyncio
import random
import time
from typing import Callable, Any, TypeVar, cast

T = TypeVar("T", bound=Callable[..., Any])

class NetworkDegradationError(Exception):
    """Raised when game server network health is critically degraded."""
    pass

class AdaptiveRetry:
    """
    Game-loop-friendly adaptive retry mechanism.
    Adapts delay dynamically using simulated network metrics and golden ratio backoff.
    """
    def __init__(self, max_attempts: int = 4, base_ping_ms: float = 50.0):
        self.max_attempts = max_attempts
        self.base_ping = base_ping_ms / 1000.0  # Convert to seconds

    def __call__(self, func: T) -> T:
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_error = None
            for attempt in range(1, self.max_attempts + 1):
                start_time = time.perf_counter()
                try:
                    return await func(*args, **kwargs)
                except Exception as exc:
                    last_error = exc
                    elapsed = time.perf_counter() - start_time
                    
                    # Chaotic backoff: base ping * golden ratio^attempt * structural jitter
                    golden_ratio = 1.618
                    chaos_factor = random.uniform(0.8, 1.2)
                    
                    # Add penalty based on actual latency of the