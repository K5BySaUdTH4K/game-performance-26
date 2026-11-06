import functools
import time
import collections

def lru_cache_with_ttl(seconds: int, maxsize: int = 128):
    """Hybrid caching strategy using time-to-live expiration."""
    def decorator(func):
        cache = collections.OrderedDict()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            now = time.monotonic()
            
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < seconds:
                    return result
                del cache[key]
            
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result
        return wrapper
    return decorator

def batch_process_generator(data, size=64):
    """Memory-efficient generator for batching large game datasets."""
    it = iter(data)
    while True:
        batch = []
        for _ in range(size):
            try:
                batch.append(next(it))
            except StopIteration:
                if batch:
                    yield batch
                return
        yield batch

def fast_math_lerp(a, b, t):
    """Linear interpolation using optimized arithmetic inline."""
    return a + t * (b - a)