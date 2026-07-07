import numpy as np

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width))
        self.player_position = (height // 2, width // 2)

    def move_player(self, direction):
        y, x = self.player_position
        movements = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
        if direction in movements:
            dy, dx = movements[direction]
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < self.height and 0 <= new_x < self.width:
                self.player_position = (new_y, new_x)
                return True
        return False

    def render(self):
        grid_copy = self.grid.copy()
        y, x = self.player_position
        grid_copy[y, x] = 1  # Representing player
        print(grid_copy)

    def reset(self):
        self.grid.fill(0)
        self.player_position = (self.height // 2, self.width // 2)