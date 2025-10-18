# Data Model: CLI System Monitor

## Overview

The CLI System Monitor is a simple application that collects and displays system metrics in real-time. There are no persistent data entities or complex relationships, as all data is collected dynamically from the system.

## System Metrics

### CPU Usage
- **Type**: Float (percentage)
- **Range**: 0.0 - 100.0
- **Description**: Current CPU utilization across all cores
- **Validation**: Must be between 0 and 100

### Memory Usage
- **Fields**:
  - used: Integer (bytes)
  - total: Integer (bytes)
  - percentage: Float (0-100)
- **Description**: RAM usage statistics
- **Validation**: used <= total, percentage = (used/total) * 100

### Disk Usage
- **Fields**:
  - mount_point: String (e.g., "/")
  - used: Integer (bytes)
  - total: Integer (bytes)
  - percentage: Float (0-100)
- **Description**: Primary disk storage usage
- **Validation**: used <= total, percentage = (used/total) * 100

### Network Activity
- **Fields**:
  - bytes_sent: Integer
  - bytes_recv: Integer
  - packets_sent: Integer
  - packets_recv: Integer
- **Description**: Network interface statistics (aggregate across all interfaces)
- **Validation**: All values >= 0

## Data Flow

1. **Collection**: System metrics gathered using psutil library
2. **Processing**: Raw data converted to human-readable formats
3. **Display**: Formatted output printed to console
4. **No Storage**: Data is ephemeral and not persisted

## Error Handling

- If metric collection fails, display "N/A" for that metric
- Continue displaying other available metrics
- Log errors internally if verbose mode enabled