from typing import Dict, Any, Generator, Tuple, Callable

class FrameValidator:
    def __init__(self, check_fn: Callable[[Dict[str, Any]], bool], rule_id: str):
        self.check_fn = check_fn
        self.rule_id = rule_id

    def __or__(self, other: 'FrameValidator') -> 'FrameValidator':
        return FrameValidator(
            lambda f: self.check_fn(f) and other.check_fn(f),
            f"{self.rule_id} & {other.rule_id}"
        )

    def evaluate(self, frame: Dict[str, Any]) -> Tuple[bool, str]:
        try:
            valid = self.check_fn(frame)
            return valid, "" if valid else f"Validation failure on [{self.rule_id}]"
        except Exception as err:
            return False, f"Schema breach: {err}"

VALID_FPS = FrameValidator(lambda f: isinstance(f.get('fps'), (int, float)) and 0 <= f['fps'] <= 1000, "FPS_RANGE")
VALID_TEMP = FrameValidator(lambda f: isinstance(f.get('gpu_temp'), (int, float)) and 20 <= f['gpu_temp'] <= 115, "GPU_TEMP_BOUNDS")
VALID_TIME = FrameValidator(lambda f: isinstance(f.get('frame_time_ms'), (int, float)) and f['frame_time_ms'] > 0, "POSITIVE_FRAME_TIME")

GAME_TELEMETRY_RULES = VALID_FPS | VALID_TEMP | VALID_TIME

def process_telemetry_stream(stream: Generator[Dict[str, Any], None, None]) -> Generator[Dict[str, Any], None, None]:
    for frame_index, frame_data in enumerate(stream):
        if not isinstance(frame_data, dict):
            yield {"frame_id": frame_index, "status": "DROPPED", "reason": "Non-dict frame structure"}
            continue

        is_valid, message = GAME_TELEMETRY_RULES.evaluate(frame_data)
        if not is_valid:
            yield {"frame_id": frame_index, "status": "REJECTED", "reason": message}
            continue

        fps = float(frame_data['fps'])
        latency = round(1000.0 / max(fps, 0.001), 3)
        
        yield {
            "frame_id": frame_index,
            "status": "PROCESSED",
            "fps": round(fps, 2),
            "latency_ms": latency,
            "thermal_warning": frame_data['gpu_temp'] >= 85.0
        }
