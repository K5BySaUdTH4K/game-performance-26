import random
import time

class GameProcessor:
    def __init__(self, players):
        self.players = players
        self.scores = {player: 0 for player in players}

    def roll_dice(self):
        return random.randint(1, 6)

    def update_score(self, player, points):
        self.scores[player] += points
        return self.scores[player]

    def simulate_turn(self, player):
        roll = self.roll_dice()
        print(f"{player} rolled a {roll}")
        self.update_score(player, roll)
        print(f"{player}'s new score: {self.scores[player]}")
        return roll

    def game_loop(self, turns):
        for turn in range(turns):
            for player in self.players:
                time.sleep(1)  # Simulate time taken for player to roll
                self.simulate_turn(player)

if __name__ == '__main__':
    game = GameProcessor(['Alice', 'Bob'])
    game.game_loop(3)