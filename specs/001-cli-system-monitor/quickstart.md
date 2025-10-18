# Quick Start: CLI System Monitor

## Overview

The CLI System Monitor is a cross-platform command-line tool that displays real-time system metrics including CPU usage, memory usage, disk space, and network activity.

## Prerequisites

- Python 3.11 or higher
- pip for package installation

## Installation

1. Clone the repository and navigate to the project root
2. Install dependencies:
   ```bash
   pip install psutil
   ```
3. Run the application:
   ```bash
   python -m cli_system_monitor.monitor
   ```

## Usage

### Basic Usage

```bash
# Run from project root
python src/cli_system_monitor/monitor.py

# Or if installed as module
python -m cli_system_monitor.monitor
```

### Sample Output

```
System Monitor - CLI Tool
==========================

CPU Usage: 45.2%
Memory: 3.2 GB / 8.0 GB (40.0%)
Disk (/): 120.5 GB / 256.0 GB (47.1%)
Network: Sent 1.2 MB, Received 5.8 MB

Last updated: 2025-10-17 19:18:00
```

### Options

- `--help`: Show help message
- `--interval <seconds>`: Update interval (default: 1 second)
- `--once`: Display metrics once and exit

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Project Structure

```
src/cli_system_monitor/
├── __init__.py
├── monitor.py       # Main CLI entry point
└── system_info.py   # System metrics collection

tests/
├── unit/
└── integration/
```

## Troubleshooting

- **Permission denied**: Ensure you have read access to system information
- **Import error**: Verify psutil is installed (`pip install psutil`)
- **No output**: Check if running on supported platform (Linux, macOS, Windows)