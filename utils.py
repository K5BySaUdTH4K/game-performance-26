import hashlib
from typing import List, Dict, Any
from collections import deque

def _compute_creative_checksum(metadata: str) -> int:
    base = int(hashlib.md5(metadata.encode()).hexdigest()[:8], 16)
    poly = 0
    for char in metadata:
        poly = (poly * 31 + ord(char)) % 10007
    return (base ^ poly) & 0xFFFFFFFF

def pack_gaming_session(player_id: int, score: int, level: int, events: List[str]) -> int:
    if not (0 <= player_id < 2**16 and 0 <= score < 2**32 and 0 <= level < 2**8):
        raise ValueError("Data out of range for packing")
    checksum = _compute_creative_checksum(''.join(events))
    packed = 0
    packed |= (player_id & 0xFFFF) << 48
    packed |= (score & 0xFFFFFFFF) << 16
    packed |= (level & 0xFF) << 8
    packed |= (checksum & 0xFF)
    rotate = 13
    packed = ((packed << rotate) | (packed >> (64 - rotate))) & ((1 << 64) - 1)
    return packed

def unpack_gaming_session(packed: int) -> Dict[str, Any]:
    rotate = 13
    packed = ((packed >> rotate) | (packed << (64 - rotate))) & ((1 << 64) - 1)
    player_id = (packed >> 48) & 0xFFFF
    score = (packed >> 16) & 0xFFFFFFFF
    level = (packed >> 8) & 0xFF
    checksum = packed & 0xFF
    return {
        'player_id': player_id,
        'score': score,
        'level': level,
        'checksum': checksum
    }

def process_gaming_data(sessions: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not sessions:
        return {'total_players': 0, 'avg_score': 0, 'top_level': 0}
    scores = [s.get('score', 0) for s in sessions]
    levels = [s.get('level', 1) for s in sessions]
    queue = deque(sessions)
    processed = []
    while queue:
        current = queue.popleft()
        adj_score = current.get('score', 0) * (1 + current.get('level', 1) / 100.0)
        processed.append(adj_score)
        if len(processed) > 10:
            break
    avg_score = sum(scores) / len(scores)
    top_level = max(levels)
    unique = len({hash(str(s)) for s in sessions})
    return {
        'total_players': len(sessions),
        'avg_score': round(avg_score, 2),
        'top_level': top_level,
        'adjusted_avg': round(sum(processed) / len(processed), 2) if processed else 0,
        'unique_sessions': unique
    }

def handle_gaming_data(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    if isinstance(data, dict):
        data = [data]
    return process_gaming_data(data)
