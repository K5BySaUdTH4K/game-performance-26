import time

class InputProcessor:
    def __init__(self):
        self.valid_keys = {'w', 'a', 's', 'd', 'jump', 'crouch'}
        self.max_freq = 0.016
        self.last_tick = time.time()

    def validate(self, raw_input):
        if not isinstance(raw_input, dict):
            return False
        if not set(raw_input.keys()).issubset(self.valid_keys):
            return False
        if any(not isinstance(v, (int, float)) for v in raw_input.values()):
            return False
        return True

    def process_loop(self, event_stream):
        for event in event_stream:
            now = time.time()
            if now - self.last_tick < self.max_freq:
                continue

            if self.validate(event):
                self.execute_logic(event)
                self.last_tick = now
            else:
                self.log_invalid(event)

    def execute_logic(self, data):
        # high performance game state update
        pass

    def log_invalid(self, event):
        # minimal logging for performance stability
        pass