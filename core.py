import random
import json
from validators import validate_command

def main_loop():
    commands = ['move', 'attack', 'defend', 'exit']
    while True:
        user_input = input('Enter command: ').strip()
        if validate_command(user_input, commands):
            process_command(user_input)
        else:
            print('Invalid command. Please try again.')
        if user_input == 'exit':
            break


def process_command(command):
    action_outcomes = {
        'move': 'You moved forward.',
        'attack': 'You attacked the enemy.',
        'defend': 'You took a defensive stance.'
    }
    print(action_outcomes.get(command, 'Command not recognized.'))

if __name__ == '__main__':
    main_loop()