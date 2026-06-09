import random

class GameHandler:
    def __init__(self):
        self.players = []
        self.rounds = 0

    def add_player(self, name):
        self.players.append(name)
        print(f'Player {name} added.')

    def start_game(self):
        if len(self.players) < 2:
            raise ValueError('At least 2 players required.')
        self.rounds = 5  # predefined rounds
        print(f'Game starting with {self.rounds} rounds.')

    def play_round(self):
        if self.rounds <= 0:
            print('No rounds left to play!')
            return
        winner = random.choice(self.players)
        print(f'Round winner: {winner}')
        self.rounds -= 1

    def end_game(self):
        print('Game Over!')
        self.players = []
        self.rounds = 0

if __name__ == '__main__':
    handler = GameHandler()
    handler.add_player('Alice')
    handler.add_player('Bob')
    handler.start_game()
    for _ in range(5):
        handler.play_round()
    handler.end_game()