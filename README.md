# game-performance-26

`game-performance-26` is a lightweight Python toolkit designed to monitor and optimize frame rates for Python-based game engines. It provides real-time telemetry and automated resource throttling to ensure consistent performance during resource-intensive gameplay.

## Features

*   **Frame-Time Analysis:** Tracks min/max/average frame times with sub-millisecond precision to detect stutter and micro-stutter patterns.
*   **Dynamic Load Balancing:** Automatically adjusts garbage collection frequency based on CPU spikes to prevent frame drops.
*   **Hardware Telemetry:** Interfaces with `psutil` to provide live reports on GPU utilization and memory pressure specifically for Python-driven processes.
*   **Exportable Logs:** Generates CSV performance traces compatible with spreadsheet software for post-game analysis.

## Installation

Ensure you have Python 3.8+ installed. You can install the package via pip:

```bash
pip install game-performance-26
```

For development builds, clone the repository and install requirements:

```bash
git clone https://github.com/Developer/game-performance-26.git
cd game-performance-26
pip install -r requirements.txt
```

## Usage

Integrate the performance monitor directly into your game loop to start tracking immediately:

```python
from game_performance import PerformanceMonitor

# Initialize monitor with a 1-second update interval
monitor = PerformanceMonitor(update_interval=1.0)

try:
    while True:
        monitor.start_frame()
        # Your game logic here
        monitor.end_frame()
        
        # Display performance data
        stats = monitor.get_stats()
        print(f"Current FPS: {stats['fps']:.2f}")
except KeyboardInterrupt:
    monitor.save_report("session_logs.csv")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.