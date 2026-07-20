import random
import math

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def spawn_random_location(bounds):
    x = random.uniform(bounds['x_min'], bounds['x_max'])
    y = random.uniform(bounds['y_min'], bounds['y_max'])
    return (x, y)


def clamp(value, min_value, max_value):
    return max(min_value, min(max_value, value))


def linear_interpolate(start, end, t):
    return (1 - t) * start + t * end


def random_choice(choices):
    return random.choice(choices)


def is_within_bounds(point, bounds):
    return (bounds['x_min'] <= point[0] <= bounds['x_max'] and
            bounds['y_min'] <= point[1] <= bounds['y_max'])
