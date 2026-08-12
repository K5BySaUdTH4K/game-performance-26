from typing import Dict

class GameHandler:
    """
    A class to handle game events and manage game state.
    """

    def __init__(self: 'GameHandler', initial_state: Dict[str, int]) -> None:
        """
        Initializes the GameHandler with a given initial state.
        :param initial_state: A dictionary representing the initial state of the game.
        """
        self.state = initial_state

    def increment_score(self: 'GameHandler', player_id: str, points: int) -> None:
        """
        Increments the player's score by a specified number of points.
        :param player_id: The ID of the player whose score will be increased.
        :param points: The number of points to add to the player's score.
        """
        if player_id in self.state:
            self.state[player_id] += points
        else:
            self.state[player_id] = points

    def reset_game(self: 'GameHandler') -> None:
        """
        Resets the game state to the initial conditions.
        """
        self.state.clear()

    def get_score(self: 'GameHandler', player_id: str) -> int:
        """
        Retrieves the current score for the specified player.
        :param player_id: The ID of the player whose score is requested.
        :return: The current score of the player, or zero if not found.
        """
        return self.state.get(player_id, 0)

if __name__ == '__main__':
    initial_state = {'player1': 0, 'player2': 0}
    game_handler = GameHandler(initial_state)
    game_handler.increment_score('player1', 10)
    print(game_handler.get_score('player1'))  # Output: 10
    game_handler.reset_game()
    print(game_handler.get_score('player1'))  # Output: 0