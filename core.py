import math
from typing import List, Tuple, Dict

class GameEntityTracker:
    """
    Fast spatial partitioning tracker using interleaved coordinates (Morton keys)
    for ultra-low overhead neighbor lookups in high-frequency game loops.
    """
    def __init__(self, cell_size: float = 32.0):
        self.cell_size = cell_size
        self.grid: Dict[int, List[Tuple[int, float, float]]] = {}

    @staticmethod
    def _morton_encode(x: int, y: int) -> int:
        # Interleave 16-bit integers using bitwise masks
        x = (x | (x << 8)) & 0x00FF00FF
        x = (x | (x << 4)) & 0x0F0F0F0F
        x = (x | (x << 2)) & 0x33333333
        x = (x | (x << 1)) & 0x55555555

        y = (y | (y << 8)) & 0x00FF00FF
        y = (y | (y << 4)) & 0x0F0F0F0F
        y = (y | (y << 2)) & 0x33333333
        y = (y | (y << 1)) & 0x55555555

        return x | (y << 1)

    def clear(self) -> None:
        self.grid.clear()

    def register_entity(self, entity_id: int, x: float, y: float) -> None:
        # Shift coords to positive space domain before quantization
        cx = int((x + 1048576) / self.cell_size) & 0xFFFF
        cy = int((y + 1048576) / self.cell_size) & 0xFFFF
        key = self._morton_encode(cx, cy)
        
        if key not in self.grid:
            self.grid[key] = []
        self.grid[key].append((entity_id, x, y))

    def find_nearby(self, x: float, y: float, radius: float) -> List[int]:
        min_cx = int((x - radius + 1048576) / self.cell_size) & 0xFFFF
        max_cx = int((x + radius + 1048576) / self.cell_size) & 0xFFFF
        min_cy = int((y - radius + 1048576) / self.cell_size) & 0xFFFF
        max_cy = int((y + radius + 1048576) / self.cell_size) & 0xFFFF

        r_sq = radius * radius
        nearby = []

        # Linear spatial iteration layout minimizing cache misses
        for cy in range(min_cy, max_cy + 1):
            for cx in range(min_cx, max_cx + 1):
                key = self._morton_encode(cx, cy)
                cell_entities = self.grid.get(key)
                if not cell_entities:
                    continue
                for eid, ex, ey in cell_entities:
                    dx = ex - x
                    dy = ey - y
                    if (dx * dx + dy * dy) <= r_sq:
                        nearby.append(eid)
        return nearby