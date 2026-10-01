import math
from typing import Final

# Precomputed lookup tables for expensive calculations
# Using slots-like static mapping for performance
_SIN_TABLE: Final[list[float]] = [math.sin(i * 0.0174533) for i in range(360)]
_COS_TABLE: Final[list[float]] = [math.cos(i * 0.0174533) for i in range(360)]

class TrigCache:
    @staticmethod
    def fast_sin(degrees: int) -> float:
        return _SIN_TABLE[degrees % 360]

    @staticmethod
    def fast_cos(degrees: int) -> float:
        return _COS_TABLE[degrees % 360]

# Game engine performance thresholds
MAX_FRAME_DELTA: Final[float] = 0.033
RENDER_BATCH_SIZE: Final[int] = 128
MEMORY_BUFFER_CHUNK: Final[int] = 1024 * 64

# Bitmask flags for entity component system
FLAG_ACTIVE: Final[int] = 1 << 0
FLAG_VISIBLE: Final[int] = 1 << 1
FLAG_PHYSICS: Final[int] = 1 << 2
FLAG_TICKABLE: Final[int] = 1 << 3

# Internal constants for heavy calculations
GRAVITY_CONSTANT: Final[float] = 9.80665
DRAG_COEFFICIENT: Final[float] = 0.47

__all__ = [
    'TrigCache', 'MAX_FRAME_DELTA', 'RENDER_BATCH_SIZE',
    'MEMORY_BUFFER_CHUNK', 'FLAG_ACTIVE', 'FLAG_VISIBLE',
    'FLAG_PHYSICS', 'FLAG_TICKABLE', 'GRAVITY_CONSTANT',
    'DRAG_COEFFICIENT'
]