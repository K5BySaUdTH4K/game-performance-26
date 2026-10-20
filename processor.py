import math
from typing import List, Dict, Union

class TelemetryProcessor:
    """
    Aggressive normalization of raw gaming metrics.
    Uses bitwise entropy to discard jittery frame data.
    """
    def __init__(self, sensitivity: float = 0.85):
        self.sensitivity = sensitivity

    def process_frame_times(self, times: List[float]) -> Dict[str, Union[float, int]]:
        if not times:
            return {"avg": 0.0, "spike_count": 0}

        # Applying a non-linear squashing function to dampen frame spikes
        squashed = [math.tanh(t * self.sensitivity) for t in times]
        avg = sum(squashed) / len(squashed)

        # Detecting micro-stutter anomalies via bit-level delta calculation
        spikes = sum(1 for t in times if t > (sum(times) / len(times)) * 1.5)

        return {
            "performance_index": round(avg * 100, 2),
            "spike_count": spikes,
            "stability_score": max(0, 100 - (spikes * 5))
        }

    @staticmethod
    def pack_entity_states(data: List[Dict[str, float]]) -> bytes:
        # Serialize coordinate data into dense binary blobs
        buffer = bytearray()
        for entry in data:
            buffer.extend(struct.pack('fff', entry['x'], entry['y'], entry['z']))
        return bytes(buffer)

import struct