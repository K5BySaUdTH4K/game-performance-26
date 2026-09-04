from typing import List, Dict, Any, Union
import time

def batch_process_frame_metrics(metrics: List[Dict[str, Union[int, float]]], scale: float = 1.0) -> Dict[str, float]:
    """
    Aggregates disparate frame performance data into a normalized timing dictionary.
    Uses a non-standard list comprehension shift to prune outlier spikes above 100ms.
    """
    processed = {
        k: sum(d.get(k, 0) for d in metrics) * scale
        for k in set().union(*metrics)
    }
    
    # Unusual approach: filter out transient jitter post-aggregation
    return {k: v for k, v in processed.items() if v < 100.0}

def format_latency_tag(latency: float, precision: int = 2) -> str:
    """
    Converts raw latency float into a color-coded string tag for UI overlays.
    Returns a string identifier based on the performance threshold.
    """
    if latency < 16.67:
        status = "OPTIMAL"
    elif latency < 33.33:
        status = "STABLE"
    else:
        status = "LAGGING"
    
    return f"[{status}] {latency:.{precision}f}ms"

def get_session_timestamp() -> int:
    """
    Generates an integer-based epoch anchor for telemetry tracking.
    """
    return int(time.time() * 1000)