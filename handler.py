import random
import time

class GameHandler:
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0
        self.start_time = time.time()

    def roll_dice(self):
        return random.randint(1, 6)

    def play_turn(self):
        dice_value = self.roll_dice()
        print(f'{self.player_name} rolled a {dice_value}.')
        self.update_score(dice_value)

    def update_score(self, value):
        self.score += value
        print(f'Current score: {self.score}')

    def game_duration(self):
        elapsed = time.time() - self.start_time
        print(f'Game duration: {elapsed:.2f} seconds')

    def reset_game(self):
        self.score = 0
        self.start_time = time.time()
        print('Game has been reset.')

# Example usage
if __name__ == '__main__':
    player = GameHandler('Alice')
    for _ in range(3):
        player.play_turn()
    player.game_duration()
    player.reset_game()