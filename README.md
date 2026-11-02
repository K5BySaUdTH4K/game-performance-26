[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# game-performance-26

`game-performance-26` is a lightweight Python telemetry engine designed to capture, log, and analyze real-time frame rates and hardware utilization across DirectX and Vulkan titles. It provides game developers and hardware reviewers with automated frame-time analysis, micro-stutter detection, and overlay-ready metrics exports.

## Features

- **Low-Overhead Frame-Time Tracking**: Captures sub-millisecond frame intervals, calculating real-time averages along with 1% and 0.1% low percentiles.
- **Hardware Telemetry Integration**: Logs GPU/CPU clock speeds, thermal limits, power draw, and VRAM utilization via NVML and native system APIs.
- **Automated Report Generation**: Exports benchmark sessions into clean CSV, JSON, and pre-formatted Markdown summary reports.
- **Process Auto-Attach**: Detects game launches dynamically via executable monitoring without requiring manual process IDs.

## Installation

Ensure you have Python 3.9+ installed on your system.

```bash
git clone https://github.com/Developer/game-performance-26.git
cd game-performance-26
pip install -r requirements.txt
pip install .
```

## Quick Start

The following example attaches the monitor to a running game session, collects 60 seconds of performance data, and exports a summary report.

```python
import time
from game_perf import BenchmarkMonitor, ReportExporter

# Initialize monitor for the target process
monitor = BenchmarkMonitor(target_process="Cyberpunk2077.exe", interval_ms=100)

print("Waiting for target process...")
monitor.start()

# Collect metrics for 60 seconds
time.sleep(60)

# Stop session and calculate results
session_data = monitor.stop()

# Print metrics to console
print(f"Average FPS: {session_data.avg_fps:.2f}")
print(f"1% Low FPS:  {session_data.low_1_percent:.2f}")
print(f"Max GPU Temp: {session_data.max_gpu_temp}°C")

# Export to CSV
exporter = ReportExporter(session_data)
exporter.to_csv("cyberpunk_benchmark.csv")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.