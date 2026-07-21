import random

def random_position(max_x, max_y):
    return random.randint(0, max_x), random.randint(0, max_y)


def distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


def load_game_data(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def save_game_data(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)


def shuffle_list(items):
    random.shuffle(items)
    return items


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def interpolate(value1, value2, factor):
    return value1 + (value2 - value1) * factor


def apply_damage(health, damage):
    return max(0, health - damage)


def is_within_bounds(point, bounds):
    return bounds[0][0] <= point[0] <= bounds[1][0] and bounds[0][1] <= point[1] <= bounds[1][1]