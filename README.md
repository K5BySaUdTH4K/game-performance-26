# game-performance-26

`game-performance-26` is a lightweight Python toolkit designed to monitor and optimize system resources during gaming sessions. It helps users track frame time consistency, CPU/GPU utilization, and background process interference in real-time.

### Key Features

*   **Real-time Telemetry:** Stream frame rate and hardware thermals directly to the console or an external dashboard.
*   **Process Governor:** Automatically detects intensive background tasks and lowers their CPU priority while games are active.
*   **Thermal Throttling Alerts:** Configurable logging for temperature spikes that trigger performance drops.
*   **Low-Overhead Profiling:** Built using `psutil` and `cProfile` to ensure the tool consumes less than 1% of total system resources.

### Installation

Requires Python 3.8+ and administrative privileges to manage process priorities.

```bash
# Clone the repository
git clone https://github.com/Developer/game-performance-26.git
cd game-performance-26

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

To begin monitoring your active game process and apply optimization presets, execute the following:

```bash
# Run with default monitoring settings
python main.py --target "Game.exe" --optimize
```

To view a detailed report of system resource usage after a session, use:

```bash
python main.py --report session_logs.json
```

### Configuration
You can adjust the polling interval and target thresholds by editing the `config.yaml` file located in the root directory. Setting the `polling_rate` too low may increase CPU overhead.

### License
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.