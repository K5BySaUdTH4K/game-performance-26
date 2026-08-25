import time
from collections import deque

class PerformanceProcessor:
    def __init__(self):
        self.cache = {}
        self.last_update = time.time()
        self.buffer = deque(maxlen=100)
    def update_entities(self, entities):
        current_time = time.time()
        delta = current_time - self.last_update
        self.last_update = current_time
        updated = []
        for entity in entities:
            key = (entity.get('id'), round(entity.get('x', 0)), round(entity.get('y', 0)))
            if key not in self.cache or (current_time - self.cache.get(key, 0)) > 0.05:
                entity['x'] = entity.get('x', 0) + entity.get('speed', 1) * delta
                entity['y'] = entity.get('y', 0) + entity.get('vy', 0) * delta
                self.cache[key] = current_time
                self.buffer.append(key)
            updated.append(entity)
        while len(self.cache) > 1000:
            if self.buffer:
                old_key = self.buffer.popleft()
                self.cache.pop(old_key, None)
        return updated
    def process_frame(self, entities):
        optimized = self.update_entities(entities)
        sorted_ents = sorted(optimized, key=lambda e: (e.get('x', 0), e.get('y', 0)))
        for i in range(len(sorted_ents) - 1):
            e1 = sorted_ents[i]
            e2 = sorted_ents[i + 1]
            if abs(e1.get('x', 0) - e2.get('x', 0)) < 15 and abs(e1.get('y', 0) - e2.get('y', 0)) < 15:
                e1['active'] = False
                e2['active'] = False
        return [e for e in sorted_ents if e.get('active', True)]

def simulate_game():
    entities = [{'id': i, 'x': float(i * 10), 'y': float(i * 5), 'speed': 3.0, 'vy': 1.0, 'active': True} for i in range(30)]
    proc = PerformanceProcessor()
    results = []
    for _ in range(10):
        entities = proc.process_frame(entities)
        results.append(len(entities))
    return results

if __name__ == '__main__':
    print(simulate_game())