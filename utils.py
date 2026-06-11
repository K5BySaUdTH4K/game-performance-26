from typing import List, Dict, Any


def calculate_average(scores: List[float]) -> float:
    """
    Calculate the average of a list of scores.
    
    Parameters:
    scores (List[float]): A list of float scores.
    
    Returns:
    float: The average of the scores, or 0 if the list is empty.
    """
    return sum(scores) / len(scores) if scores else 0.0


def extract_unique_players(game_data: List[Dict[str, Any]]) -> List[str]:
    """
    Extract unique player names from game data.
    
    Parameters:
    game_data (List[Dict[str, Any]]): A list of dictionaries containing game-related data.
    
    Returns:
    List[str]: A list of unique player names.
    """
    players = {entry['player_name'] for entry in game_data}
    return list(players)


def format_game_duration(seconds: int) -> str:
    """
    Format a duration in seconds into a human-readable string.
    
    Parameters:
    seconds (int): Duration in seconds.
    
    Returns:
    str: The formatted duration.
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{hours}h {minutes}m {seconds}s' if hours else f'{minutes}m {seconds}s'