# Main CLI entry point for system monitor

import sys
import time
import argparse
from datetime import datetime
from .system_info import get_all_metrics


def format_bytes(bytes_value: float) -> str:
    """Format bytes to human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.1f} {unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.1f} PB"


def print_metrics(metrics: dict) -> None:
    """Print formatted system metrics."""
    print("System Monitor - CLI Tool")
    print("=" * 30)
    print()

    # CPU
    print(f"CPU Usage: {metrics['cpu']:.1f}%")

    # Memory
    mem = metrics['memory']
    print(f"Memory: {format_bytes(mem['used'])} / {format_bytes(mem['total'])} ({mem['percentage']:.1f}%)")

    # Disk
    disk = metrics['disk']
    print(f"Disk (/): {format_bytes(disk['used'])} / {format_bytes(disk['total'])} ({disk['percentage']:.1f}%)")

    # Network
    net = metrics['network']
    print(f"Network: Sent {format_bytes(net['bytes_sent'])}, Received {format_bytes(net['bytes_recv'])}")

    print()
    print(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="CLI System Monitor - Display system resource usage",
        prog="cli-system-monitor"
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=1.0,
        help="Update interval in seconds (default: 1.0)"
    )
    parser.add_argument(
        "--once",
        action="store_true",
        help="Display metrics once and exit"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="CLI System Monitor 0.1.0"
    )

    args = parser.parse_args()

    try:
        if args.once:
            metrics = get_all_metrics()
            print_metrics(metrics)
            return 0

        # Continuous monitoring
        while True:
            metrics = get_all_metrics()
            print_metrics(metrics)
            time.sleep(args.interval)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.", file=sys.stderr)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())