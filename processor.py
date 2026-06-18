import sys
import json
import random

def validate_input(user_input):
    if not isinstance(user_input, dict):
        raise ValueError('Input must be a dictionary')
    if 'action' not in user_input or 'value' not in user_input:
        raise KeyError('Input must contain both action and value keys')
    if not isinstance(user_input['value'], int) or user_input['value'] < 0:
        raise ValueError('Value must be a non-negative integer')

def process_action(action, value):
    if action == 'increase':
        print(f'Increasing score by {value}')
        return random.randint(1, 10) * value
    elif action == 'decrease':
        print(f'Decreasing score by {value}')
        return -random.randint(1, 10) * value
    else:
        raise ValueError('Invalid action: Must be increase or decrease')

if __name__ == '__main__':
    user_input = json.loads(sys.stdin.read())
    try:
        validate_input(user_input)
        result = process_action(user_input['action'], user_input['value'])
        print(f'Process result: {result}')
    except (ValueError, KeyError) as e:
        print(f'Error: {e}')
        sys.exit(1)