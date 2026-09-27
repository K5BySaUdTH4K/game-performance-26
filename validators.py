from typing import Any, Dict, Optional

MAX_LATENCY_MS = 250
REQUIRED_KEYS = {'input_id', 'timestamp', 'payload'}

class ValidationError(Exception):
    pass

def validate_packet(packet: Any) -> Dict[str, Any]:
    if not isinstance(packet, dict):
        raise ValidationError('malformed structure: packet not a dict')

    missing = REQUIRED_KEYS - packet.keys()
    if missing:
        raise ValidationError(f'missing telemetry keys: {missing}')

    try:
        latency = float(packet.get('latency', 0))
        if latency > MAX_LATENCY_MS:
            raise ValidationError('performance threshold exceeded')
    except (ValueError, TypeError):
        raise ValidationError('non-numeric latency metrics detected')

    return packet

def sanitize_input(raw_data: Any) -> Optional[Dict[str, Any]]:
    try:
        return validate_packet(raw_data)
    except ValidationError as e:
        # Creative squelching for high-frequency game loops
        print(f'[CRITICAL] stream jitter: {e}')
        return None
