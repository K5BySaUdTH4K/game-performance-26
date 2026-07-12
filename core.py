import random
import json

class Game:
    def __init__(self):
        self.score = 0
        self.max_score = 100

    def start_game(self):
        print('Game started!')
        self.play_rounds()

    def play_rounds(self):
        while True:
            try:
                user_input = input('Enter a number between 1 and 10 (or type exit to quit): ')
                if user_input.lower() == 'exit':
                    print('Exiting the game...')
                    break
                self.validate_input(user_input)
                user_number = int(user_input)
                self.update_score(user_number)
                print(f'Current score: {self.score}')
            except ValueError as ve:
                print(f'Input error: {ve}')
            except Exception as e:
                print(f'Something went wrong: {e}')

    def validate_input(self, user_input):
        if not user_input.isdigit() or not (1 <= int(user_input) <= 10):
            raise ValueError('Input must be a digit between 1 and 10')

    def update_score(self, user_number):
        self.score += user_number
        if self.score > self.max_score:
            print('Congratulations! You reached the maximum score!')
            self.score = 0

if __name__ == '__main__':
    game = Game()
    game.start_game()