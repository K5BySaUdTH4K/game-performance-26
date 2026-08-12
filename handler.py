import json

class GameHandler:
    def __init__(self):
        self.players = []
        self.valid_actions = ['move', 'attack', 'defend']

    def add_player(self, player_name):
        if not isinstance(player_name, str) or len(player_name) == 0:
            raise ValueError('Invalid player name: must be a non-empty string')
        self.players.append(player_name)

    def process_action(self, player_name, action):
        if player_name not in self.players:
            raise ValueError('Player not found')
        if action not in self.valid_actions:
            raise ValueError(f'Invalid action: {action}')
        # Process the action (this is a placeholder)
        return json.dumps({'player': player_name, 'action': action})

    def main_loop(self):
        while True:
            try:
                # Simulate input
                player_name = input('Enter player name: ')
                action = input('Enter action: ')
                self.process_action(player_name, action)
            except ValueError as e:
                print(f'Error: {e}')
            except KeyboardInterrupt:
                print('\nGame ended by user.')
                break

if __name__ == '__main__':
    game_handler = GameHandler()
    game_handler.main_loop()