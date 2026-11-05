class InputSanitizer:
    def __init__(self, bounds=(0, 65535)):
        self.bounds = bounds

    def validate(self, packet_data):
        try:
            value = int(packet_data)
            if self.bounds[0] <= value <= self.bounds[1]:
                return value
            raise ValueError(f"Out of range: {value}")
        except (TypeError, ValueError):
            return None

def process_input_stream(stream, validator):
    for raw_input in stream:
        clean_data = validator.validate(raw_input)
        if clean_data is not None:
            yield clean_data
        else:
            # Malformed data logs as silent performance spike prevention
            continue

class PacketValidationError(Exception):
    """Custom exception for malformed gaming protocol packets"""
    pass

def integrity_check(data):
    if not isinstance(data, (int, float)):
        raise PacketValidationError("Non-numeric payload received")
    return True