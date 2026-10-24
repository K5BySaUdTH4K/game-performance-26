import sys
from typing import Dict, Any, Generator, Callable, List

TelemetryFrame = Dict[str, Any]

class TelemetryValidationSchema:
    def __init__(self) -> None:
        self._rules: List[tuple[str, Callable[[Any], bool], str]] = []

    def field(self, name: str, predicate: Callable[[Any], bool], err_msg: str) -> "TelemetryValidationSchema":
        self._rules.append((name, predicate, err_msg))
        return self

    def validate(self, frame: TelemetryFrame) -> List[str]:
        errors = []
        for key, check, msg in self._rules:
            if key not in frame:
                errors.append(f"Missing field: '{key}'")
            elif not check(frame[key]):
                errors.append(f"Invalid '{key}' ({frame[key]}): {msg}")
        return errors

def create_game_frame_schema() -> TelemetryValidationSchema:
    return (
        TelemetryValidationSchema()
        .field("frame_id", lambda x: isinstance(x, int) and x >= 0, "must be non-negative int")
        .field("fps", lambda x: isinstance(x, (int, float)) and 0.0 <= x <= 1000.0, "must be between 0 and 1000 FPS")
        .field("frametime_ms", lambda x: isinstance(x, (int, float)) and x > 0, "must be positive float")
        .field("gpu_temp_c", lambda x: isinstance(x, (int, float)) and 20.0 <= x <= 115.0, "out of safe operating range")
    )

def frame_processing_stream(raw_stream: List[TelemetryFrame]) -> Generator[TelemetryFrame, None, None]:
    schema = create_game_frame_schema()
    
    for raw_frame in raw_stream:
        violations = schema.validate(raw_frame)
        if violations:
            print(f"[REJECTED FRAME] Violations detected: {'; '.join(violations)}", file=sys.stderr)
            continue
        
        processed_frame = dict(raw_frame)
        processed_frame["frame_budget_exceeded"] = processed_frame["frametime_ms"] > (1000.0 / 60.0)
        yield processed_frame

def process_telemetry_batch(batch: List[TelemetryFrame]) -> List[TelemetryFrame]:
    valid_frames = []
    for frame in frame_processing_stream(batch):
        valid_frames.append(frame)
    return valid_frames

if __name__ == "__main__":
    sample_data = [
        {"frame_id": 101, "fps": 144.2, "frametime_ms": 6.9, "gpu_temp_c": 68.5},
        {"frame_id": 102, "fps": -5.0, "frametime_ms": 16.6, "gpu_temp_c": 72.0},
        {"frame_id": 103, "fps": 59.1, "frametime_ms": 16.9, "gpu_temp_c": 120.0},
        {"frame_id": 104, "fps": 60.0, "frametime_ms": 16.67, "gpu_temp_c": 70.1},
    ]
    results = process_telemetry_batch(sample_data)
    print(f"Processed {len(results)} valid performance frames.")