# game-performance-26

`game-performance-26` is a lightweight Python toolkit designed to monitor and optimize frame latency and system resource utilization during gaming sessions. It provides real-time telemetry hooks to identify performance bottlenecks and automate system affinity adjustments.

## Features

*   **Latency Profiler:** Tracks micro-stutters and frame-time variance with sub-millisecond precision.
*   **Process Priority Orchestrator:** Automatically elevates thread priority for active game processes to minimize input lag.
*   **Resource Throttling:** Monitors background tasks and applies temporary CPU affinity caps to prevent thermal throttling.
*   **Log Analytics:** Exports session performance data to structured CSV formats for long-term trend analysis.

## Installation

Ensure you have Python 3.8+ installed. It is recommended to use a virtual environment:

```bash
# Clone the repository
git clone https://github.com/Developer/game-performance-26.git
cd game-performance-26

# Install dependencies
pip install -r requirements.txt
```

## Usage

To start a monitoring session for a specific process ID (PID), execute the main script with administrative privileges:

```bash
# Monitor process with PID 1234
python monitor.py --pid 1234 --output ./logs/session_alpha.csv
```

For automated optimization profiles, you can run the daemon mode:

```bash
python monitor.py --daemonize --threshold 16.6ms
```

## Requirements
*   **OS:** Windows 10/11 (requires `pywin32` for priority manipulation)
*   **Python:** 3.8 or newer
*   **Permissions:** Administrator/Root access required for process-level modifications

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.