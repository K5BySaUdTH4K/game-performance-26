import random
import logging

def process_game_data(data):
    if not isinstance(data, list):
        logging.error('Input data is not a list.')
        raise ValueError('Expected a list of game data.')
    if len(data) == 0:
        logging.warning('Received an empty list.')
        return 'No data to process'
    
    processed_data = []
    for item in data:
        if not isinstance(item, dict):
            logging.error(f'Invalid item in list: {item}')
            continue
        try:
            score = item.get('score', 0)
            if score < 0:
                raise ValueError('Score cannot be negative')
            level = item.get('level', 1)
            processed_data.append({'score': score, 'level': level})
        except ValueError as ve:
            logging.error(f'Error processing item {item}: {ve}')
    
    if len(processed_data) == 0:
        logging.info('No valid data processed.')
    return processed_data

# Simulate some game data to test the function
if __name__ == '__main__':
    example_data = [
        {'score': random.randint(-10, 100), 'level': random.randint(1, 10)},
        {'score': 50.5, 'level': 2},
        {'level': 3},
        'invalid_item',
        {}  # This will be ignored as it does not contain score
    ]
    print(process_game_data(example_data))