import array
import math
from typing import Iterator


class ZeroAllocSpatialGrid:
    """High-performance 2D spatial grid using flattened typed arrays for zero-alloc game updates."""

    __slots__ = ('cell_size', 'width', 'height', 'grid', 'counts', 'max_per_cell')

    def __init__(self, width: int = 1920, height: int = 1080, cell_size: int = 64, max_per_cell: int = 16):
        self.cell_size = cell_size
        self.width = math.ceil(width / cell_size)
        self.height = math.ceil(height / cell_size)
        self.max_per_cell = max_per_cell
        total_cells = self.width * self.height
        self.grid = array.array('i', [-1] * (total_cells * max_per_cell))
        self.counts = array.array('H', [0] * total_cells)

    def clear(self) -> None:
        for i in range(len(self.counts)):
            self.counts[i] = 0

    def _hash(self, x: float, y: float) -> int:
        cx = max(0, min(self.width - 1, int(x // self.cell_size)))
        cy = max(0, min(self.height - 1, int(y // self.cell_size)))
        return cy * self.width + cx

    def insert(self, entity_id: int, x: float, y: float) -> bool:
        cell_idx = self._hash(x, y)
        cnt = self.counts[cell_idx]
        if cnt >= self.max_per_cell:
            return False
        offset = cell_idx * self.max_per_cell + cnt
        self.grid[offset] = entity_id
        self.counts[cell_idx] = cnt + 1
        return True

    def query_cell(self, x: float, y: float) -> Iterator[int]:
        cell_idx = self._hash(x, y)
        cnt = self.counts[cell_idx]
        base = cell_idx * self.max_per_cell
        for i in range(cnt):
            yield self.grid[base + i]


class FrameBatchProcessor:
    """Processes entity transforms in contiguous float dynamic buffers for cache locality."""

    __slots__ = ('capacity', 'count', 'positions', 'velocities')

    def __init__(self, capacity: int = 10000):
        self.capacity = capacity
        self.count = 0
        self.positions = array.array('f', [0.0] * (capacity * 2))
        self.velocities = array.array('f', [0.0] * (capacity * 2))

    def add_entity(self, x: float, y: float, vx: float, vy: float) -> int:
        if self.count >= self.capacity:
            raise OverflowError("Frame batch entity capacity reached")
        idx = self.count
        self.positions[idx * 2] = x
        self.positions[idx * 2 + 1] = y
        self.velocities[idx * 2] = vx
        self.velocities[idx * 2 + 1] = vy
        self.count += 1
        return idx

    def step_physics(self, delta_time: float) -> None:
        dt = float(delta_time)
        pos = self.positions
        vel = self.velocities
        for i in range(self.count * 2):
            pos[i] += vel[i] * dt
