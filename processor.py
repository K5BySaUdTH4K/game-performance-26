import random
import json

class GameProcessor:
    def __init__(self):
        self.score = 0
        self.max_score = 100

    def process_input(self, user_input):
        try:
            if not isinstance(user_input, int):
                raise ValueError('Input must be an integer.')
            if user_input < 0 or user_input > 10:
                raise ValueError('Input must be between 0 and 10.')
            self.score += user_input
            if self.score >= self.max_score:
                return self.end_game()
            return self.continue_game()
        except ValueError as e:
            return json.dumps({'error': str(e)})

    def continue_game(self):
        return json.dumps({'status': 'Continue', 'current_score': self.score})

    def end_game(self):
        return json.dumps({'status': 'Game Over', 'final_score': self.score})

if __name__ == '__main__':
    game = GameProcessor()
    inputs = [random.randint(-5, 15) for _ in range(20)]
    for user_input in inputs:
        result = game.process_input(user_input)
        print(result)