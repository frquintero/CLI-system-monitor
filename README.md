# CLI System Monitor

A cross-platform command-line application that displays real-time system resource usage including CPU usage, memory consumption, disk space, and network activity.

## Features

- **Real-time Monitoring**: Display current system metrics with human-readable formatting
- **Cross-Platform**: Works on Linux, macOS, and Windows
- **CLI Interface**: Simple command-line tool with various options
- **Error Handling**: Graceful degradation when system access fails

## Requirements

- Python 3.11 or higher
- psutil library (automatically installed)

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Display current system metrics once:
```bash
PYTHONPATH=src python -m cli_system_monitor.monitor --once
```

Continuous monitoring with 1-second intervals:
```bash
PYTHONPATH=src python -m cli_system_monitor.monitor
```

### Command Line Options

- `--once`: Display metrics once and exit (default behavior)
- `--interval <seconds>`: Set update interval for continuous monitoring (default: 1.0)
- `--help`: Show help message
- `--version`: Show version information

### Sample Output

```
System Monitor - CLI Tool
==============================

CPU Usage: 15.3%
Memory: 4.2 GB / 8.0 GB (52.5%)
Disk (/): 45.1 GB / 256.0 GB (17.6%)
Network: Sent 125.3 MB, Received 890.7 MB

Last updated: 2025-10-17 19:30:00
```

## Technology Stack

- **Language**: Python 3.11
- **Core Library**: psutil for cross-platform system monitoring
- **Linting**: Ruff for code quality
- **Packaging**: Standard Python packaging with pyproject.toml

## Project Structure

```
src/
├── cli_system_monitor/
│   ├── __init__.py
│   ├── monitor.py       # Main CLI entry point
│   └── system_info.py   # System metrics collection
├── tests/
│   ├── unit/
│   └── integration/
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Development

### Code Quality

Run linting:
```bash
ruff check src/
```

Format code:
```bash
ruff format src/
```

### Testing

Run tests (when implemented):
```bash
python -m pytest tests/
```

## License

This project is part of the SpecKit development framework.