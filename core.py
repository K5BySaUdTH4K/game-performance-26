import random
import time

class Game:
    def __init__(self, title):
        self.title = title
        self.score = 0
        self.high_score = 0
        self.start_time = time.time()

    def play(self):
        while True:
            action = self.get_user_input()
            if action == 'quit':
                break
            self.process_action(action)
        self.end_game()

    def get_user_input(self):
        return input(f"{self.title} - Enter action (play/quit): ").strip().lower()

    def process_action(self, action):
        if action == 'play':
            points = random.randint(1, 10)
            self.score += points
            print(f"You scored {points} points! Total score: {self.score}")
        else:
            print("Invalid action, try again.")

    def end_game(self):
        self.high_score = max(self.high_score, self.score)
        elapsed_time = time.time() - self.start_time
        print(f"Game over! Your score: {self.score} | High score: {self.high_score} | Time played: {elapsed_time:.2f} seconds.")

if __name__ == '__main__':
    game = Game('Awesome Game')
    game.play()