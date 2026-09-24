from typing import Dict, Set


class SpatialGridOptimizer:
    """Fast 2D spatial hashing for game entities using bit-packed coordinates."""

    def __init__(self, cell_size: int = 64):
        self.cell_size = cell_size
        # Maps packed 64-bit coordinate integers to sets of entity IDs
        self.grid: Dict[int, Set[int]] = {}
        # Tracks entity last known packed positions to allow fast moves
        self.entity_positions: Dict[int, int] = {}

    def _pack_coords(self, x: float, y: float) -> int:
        # Shift coordinate space to positive-only quadrant for simple bitwise packing
        grid_x = int(x // self.cell_size) + 0x7FFFFFFF
        grid_y = int(y // self.cell_size) + 0x7FFFFFFF
        return (grid_x << 32) | grid_y

    def update_entity(self, entity_id: int, x: float, y: float) -> None:
        new_key = self._pack_coords(x, y)
        old_key = self.entity_positions.get(entity_id)

        if old_key == new_key:
            return

        if old_key is not None:
            cell = self.grid.get(old_key)
            if cell:
                cell.discard(entity_id)
                if not cell:
                    del self.grid[old_key]

        if new_key not in self.grid:
            self.grid[new_key] = set()
        self.grid[new_key].add(entity_id)
        self.entity_positions[entity_id] = new_key

    def remove_entity(self, entity_id: int) -> None:
        old_key = self.entity_positions.pop(entity_id, None)
        if old_key is not None:
            cell = self.grid.get(old_key)
            if cell:
                cell.discard(entity_id)
                if not cell:
                    del self.grid[old_key]

    def get_nearby(self, x: float, y: float, radius: float) -> Set[int]:
        nearby_entities: Set[int] = set()
        min_x, max_x = x - radius, x + radius
        min_y, max_y = y - radius, y + radius

        min_gx = int(min_x // self.cell_size) + 0x7FFFFFFF
        max_gx = int(max_x // self.cell_size) + 0x7FFFFFFF
        min_gy = int(min_y // self.cell_size) + 0x7FFFFFFF
        max_gy = int(max_y // self.cell_size) + 0x7FFFFFFF

        for gx in range(min_gx, max_gx + 1):
            shifted_gx = gx << 32
            for gy in range(min_gy, max_gy + 1):
                key = shifted_gx | gy
                if key in self.grid:
                    nearby_entities.update(self.grid[key])

        return nearby_entities
