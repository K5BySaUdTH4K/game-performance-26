import random
import math

def random_position(max_x, max_y):
    return random.randint(0, max_x), random.randint(0, max_y)


def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def lerp(start, end, t):
    return start + (end - start) * t


def shuffle_list(input_list):
    shuffled = input_list[:]
    random.shuffle(shuffled)
    return shuffled


def interpolate_color(color1, color2, t):
    return (
        int(lerp(color1[0], color2[0], t)),
        int(lerp(color1[1], color2[1], t)),
        int(lerp(color1[2], color2[2], t))
    )


def create_grid(rows, cols):
    return [[(x, y) for x in range(cols)] for y in range(rows)]

