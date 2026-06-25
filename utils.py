import random
import logging

logging.basicConfig(level=logging.ERROR)

class GameError(Exception):
    pass

def get_random_number(min_value, max_value):
    if not isinstance(min_value, int) or not isinstance(max_value, int):
        raise GameError("min_value and max_value must be integers")
    if min_value >= max_value:
        raise GameError("min_value must be less than max_value")
    return random.randint(min_value, max_value)

def divide_numbers(numerator, denominator):
    try:
        if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise GameError("Both numerator and denominator must be numbers")
        return numerator / denominator
    except ZeroDivisionError:
        logging.error("Division by zero encountered")
        raise GameError("Denominator cannot be zero")

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        logging.error("File not found: %s", file_path)
        raise GameError("File not found")
    except IOError:
        logging.error("Error reading file: %s", file_path)
        raise GameError("File reading error")
