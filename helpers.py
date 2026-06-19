import json
from typing import Any, Dict, List

def load_game_data(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading game data: {e}")
        return {}


def save_game_data(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_player_score(game_data: Dict[str, Any], player_id: str, score_delta: int) -> None:
    players = game_data.get('players', [])
    for player in players:
        if player['id'] == player_id:
            player['score'] += score_delta
            break


def get_top_players(game_data: Dict[str, Any], top_n: int = 5) -> List[Dict[str, Any]]:
    players = game_data.get('players', [])
    sorted_players = sorted(players, key=lambda x: x['score'], reverse=True)
    return sorted_players[:top_n]
