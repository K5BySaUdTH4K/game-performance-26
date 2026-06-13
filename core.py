import time

class GameCore:
    def __init__(self):
        self.entities = []
        self.render_time = 0

    def add_entity(self, entity):
        self.entities.append(entity)

    def update_entities(self):
        for entity in self.entities:
            entity.update()

    def render(self):
        start_time = time.time()
        self.update_entities()
        for entity in self.entities:
            entity.render()
        self.render_time = time.time() - start_time

    def get_render_time(self):
        return self.render_time

class GameEntity:
    def __init__(self, name):
        self.name = name

    def update(self):
        pass  # Placeholder for update logic

    def render(self):
        print(f'Rendering {self.name}')  

# Example usage
if __name__ == '__main__':
    game = GameCore()
    player = GameEntity('Player')
    enemy = GameEntity('Enemy')
    game.add_entity(player)
    game.add_entity(enemy)
    game.render()
    print(f'Time taken to render: {game.get_render_time():.5f} seconds')