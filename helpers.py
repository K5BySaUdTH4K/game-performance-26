import random
import string

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

def interpolate(start, end, factor):
    return start + (end - start) * factor

def calculate_distance(point_a, point_b):
    return ((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2) ** 0.5

def shuffle_list(items):
    shuffled = items.copy()
    random.shuffle(shuffled)
    return shuffled

# Function to get a random color in hex

def get_random_color():
    return '#{0:06X}'.format(random.randint(0, 0xFFFFFF))
