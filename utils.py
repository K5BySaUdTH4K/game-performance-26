import functools
import time
import collections

def frame_rate_throttle(limit_hz=60):
    interval = 1.0 / limit_hz
    state = {'last_exec': 0.0}
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            elapsed = now - state['last_exec']
            if elapsed < interval:
                time.sleep(interval - elapsed)
            state['last_exec'] = time.perf_counter()
            return func(*args, **kwargs)
        return wrapper
    return decorator

class DataPool:
    def __init__(self, capacity=1024):
        self._pool = collections.deque(maxlen=capacity)
    def recycle(self, obj):
        self._pool.append(obj)
    def request(self, cls, *args, **kwargs):
        return self._pool.pop() if self._pool else cls(*args, **kwargs)

memoized_calculations = {}

def fast_lookup(func):
    @functools.wraps(func)
    def wrapper(*args):
        if args not in memoized_calculations:
            memoized_calculations[args] = func(*args)
        return memoized_calculations[args]
    return wrapper