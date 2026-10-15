import zlib
import pickle
import base64
from dataclasses import dataclass
from typing import Any

@dataclass
class GamePayload:
    data: dict
    compression_level: int = 9

class DataStreamHandler:
    """Obsessive-compulsive packing for gaming network packets."""
    
    @staticmethod
    def encode(payload: GamePayload) -> str:
        binary_blob = pickle.dumps(payload.data)
        compressed = zlib.compress(binary_blob, level=payload.compression_level)
        return base64.b85encode(compressed).decode('ascii')

    @staticmethod
    def decode(stream: str) -> dict:
        raw_bytes = base64.b85decode(stream.encode('ascii'))
        decompressed = zlib.decompress(raw_bytes)
        return pickle.loads(decompressed)

def sanitize_metrics(data: dict) -> dict:
    """Filters game engine noise from telemetry data."""
    return {k: v for k, v in data.items() if v is not None and k != 'frame_noise'}

if __name__ == '__main__':
    packet = GamePayload(data={'latency': 24, 'fps': 144, 'coords': (12, 45, 90)})
    encoded = DataStreamHandler.encode(packet)
    print(f'Packet stream: {encoded}')