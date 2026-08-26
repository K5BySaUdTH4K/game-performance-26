# game-performance-26

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

game-performance-26 is a Python toolkit that monitors performance metrics in real-time game applications. Developers can use it to measure frame times, CPU load, and memory consumption to optimize their games effectively.

## Features
- Real-time FPS and frame timing analysis with high precision
- Detailed CPU and RAM usage tracking for each game update cycle
- Export performance logs in JSON and CSV formats for post-analysis
- Minimal performance overhead for use in both testing and production

## Installation
Install via pip:

```bash
pip install game-performance-26
```

## Usage
```python
from game_performance_26 import Monitor

monitor = Monitor()

while running:
    monitor.begin_frame()
    # Handle events, update logic, render
    monitor.end_frame()

print(f"Average FPS: {monitor.get_fps()}")
monitor.save_report("perf_data.json")
```

## License
MIT License