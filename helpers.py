import random
import math

def generate_random_coordinates(min_x, max_x, min_y, max_y):
    return (random.uniform(min_x, max_x), random.uniform(min_y, max_y))


def calculate_distance(point_a, point_b):
    return math.sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def lerp(start, end, t):
    return start + (end - start) * t


def is_point_in_circle(point, circle_center, radius):
    return calculate_distance(point, circle_center) <= radius


def generate_unique_id(existing_ids):
    new_id = random.randint(1, 1000000)
    while new_id in existing_ids:
        new_id = random.randint(1, 1000000)
    existing_ids.add(new_id)
    return new_id
