import time
import numpy as np

def optimized_game_logic(game_state):
    start_time = time.time()
    next_positions = np.empty_like(game_state['positions'])
    for i, pos in enumerate(game_state['positions']):
        next_positions[i] = calculate_next_position(pos, game_state['velocities'][i])
    game_state['positions'] = next_positions
    elapsed_time = time.time() - start_time
    print(f"Optimized loop executed in {elapsed_time:.6f} seconds")


def calculate_next_position(position, velocity):
    new_position = position + velocity
    return new_position


def main_loop():
    game_state = {'positions': np.array([[0, 0], [1, 1], [2, 2]]), 'velocities': np.array([[0.1, 0.1], [0.2, 0.2], [0.3, 0.3]])}
    while True:
        optimized_game_logic(game_state)
        time.sleep(0.1)  # Simulate frame delay

if __name__ == '__main__':
    main_loop()