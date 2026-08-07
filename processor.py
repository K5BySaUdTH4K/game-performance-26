import json
import random

def main_loop():
    while True:
        user_input = input('Enter a number between 1 and 10: ')
        if not validate_input(user_input):
            print('Invalid input, please try again.')
            continue
        number = int(user_input)
        result = process_number(number)
        print(f'Result of processing: {result}')
        if number == 0:
            break


def validate_input(user_input):
    if user_input.isdigit():
        number = int(user_input)
        return 1 <= number <= 10
    return False


def process_number(number):
    return number * random.randint(1, 5)


if __name__ == '__main__':
    main_loop()