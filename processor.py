def process_game_data(game_data):
    processed_data = []
    for item in game_data:
        processed_item = {
            'name': item['name'],
            'score': item['score'],
            'level': item.get('level', 1),
        }
        processed_data.append(processed_item)
    return processed_data


def calculate_average_score(game_data):
    total_score = sum(item['score'] for item in game_data)
    average_score = total_score / len(game_data) if game_data else 0
    return average_score


def filter_high_scores(game_data, threshold):
    return [item for item in game_data if item['score'] > threshold]


def format_scoreboard(processed_data):
    scoreboard = "Scoreboard:\n"
    for item in processed_data:
        scoreboard += f"{item['name']} - Level: {item['level']}, Score: {item['score']}\n"
    return scoreboard