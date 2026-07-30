from typing import List, Dict


def calculate_frame_rate(frames: int, time_elapsed: float) -> float:
    """Calculate frame rate based on frames and elapsed time.
    
    Args:
        frames (int): The number of frames rendered.
        time_elapsed (float): The time elapsed in seconds.
    
    Returns:
        float: The calculated frame rate (frames per second).
    """
    if time_elapsed <= 0:
        return 0.0
    return frames / time_elapsed


def load_assets(asset_list: List[str]) -> Dict[str, str]:
    """Load assets and return a dictionary of loaded assets.
    
    Args:
        asset_list (List[str]): A list of asset file paths.
    
    Returns:
        Dict[str, str]: A dictionary with asset names as keys and their paths as values.
    """
    loaded_assets = {}
    for asset in asset_list:
        loaded_assets[asset] = f'Loaded: {asset}'  # Simulated loading
    return loaded_assets


def find_high_score(scores: List[int]) -> int:
    """Find the highest score from a list of scores.
    
    Args:
        scores (List[int]): A list of integer scores.
    
    Returns:
        int: The highest score found or 0 if the list is empty.
    """
    return max(scores, default=0)


def reset_game() -> None:
    """Reset the game settings to their initial values."""
    print("Game has been reset.")
