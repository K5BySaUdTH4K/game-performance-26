import random
import math

def get_random_position(boundaries):
    x = random.uniform(boundaries['x_min'], boundaries['x_max'])
    y = random.uniform(boundaries['y_min'], boundaries['y_max'])
    return (x, y)


def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def is_within_bounds(position, boundaries):
    return (boundaries['x_min'] <= position[0] <= boundaries['x_max'] and
            boundaries['y_min'] <= position[1] <= boundaries['y_max'])


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def interpolate(value1, value2, factor):
    return value1 + (value2 - value1) * factor


def normalize_vector(vector):
    magnitude = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    return (vector[0] / magnitude, vector[1] / magnitude) if magnitude > 0 else (0, 0)