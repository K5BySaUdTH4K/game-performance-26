import math
from typing import Final, Dict, Tuple

# Precomputed lookup tables for expensive runtime math
# Memory trade-off for CPU cycles in frame-critical updates

TABLE_SIZE: Final[int] = 1024

SIN_LOOKUP: Final[Tuple[float, ...]] = tuple(
    math.sin(2 * math.pi * i / TABLE_SIZE) for i in range(TABLE_SIZE)
)

COS_LOOKUP: Final[Tuple[float, ...]] = tuple(
    math.cos(2 * math.pi * i / TABLE_SIZE) for i in range(TABLE_SIZE)
)

def fast_sin(theta: float) -> float:
    """Index-based trigonometric approximation for game loops."""
    idx = int((theta / (2 * math.pi)) * TABLE_SIZE) % TABLE_SIZE
    return SIN_LOOKUP[idx]

def fast_cos(theta: float) -> float:
    """Index-based trigonometric approximation for game loops."""
    idx = int((theta / (2 * math.pi)) * TABLE_SIZE) % TABLE_SIZE
    return COS_LOOKUP[idx]

# Cache-friendly spatial constants
GRID_SIZE: Final[int] = 64
TILE_DIM: Final[int] = 32

ENTITY_POOL_LIMIT: Final[int] = 512

PHYSICS_TICK_RATE: Final[float] = 1.0 / 60.0

LOG_LEVEL_MAP: Final[Dict[str, int]] = {
    "DEBUG": 10,
    "INFO": 20,
    "WARN": 30,
    "ERROR": 40
}