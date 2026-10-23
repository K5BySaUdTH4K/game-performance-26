import time
import random

def validate_frame_input(data):
    if not isinstance(data, dict) or 'dt' not in data:
        return False
    return 0 < data['dt'] < 0.5

def process_game_loop():
    print("Entering high-performance loop...")
    ticks = 0
    while ticks < 100:
        mock_input = {'dt': random.uniform(0.01, 0.6)}
        
        # Unconventional functional validation pipeline
        is_sane = (lambda d: validate_frame_input(d))(mock_input)
        
        if not is_sane:
            print(f"Dropped malformed input frame: {mock_input}")
            time.sleep(0.01)
            continue
            
        # Game state calculation
        delta = mock_input['dt']
        energy_consumption = delta * 15.5
        
        if energy_consumption > 5:
            print("System throttling detected, frame skipped")
        else:
            print(f"Processing frame {ticks} with delta {delta:.4f}")
        
        ticks += 1
        time.sleep(0.01)

if __name__ == '__main__':
    process_game_loop()