def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    return user_input

def process_input(user_input):
    try:
        validated_input = validate_input(user_input)
        print(f'Processing: {validated_input}')
    except ValueError as e:
        print(f'Input Error: {e}')

# Main processing loop
if __name__ == '__main__':
    while True:
        user_input = input('Enter command: ')
        process_input(user_input)
        if user_input.lower() == 'exit':
            break