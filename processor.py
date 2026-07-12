from typing import List, Dict, Any


def process_game_data(game_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Processes a list of game data dictionaries and aggregates statistics.

    Args:
        game_data (List[Dict[str, Any]]): A list of game data containing various metrics.

    Returns:
        Dict[str, Any]: A dictionary with aggregated statistics like total score and average level.
    """
    total_score = sum(item.get('score', 0) for item in game_data)
    total_level = sum(item.get('level', 0) for item in game_data)
    count = len(game_data)

    average_level = total_level / count if count > 0 else 0
    aggregated_data = {
        'total_score': total_score,
        'average_level': average_level,
        'game_count': count,
    }
    return aggregated_data


def display_statistics(stats: Dict[str, Any]) -> None:
    """
    Displays the game statistics in a formatted manner.

    Args:
        stats (Dict[str, Any]): A dictionary containing game statistics to display.
    """
    print("Game Statistics:")
    print(f"Total Score: {stats['total_score']}")
    print(f"Average Level: {stats['average_level']:.2f}")
    print(f"Total Games Processed: {stats['game_count']}")
