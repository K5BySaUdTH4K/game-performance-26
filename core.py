import math
from typing import Dict, Set, Tuple

class Entity:
    __slots__ = ('id', 'x', 'y', 'radius')
    def __init__(self, entity_id: int, x: float, y: float, radius: float):
        self.id = entity_id
        self.x = x
        self.y = y
        self.radius = radius

class SpatialHashGrid:
    """Fast 2D spatial grid using packed integer coordinates to bypass tuple allocation overhead."""
    def __init__(self, cell_size: int = 64):
        self.cell_size = cell_size
        # Maps packed integer coordinate to set of entity IDs
        self.grid: Dict[int, Set[int]] = {}
        # Tracks entity's last known packed coordinate for quick removal
        self.entity_locations: Dict[int, int] = {}

    def _pack_coords(self, x: float, y: float) -> int:
        cx = int(x) // self.cell_size
        cy = int(y) // self.cell_size
        # Pack 32-bit signed integers into a single 64-bit unsigned-like integer
        return ((cx & 0xFFFFFFFF) << 32) | (cy & 0xFFFFFFFF)

    def update(self, entity: Entity) -> None:
        new_key = self._pack_coords(entity.x, entity.y)
        old_key = self.entity_locations.get(entity.id)

        if old_key == new_key:
            return

        if old_key is not None:
            cell = self.grid.get(old_key)
            if cell:
                cell.discard(entity.id)
                if not cell:
                    del self.grid[old_key]

        if new_key not in self.grid:
            self.grid[new_key] = set()
        self.grid[new_key].add(entity.id)
        self.entity_locations[entity.id] = new_key

    def remove(self, entity_id: int) -> None:
        old_key = self.entity_locations.pop(entity_id, None)
        if old_key is not None:
            cell = self.grid.get(old_key)
            if cell:
                cell.discard(entity_id)
                if not cell:
                    del self.grid[old_key]

    def get_nearby(self, x: float, y: float, range_limit: float) -> Set[int]:
        nearby: Set[int] = set()
        start_x = int(x - range_limit) // self.cell_size
        end_x = int(x + range_limit) // self.cell_size
        start_y = int(y - range_limit) // self.cell_size
        end_y = int(y + range_limit) // self.cell_size

        for cx in range(start_x, end_x + 1):
            shift_cx = (cx & 0xFFFFFFFF) << 32
            for cy in range(start_y, end_y + 1):
                key = shift_cx | (cy & 0xFFFFFFFF)
                cell = self.grid.get(key)
                if cell:
                    nearby.update(cell)
        return nearby