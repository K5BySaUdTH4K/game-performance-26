# game-performance-26

`game-performance-26` is a lightweight Python toolkit designed to monitor and optimize frame latency and resource allocation for desktop gaming sessions. It provides real-time telemetry to help developers and power users identify bottlenecking processes and stabilize frame pacing.

### Features

*   **Process Priority Injection:** Dynamically adjusts CPU affinity and priority levels for active game windows to reduce background task interference.
*   **Latency Telemetry:** Captures sub-millisecond frame timing data to generate comparative performance reports across different system configurations.
*   **Resource Monitoring:** Tracks VRAM and GPU utilization via NVIDIAs-SMI integration to detect thermal throttling or memory leaks in real-time.
*   **Automated Profiles:** Supports JSON-based configuration files to apply specific optimization presets based on the detected game executable.

### Installation

Requires Python 3.8+ and administrative/sudo privileges to modify system process priorities.

```bash
# Clone the repository
git clone https://github.com/Developer/game-performance-26.git
cd game-performance-26

# Install dependencies
pip install -r requirements.txt

# Run the setup script
python setup.py install
```

### Usage

To start monitoring an active game process, run the module with the target executable name:

```bash
# Monitor a specific game process
python -m gp_monitor --process "Cyberpunk2077.exe" --log-level INFO
```

You can also enable the aggressive optimization mode, which attempts to pause non-essential background services while the game is running:

```bash
python -m gp_monitor --process "EldenRing.exe" --optimize-all
```

### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License. See the `LICENSE` file for details.