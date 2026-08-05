import random
import time

class Game:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.state = 'initialized'

    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)
            print(f'{player} added to {self.name}')
        else:
            print(f'{player} already in the game')

    def start(self):
        if len(self.players) < 2:
            print('Not enough players to start the game.')
            return
        self.state = 'started'
        print(f'{self.name} has started!')
        self.play()

    def play(self):
        while self.state == 'started':
            print('Game is in progress...')
            time.sleep(1)
            self.check_winner()

    def check_winner(self):
        if random.choice([True, False]):
            self.state = 'ended'
            print('The game has ended!')


game = Game('Epic Adventure')
game.add_player('Alice')
game.add_player('Bob')
game.start()