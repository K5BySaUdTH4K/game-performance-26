import json
from typing import List, Dict, Any

def process_game_data(game_data: List[Dict[str, Any]]) -> str:
    processed_data = []
    for game in game_data:
        processed_entry = {
            'title': game.get('title', 'Unknown Title'),
            'platform': game.get('platform', 'Unknown Platform'),
            'release_year': game.get('release_year', 'N/A'),
            'rating': game.get('rating', 0),
            'genre': game.get('genre', 'General')
        }
        processed_data.append(processed_entry)
    return json.dumps(processed_data, indent=4)

if __name__ == '__main__':
    example_data = [
        {'title': 'Game A', 'platform': 'PC', 'release_year': 2020, 'rating': 9.5, 'genre': 'Action'},
        {'title': 'Game B', 'platform': 'Console', 'release_year': 2021, 'rating': 8.0}
    ]
    print(process_game_data(example_data))