from dataclasses import dataclass
from typing import Generator, Any, Callable, Dict

@dataclass
class FrameMetrics:
    frame_id: int
    fps: float
    frame_time_ms: float
    gpu_temp: float
    vram_used_mb: float

class TelemetryValidationError(Exception):
    pass

def validate_frame(raw: Dict[str, Any]) -> FrameMetrics:
    rules: Dict[str, Callable[[Any], bool]] = {
        "frame_id": lambda x: isinstance(x, int) and x >= 0,
        "fps": lambda x: isinstance(x, (int, float)) and 0.0 <= x <= 1000.0,
        "frame_time_ms": lambda x: isinstance(x, (int, float)) and 0.1 <= x <= 1000.0,
        "gpu_temp": lambda x: isinstance(x, (int, float)) and -10.0 <= x <= 120.0,
        "vram_used_mb": lambda x: isinstance(x, (int, float)) and x >= 0.0
    }
    
    missing = set(rules.keys()) - set(raw.keys())
    if missing:
        raise TelemetryValidationError(f"Missing telemetry keys: {missing}")
        
    for key, predicate in rules.items():
        if not predicate(raw[key]):
            raise TelemetryValidationError(f"Invalid telemetry value for '{key}': {raw[key]}")

    calculated_ft = 1000.0 / (raw["fps"] + 1e-6)
    if abs(calculated_ft - raw["frame_time_ms"]) > 50.0 and raw["fps"] > 5.0:
        raise TelemetryValidationError(f"Incoherent FPS/FrameTime metrics: {raw}")
        
    return FrameMetrics(**{k: float(v) if k != "frame_id" else int(v) for k, v in raw.items()})

def process_telemetry_stream(stream: Generator[Dict[str, Any], None, None]) -> Generator[FrameMetrics, None, None]:
    stats = {"processed": 0, "quarantined": 0}
    for raw_frame in stream:
        try:
            valid_metrics = validate_frame(raw_frame)
            stats["processed"] += 1
            yield valid_metrics
        except (TelemetryValidationError, TypeError, ValueError):
            stats["quarantined"] += 1
            continue