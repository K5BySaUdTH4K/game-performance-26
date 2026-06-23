import random
import numpy as np

def generate_random_position(x_limit, y_limit):
    return random.randint(0, x_limit), random.randint(0, y_limit)


def calculate_distance(point_a, point_b):
    return np.sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)


def normalize_vector(vector):
    magnitude = np.sqrt(sum(v ** 2 for v in vector))
    return tuple(v / magnitude for v in vector) if magnitude > 0 else vector


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def random_color():
    return tuple(random.randint(0, 255) for _ in range(3))


def lerp(start, end, t):
    return start + (end - start) * t


def radians_to_degrees(radians):
    return radians * (180.0 / np.pi)


def degrees_to_radians(degrees):
    return degrees * (np.pi / 180.0)