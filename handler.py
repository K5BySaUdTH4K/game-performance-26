import time
import random

class GameHandler:
    def __init__(self):
        self.players = {}

    def add_player(self, player_id):
        if player_id not in self.players:
            self.players[player_id] = {'score': 0, 'last_action_time': time.time()}

    def update_score(self, player_id, score):
        if player_id in self.players:
            current_time = time.time()
            time_since_last_action = current_time - self.players[player_id]['last_action_time']
            if time_since_last_action >= 0.1:
                self.players[player_id]['score'] += score
                self.players[player_id]['last_action_time'] = current_time

    def get_scores(self):
        return {id: data['score'] for id, data in self.players.items()}

    def simulate_gameplay(self):
        for player_id in self.players:
            action_score = random.randint(1, 10)
            self.update_score(player_id, action_score)

if __name__ == '__main__':
    game = GameHandler()
    game.add_player('player1')
    for _ in range(100):
        game.simulate_gameplay()
    print(game.get_scores())