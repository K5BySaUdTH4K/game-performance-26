import random
import math

def generate_random_position(max_x, max_y):
    return (random.randint(0, max_x), random.randint(0, max_y))


def distance_between_points(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def interpolate(start, end, alpha):
    return start + (end - start) * alpha


def is_point_within_bounds(point, bounds):
    return bounds[0][0] <= point[0] <= bounds[1][0] and bounds[0][1] <= point[1] <= bounds[1][1]


def random_choice_from_list(items):
    return random.choice(items)


def calculate_angle(point1, point2):
    return math.degrees(math.atan2(point2[1] - point1[1], point2[0] - point1[0]))
