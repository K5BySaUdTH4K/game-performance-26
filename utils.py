import random
import numpy as np

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)


def shuffle_list(input_list):
    shuffled = input_list.copy()
    random.shuffle(shuffled)
    return shuffled


def calculate_average(numbers):
    if not numbers:
        raise ValueError('List of numbers cannot be empty')
    return sum(numbers) / len(numbers)


def normalize_data(data):
    if not data:
        raise ValueError('Data cannot be empty')
    mean = np.mean(data)
    std_dev = np.std(data)
    return [(x - mean) / std_dev for x in data]


def load_json_file(filepath):
    import json
    with open(filepath, 'r') as file:
        return json.load(file)


def save_json_file(filepath, data):
    import json
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)