import collections
from typing import Generator, Callable, Any, Dict

def coroutine(func: Callable[..., Generator[None, Any, None]]) -> Callable[..., Generator[None, Any, None]]:
    def start(*args: Any, **kwargs: Any) -> Generator[None, Any, None]:
        g = func(*args, **kwargs)
        next(g)
        return g
    return start

@coroutine
def anomaly_detector(threshold_factor: float, sink: Generator[None, Dict[str, Any], None]) -> Generator[None, float, None]:
    history = collections.deque(maxlen=60)
    while True:
        duration = yield
        if not history:
            history.append(duration)
            sink.send({"duration": duration, "is_anomaly": False, "baseline": duration})
            continue
        baseline = sum(history) / len(history)
        is_anomaly = duration > (baseline * threshold_factor)
        if not is_anomaly:
            history.append(duration)
        sink.send({"duration": duration, "is_anomaly": is_anomaly, "baseline": baseline})

@coroutine
def metric_aggregator() -> Generator[None, Dict[str, Any], None]:
    while True:
        data = yield
        if data["is_anomaly"]:
            print(f"[anomaly] Frame took {data['duration']:.2f}ms (baseline: {data['baseline']:.2f}ms)")