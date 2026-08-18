import random
import math

def random_position(x_min, x_max, y_min, y_max):
    return (random.uniform(x_min, x_max), random.uniform(y_min, y_max))


def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def lerp(start, end, t):
    return start + (end - start) * t


def is_point_in_rect(point, rect):
    return rect[0] <= point[0] <= rect[0] + rect[2] and rect[1] <= point[1] <= rect[1] + rect[3]


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def generate_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))