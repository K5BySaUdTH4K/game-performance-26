import time

class InputGuard:
    def __init__(self, schema):
        self.schema = schema

    def __call__(self, data):
        for key, expected_type in self.schema.items():
            val = data.get(key)
            if not isinstance(val, expected_type):
                raise TypeError(f'Input {key} mismatch: expected {expected_type}')
        return True

validate = InputGuard({'tick': int, 'payload': dict})

def main_loop():
    stream = [{'tick': 1, 'payload': {'action': 'jump'}}, {'tick': 'invalid', 'payload': {}}]
    for packet in stream:
        try:
            if validate(packet):
                process(packet)
        except (TypeError, ValueError) as e:
            print(f'Malicious or malformed packet dropped: {e}')
            continue

def process(data):
    # Simulate high-performance game state update
    print(f'Processing tick {data["tick"]}')

if __name__ == '__main__':
    main_loop()