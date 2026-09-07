import typing

class ValidationError(ValueError):
    pass

class MetricValidator:
    def __init__(self):
        self.rules = {}

    def rule(self, metric: str):
        def decorator(func):
            self.rules[metric] = func
            return func
        return decorator

    def validate(self, data: dict[str, typing.Any]) -> bool:
        for metric, value in data.items():
            if metric in self.rules:
                if not self.rules[metric](value):
                    raise ValidationError(f"Metric {metric} failed validation with value: {value}")
        return True

validator = MetricValidator()

@validator.rule("fps")
def _validate_fps(val) -> bool:
    return isinstance(val, (int, float)) and 0 <= val <= 1000

@validator.rule("frame_time")
def _validate_frame_time(val) -> bool:
    return isinstance(val, (int, float)) and val >= 0.1

@validator.rule("gpu_temp")
def _validate_gpu_temp(val) -> bool:
    return isinstance(val, (int, float)) and 30.0 <= val <= 105.0
