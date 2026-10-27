import time
from collections import deque

class FramePacer:
    """Adaptive frame time stabilizer with ring-buffered tick deltas."""
    
    def __init__(self, target_fps=60.0, sample_size=120):
        self.target_frame_time = 1.0 / target_fps
        self.samples = deque(maxlen=sample_size)
        self.last_tick = time.perf_counter()
        self._accumulator = 0.0

    def sync(self):
        now = time.perf_counter()
        delta = now - self.last_tick
        self.last_tick = now
        self.samples.append(delta)
        
        avg_delta = sum(self.samples) / len(self.samples)
        self._accumulator += delta
        
        ticks_due = 0
        while self._accumulator >= self.target_frame_time:
            ticks_due += 1
            self._accumulator -= self.target_frame_time
            
        return ticks_due, avg_delta

class EntityBatcher:
    """Sliced batch updater for non-blocking entity ticks."""
    
    def __init__(self, slice_ratio=4):
        self.slice_ratio = slice_ratio

    def optimize_ticks(self, entities, delta):
        active = [e for e in entities if getattr(e, 'is_active', True)]
        step = max(1, len(active) // self.slice_ratio)
        
        for i in range(0, len(active), step):
            chunk = active[i:i + step]
            for entity in chunk:
                if hasattr(entity, 'update'):
                    entity.update(delta)
        return len(active)

def create_optimized_loop(engine_callback, target_fps=144.0):
    pacer = FramePacer(target_fps=target_fps)
    batcher = EntityBatcher()
    
    def step_frame(entities):
        ticks, avg_delta = pacer.sync()
        processed = 0
        for _ in range(ticks):
            processed += batcher.optimize_ticks(entities, avg_delta)
        engine_callback(ticks, avg_delta)
        return processed, avg_delta
        
    return step_frame