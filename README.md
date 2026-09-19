[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# game-performance-26

`game-performance-26` is a lightweight Python telemetry library designed to track real-time frame rates, frametimes, and system resource utilization during active gameplay sessions. It compiles low-overhead benchmark logs into actionable visual reports to help developers pinpoint rendering bottlenecks and engine hitches instantly.

## Features

- **High-Precision Frametime Analysis:** Captures 1% low and 0.1% low FPS metrics alongside frame duration variances with sub-millisecond accuracy.
- **Hardware Telemetry Monitoring:** Tracks CPU per-core load, VRAM allocation, and GPU thermals during execution without impacting rendering threads.
- **Automated Report Generation:** Automatically outputs aggregated performance logs into standalone HTML charts and structured JSON datasets upon session completion.
- **Dynamic Event Tagging:** Allows developers to programmatically flag specific in-game events, such as asset loading or explosion effects, to evaluate localized frame drops.

## Installation

Install the package via pip:

```bash
pip install game-performance-26
```

Or install the latest development build directly from the repository:

```bash
git clone https://github.com/Developer/game-performance-26.git
cd game-performance-26
pip install -e .
```

## Quick Start

Integrate the performance profiler into your game loop:

```python
from game_performance import TelemetryTracker

# Initialize the tracker
tracker = TelemetryTracker(app_name="Demo Engine", target_fps=60)
tracker.start_session()

# Main game loop
while game_is_running:
    tracker.begin_frame()
    
    # Run engine logic and rendering
    update_game_physics()
    render_scene()
    
    # Tag high-stress events for profiling
    if level_loading:
        tracker.tag_event("Level_Transition")
        
    tracker.end_frame()

# Finalize and export session report
tracker.end_session()
tracker.export_report(output_dir="./perf_logs", format="html")
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.