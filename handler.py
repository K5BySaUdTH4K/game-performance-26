import json

def validate_input(user_input):
    if isinstance(user_input, str) and len(user_input) > 0:
        return True
    return False

class GameHandler:
    def __init__(self):
        self.players = []
        
    def main_loop(self):
        while True:
            user_input = input("Enter player name (or 'quit' to exit): ")
            if user_input.lower() == 'quit':
                break
            if validate_input(user_input):
                self.players.append(user_input)
                self.process_input(user_input)
            else:
                print("Invalid input, try again.")

    def process_input(self, player_name):
        print(f"Processing player: {player_name}")

if __name__ == '__main__':
    game_handler = GameHandler()
    game_handler.main_loop()